import requests
import time
import json
import os 
from datetime import datetime

#1. Categories aur unke Keywords define karna 
KEYWORDS = {
    'technology': ['ai', 'software', 'tech', 'code', 'computer', 'data', 'cloud', 'api', 'gpu', 'llm'],
    'worldnews': ['war', 'government', 'country', 'president', 'election', 'climate', 'attack', 'global'],
    'sports': ['nfl', 'nba', 'fifa', 'sport', 'game', 'team', 'player', 'league', 'championship'],
    'science': ['research', 'study', 'space', 'physics', 'biology', 'discovery', 'nasa', 'genome'],
    'entertainment': ['movie', 'film', 'music', 'netflix', 'game', 'book', 'show', 'award', 'streaming']
}

def collect_trending_data():
    headers = {"User-Agent": "TrendPulse/1.0"}
    all_stories = []

# folder banana
    if not os.path.exists('data'):
        os.makedirs('data')

# top stories ki IDs lena
    print("fetching top story IDs..")
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", headers=headers)
        top_ids = response.json()[:500]
    except Exception as e:
        print(f"Error fetching top stories: {e}")
# Hum har category ke liye loop chalayenge taaki 2-second sleep rule follow ho sake        

    for category, keywords in KEYWORDS.items():
        print(f"Searching for stories in category: {category}...")
        count = 0

        for story_id in top_ids:
            if count >= 25:
                break

            try: 
                    item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                    story = requests.get(item_url, headers=headers).json()
                    if not story or 'title' not in story:
                        continue
                    title = story.get('title', '').lower()
    # Keywords match check karna                
                    if any(word in title for word in keywords):
                        story_info = {
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                    all_stories.append(story_info)
                    count += 1
            except Exception as e:
                print(f"Failed to fetch story {story_id}: {e}")
                continue
        #Task 1 Requirement: Har category ke baad 2 second rukna
            print(f"Finished {category}, waiting 2 seconds...")
            time.sleep(2) 

#step 3— Save to a JSON File

    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"data/trends_{date_str}.json"
        
    with open(filename, 'w') as f:
        json.dump(all_stories, f, indent=4)

                
    print(f"Collected {len(all_stories)} stories. Saved to {filename}")
if __name__ == "__main__":
            collect_trending_data()
    