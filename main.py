import pandas as pd

# Sample data: user ratings with Indian names and current movie titles
data = {
    'user': ['Raj', 'Raj', 'Aisha', 'Aisha', 'Neha', 'Neha'],
    'movie': ['Pathaan', 'Jawan', 'Pathaan', 'Shamshera', 'Jawan', 'Shamshera'],
    'rating': [5, 4, 4, 3, 2, 5]
}
df = pd.DataFrame(data)

def recommend_movies(user):
    user_ratings = df[df['user'] == user]
    similar_users = df[df['movie'].isin(user_ratings['movie']) & (df['user'] != user)]
    recommendations = similar_users.groupby('movie').agg({'rating': 'mean'}).reset_index()
    recommendations = recommendations[~recommendations['movie'].isin(user_ratings['movie'])]
    return recommendations.sort_values(by='rating', ascending=False)

if __name__ == "__main__":
    user = input("Enter your name (e.g., Raj, Aisha, Neha): ")
    recommended = recommend_movies(user)
    if recommended.empty:
        print("No recommendations available.")
    else:
        print("Recommended movies for you:")
        for index, row in recommended.iterrows():
            print(f"{row['movie']} - Rating: {row['rating']:.2f}")
