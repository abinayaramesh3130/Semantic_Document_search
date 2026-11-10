import pandas as pd
import matplotlib.pyplot as plt

# Load search result files
semantic_df = pd.read_csv("dataset/semantic_search_results.csv")
keyword_df = pd.read_csv("dataset/keyword_search_results.csv")

# Count document occurrences
semantic_counts = semantic_df["document_id"].value_counts()
keyword_counts = keyword_df["document_id"].value_counts()

# Combine the counts
comparison_df = pd.DataFrame({
    "Semantic Search": semantic_counts,
    "Keyword Search": keyword_counts
}).fillna(0)

# Plot comparison chart
comparison_df.plot(kind="bar", figsize=(10, 6))

plt.title("Semantic Search vs Keyword Search")
plt.xlabel("Documents")
plt.ylabel("Number of Results")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save chart
plt.savefig("dataset/search_comparison_chart.png")

print("Visualization completed successfully!")
print("Chart saved to: dataset/search_comparison_chart.png")