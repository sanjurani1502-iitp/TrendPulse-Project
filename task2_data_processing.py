import pandas as pd
import glob
import os

#Task 1: Load the JSON File

def clean_trend_data():
    json_files = glob.glob('data/trends_*.json')

    if not json_files:
        print("Error: No JSON file found in 'data/' folder.")
        return
    #Sabse latest file pick karna

    latest_file = max(json_files, key=os.path.getctime)

    # Pandas DataFrame mein load karna 
    df = pd.read_json(latest_file)
    print(f"Loaded {len(df)} stories from {latest_file}")

    #Task 2: Clean the Data 
        # 1. Duplicates — remove any rows with the same post_id

    df.drop_duplicates(subset='post_id', inplace=True)
    print(f"After removing duplicates: {len(df)}")

    # 2.Missing values — drop rows where post_id, title, or score is missing
    df.dropna(subset=['post_id', 'title', 'score'], inplace=True)
    print(f"After removing nulls: {len(df)}")

    # 3. Data types — make sure score and num_comments are integers
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)

    # 4.Low quality — remove stories where score is less than 5
    df = df[df['score'] >= 5]
    print(f"After removing low scores: {len(df)}")


    #Task 3: Save as CSV

    output_files = 'data/trends_clean.csv'
    df.to_csv(output_files, index=False)
    print(f"Saved {len(df)} rows to {output_files}")

    print("\nStories per category:")

    summary = df['category'].value_counts()
    for category, count in summary.items():
            print(f"  {category:<15} {count}")

if __name__ == "__main__":
    clean_trend_data()