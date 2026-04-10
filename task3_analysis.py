import pandas as pd
import numpy as np

def perform_analysis():
# Task 1: Load and Explore 
# Task 2 se bani hui CSV load karna

    df = pd.read_csv('data/trends_clean.csv')
    print(f"Loaded data: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())

    average_score = df['score'].mean()
    average_comments = df['num_comments'].mean()

    print(f"\naverage score : {average_score:,.0f}")
    print(f"average comment : {average_comments:,.0f}")

#2 — Basic Analysis with NumPy

    print("\n--- NumPy Stats ---")

    scores_array = np.array(df['score'])
# NumPy functions ka use

    mean_score = np.mean(scores_array)
    median_score = np.median(scores_array)
    std_score = np.std(scores_array)
    max_score = np.max(scores_array)
    min_score = np.min(scores_array)

    print(f"Mean score : {mean_score:,.0f}")
    print(f"Median score : {median_score:,.0f}")
    print(f"Std deviation: {std_score:,.0f}")
    print(f"Max score : {max_score:,.0f}")
    print(f"Min score : {min_score:,.0f}")

# Sabse zyada stories wali category
    category_counts = df['category'].value_counts()
    top_cat = category_counts.idxmax()
    top_count = category_counts.max()
    print(f"Most stories in: {top_cat} ({top_count} stories)")

# Sabse zyada comments wali story
    top_comm_idx = df['num_comments'].idxmax()
    top_story_title = df.loc[top_comm_idx, 'title']
    top_comm_count = df.loc[top_comm_idx, 'num_comments']
    print(f"Most commented story: \"{top_story_title}\"  — {top_comm_count:,} comments")
    
#task. 3— Add New Columns 
# 1. Engagement: comments ko score se divide karna (+1 taaki error na aaye)
   
    df['engagement'] = df['num_comments']/(df['score']+1)

# 2. Is Popular: True agar score average se bada hai

    df['is_popular']= df['score']> average_score

# Task 4: Save the Result 

    output_files = 'data/trends_analysed.csv'
    df.to_csv(output_files, index=False)
    print(f"\nSaved to {output_files}")

if __name__ == "__main__":
    perform_analysis()