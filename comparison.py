
import pandas as pd

# Load search results
semantic_df = pd.read_csv("dataset/semantic_search_results.csv")
keyword_df = pd.read_csv("dataset/keyword_search_results.csv")

# Display result counts
print("SEMANTIC SEARCH RESULTS")
print("Total results:", len(semantic_df))

print("\nKEYWORD SEARCH RESULTS")
print("Total results:", len(keyword_df))

# Compare the results
comparison_df = pd.DataFrame({
    "Search Method": ["Semantic Search", "Keyword Search"],
    "Total Results": [len(semantic_df), len(keyword_df)],
    "Unique Documents": [
        semantic_df["document"].nunique(),
        keyword_df["document"].nunique()
    ]
})

# Save comparison
comparison_df.to_csv("dataset/search_comparison.csv", index=False)

print("\nSEARCH COMPARISON")
print(comparison_df)

print("\nComparison completed successfully!")
print("Results saved to: dataset/search_comparison.csv")
