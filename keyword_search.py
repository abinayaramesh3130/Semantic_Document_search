
import pandas as pd
import os
import re

# Project paths
DOCUMENT_FOLDER = "dataset/documents"
QUERY_FILE = "dataset/queries.csv"
OUTPUT_FILE = "dataset/keyword_search_results.csv"

# Load queries
queries_df = pd.read_csv(QUERY_FILE)

results = []

# Load documents
documents = {}

for filename in sorted(os.listdir(DOCUMENT_FOLDER)):
    if filename.endswith(".txt"):
        file_path = os.path.join(DOCUMENT_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            documents[filename] = file.read()

# Perform keyword search
for _, row in queries_df.iterrows():

    query = str(row["query"]).lower()
    keywords = re.findall(r'\b\w+\b', query)

    print("\nSearching:", query)

    scores = []

    for doc_id, content in documents.items():

        content_lower = content.lower()

        score = sum(
            len(re.findall(r'\b' + re.escape(word) + r'\b', content_lower))
            for word in keywords
        )

        scores.append((doc_id, content, score))

    scores.sort(key=lambda x: x[2], reverse=True)

    for rank, (doc_id, content, score) in enumerate(scores[:5], start=1):

        results.append({
            "query": query,
            "rank": rank,
            "document_id": doc_id,
            "document": content,
            "keyword_score": score
        })

# Save results
results_df = pd.DataFrame(results)

results_df.to_csv(OUTPUT_FILE, index=False)

print("\nKeyword search completed successfully!")
print("Total queries:", len(queries_df))
print("Total results:", len(results_df))
print("Results saved to:", OUTPUT_FILE)
