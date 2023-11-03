import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("github_users.csv")

print(df.describe())

df_details = pd.read_csv("github_user_details.csv")

print(df_details.describe())

repo_count = df['Repo Count']
follower_count = df['Follower Count']
starred = df_details['Starred Count']
following = df_details['Following']



plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.scatter(follower_count, repo_count, alpha=0.5)
plt.title("Repository Count vs. Follower Count")
plt.xlabel("Follower Count")
plt.ylabel("Repository Count")
plt.grid(True)

plt.show()

plt.close()

plt.savefig('repo_vs_followers.pdf')



plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.scatter(follower_count, starred, alpha=0.5)
plt.title("Follower Count vs. Starred Count")
plt.xlabel("Starred Count")
plt.ylabel("Follower Count")
plt.grid(True)

plt.show()

plt.close()

plt.savefig('followers_vs_start.pdf')




