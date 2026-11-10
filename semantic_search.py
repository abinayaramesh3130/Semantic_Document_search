
import os
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# Project paths
CHROMA_FOLDER = "chroma_db"
QUERY_FILE = "dataset/queries.csv"
OUTPUT_FILE = "dataset/semantic_search_results.csv"

# Load embedding model
print("Loading Sentence Transformer model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing ChromaDB
client = chromadb.PersistentClient(path=CHROMA_FOLDER)

collection = client.get_collection(
    name="healthcare_documents"
)

# Load search queries
queries_df = pd.read_csv(QUERY_FILE)

results = []

# Perform semantic search
for _, row in queries_df.iterrows():

    query = row["query"]

    print("\nSearching:", query)

    query_embedding = model.encode(
        query,
        convert_to_numpy=True
    )

    search_results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=5
    )

    for i in range(len(search_results["ids"][0])):

        results.append({
            "query": query,
            "rank": i + 1,
            "document_id": search_results["ids"][0][i],
            "document": search_results["documents"][0][i],
            "distance": search_results["distances"][0][i]
        })

# Save results
results_df = pd.DataFrame(results)

results_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSemantic search completed successfully!")
print("Total queries:", len(queries_df))
print("Total results:", len(results_df))
print("Results saved to:", OUTPUT_FILE)
