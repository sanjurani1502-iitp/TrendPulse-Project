import pandas as pd
import matplotlib.pyplot as plt
import os


def create_visualizations():
# 1.task setup data load karna
    file_path = "data/trends_analysed.csv"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} nahi mila pahle task 3 chalana।")
        return
    
    df = pd.read_csv(file_path)

#Create a folder called outputs/ if it doesn't exist

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

#2 — Chart 1: Top 10 Stories by Score 
    top_10 = df.sort_values(by='score', ascending=False).head(10)

#Use the story title on the y-axis (shorten titles longer than 50 characters)

    top_10['display_title'] = top_10['title'].apply(lambda x: x[:47] + '...' if len(x) > 50 else x)

    plt.figure(figsize=(10, 6))
    plt.barh(top_10['display_title'], top_10['score'], color = 'skyblue')
    plt.gca().invert_yaxis()
    plt.title('top 10 Stories by score')
    plt.xlabel('Upvotes (Score)')
    plt.ylabel('Story Title')
    plt.tight_layout()
    plt.savefig('outputs/chart1_top_stories.png') 
    plt.show()
    plt.close()

#Chart 2: Stories per Category
    Category_counts = df['category'].value_counts()
    colors = ['red', 'blue', 'green', 'orange', 'skyblue']
    plt.figure(figsize=(8, 6))
    Category_counts.plot(kind='bar', color=colors)
    plt.title('Stories per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Stories')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/chart2_categories.png')
    plt.show()
    plt.close()

#Chart 3: Score vs Comments
    plt.figure(figsize=(8, 6))

#Colour the dots differently for popular vs non-popular stories (use the is_popular column)

    popular = df[df['is_popular'] == True]
    not_popular = df[df['is_popular'] == False]

    plt.scatter(popular['score'], popular['num_comments'], color='orange', label='Popular Stories', alpha=0.7)
    plt.scatter(not_popular['score'], not_popular['num_comments'], color='gray', label='Average Stories', alpha=0.5)
    
    plt.title('Score vs Number of Comments')
    plt.xlabel('Score')
    plt.ylabel('Comments')
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/chart3_scatter.png')
    plt.show()
    plt.close()

#Bonus — Dashboard -Combine all  charts into one figure:
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('TrendPulse Dashboard', fontsize=20, fontweight='bold')

# top left: bar chart
    axs[0, 0].barh(top_10['display_title'], top_10['score'], color='skyblue')
    axs[0, 0].invert_yaxis()
    axs[0, 0].set_title('Top 10 Stories')

#top right : category count
    axs[0, 1].bar(Category_counts.index, Category_counts.values, color=colors)
    axs[0, 1].set_title('Category Distribution')
    axs[0, 1].tick_params(axis='x', rotation=30)

# bottom left scatter plot
    axs[1, 0].scatter(popular['score'], popular['num_comments'], color='orange', alpha=0.6)
    axs[1, 0].scatter(not_popular['score'], not_popular['num_comments'], color='gray', alpha=0.4)
    axs[1, 0].set_title('Score vs Comments')

 # bottom right sammary text(Data Summary)
    axs[1, 1].axis('off') 
    summary_text = (
        f"Total Stories: {len(df)}\n"
        f"Avg Score: {df['score'].mean():.2f}\n"
        f"Top Category: {Category_counts.idxmax()}\n"
        f"Max Comments: {df['num_comments'].max()}"
    )
    axs[1, 1].text(0.1, 0.5, summary_text, fontsize=14, verticalalignment='center')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('outputs/dashboard.png')
    plt.show()

        
    print("All charts and dashboards have been saved in the 'outputs/' folder")

if __name__ == "__main__":
    create_visualizations()

