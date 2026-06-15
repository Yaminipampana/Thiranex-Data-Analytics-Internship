import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Load Dataset
df = pd.read_csv("Mall_Customers.csv")

# 2. Select Features
features = ['Annual Income (k$)', 'Spending Score (1-100)']
X = df[features]

# 3. Feature Scaling (Crucial for distance-based K-Means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Model Selection & Validation (Elbow Method & Silhouette Scores)
wcss = []
silhouette_scores = []
k_range = range(2, 11)

# We start from 1 for Elbow, but 2 for Silhouette (Silhouette needs at least 2 clusters)
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    if i >= 2:
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot Validation Plots Side-by-Side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left: Elbow Method
ax1.plot(range(1, 11), wcss, marker='o', color='#1E293B', linewidth=2)
ax1.set_title("Elbow Method (WCSS)", fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel("Number of Clusters", fontsize=10)
ax1.set_ylabel("Inertia (WCSS)", fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

# Right: Silhouette Score
ax2.plot(k_range, silhouette_scores, marker='s', color='#0D9488', linewidth=2)
ax2.set_title("Silhouette Scores (Cluster Density)", fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel("Number of Clusters", fontsize=10)
ax2.set_ylabel("Silhouette Coefficient", fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("elbow_method.png", dpi=150)
plt.close()

# 5. Final K-Means Model Execution (K=5 is selected as optimal)
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Calculate and display the validation metric
final_sil_score = silhouette_score(X_scaled, df["Cluster"])
print(f"--- Model Validation Results ---")
print(f"Optimal Cluster Count Selected: 5")
print(f"Model Silhouette Score: {final_sil_score:.4f}\n")

# 6. Map Cluster IDs to Business Personas
# Map based on the centroids computed from the scaled features:
# Cluster 0: Medium Income, Medium Spend -> Value Shoppers
# Cluster 1: High Income, High Spend -> VIP Shoppers
# Cluster 2: Low Income, High Spend -> Impulsive Buyers
# Cluster 3: High Income, Low Spend -> Careful Spenders
# Cluster 4: Low Income, Low Spend -> Budget-Conscious
cluster_mapping = {
    0: "Value Shoppers",
    1: "VIP Shoppers",
    2: "Impulsive Buyers",
    3: "Careful Spenders",
    4: "Budget-Conscious"
}
df["Customer Segment"] = df["Cluster"].map(cluster_mapping)

# 7. Advanced Visualization (With inverse-scaled centroids)
plt.figure(figsize=(10, 7))

# Custom executive color palette matching our dashboard theme
colors = {
    "VIP Shoppers": "#A855F7",       # Purple
    "Value Shoppers": "#14B8A6",     # Teal
    "Careful Spenders": "#3B82F6",   # Blue
    "Impulsive Buyers": "#F97316",   # Orange
    "Budget-Conscious": "#94A3B8"    # Grey
}

# Scatter plot of customer points
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Customer Segment",
    palette=colors,
    s=100,
    alpha=0.8,
    edgecolor='black',
    linewidth=0.5
)

# Inverse transform centroids to plot them in the original feature space
centroids_scaled = kmeans.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

# Plot centroids with black outlines
plt.scatter(
    centroids_original[:, 0],
    centroids_original[:, 1],
    s=250,
    c='#EF4444',
    marker='X',
    label='Centroids',
    edgecolors='black',
    linewidths=1.5
)

plt.title("Customer Segments (Standardized K-Means)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Annual Income (k$)", fontsize=11)
plt.ylabel("Spending Score (1-100)", fontsize=11)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Customer Segments", title_fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

plt.savefig("customer_segments.png", dpi=150)
plt.close()

# 8. Export Results
df.to_csv("Customer_Segments_Output.csv", index=False)

# Display Summary
print("--- Segment Profile Summary ---")
profile_summary = df.groupby('Customer Segment').agg({
    'Age': 'mean',
    'Annual Income (k$)': 'mean',
    'Spending Score (1-100)': 'mean',
    'CustomerID': 'count'
}).rename(columns={'CustomerID': 'Count'})
print(profile_summary.to_string())

print("\nProcessing completed successfully! Files 'Customer_Segments_Output.csv', 'elbow_method.png', and 'customer_segments.png' have been updated.")