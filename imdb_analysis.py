import pandas as pd

# Load dataset
df = pd.read_csv("IMDb Movies India.csv", sep=",", encoding="latin1", engine="python")

# Display first 5 rows
print(df.head())

# Display basic information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Clean Year column (remove brackets)
df['Year'] = df['Year'].str.replace("(", "", regex=False)
df['Year'] = df['Year'].str.replace(")", "", regex=False)

print(df['Year'].head())

# Top 10 highest rated movies
top_rated = df.sort_values(by="Rating", ascending=False)

print("\nTop 10 Highest Rated Movies:")
print(top_rated[['Name', 'Rating']].head(10))

# Count movies by Genre
genre_count = df['Genre'].value_counts()

print("\nTop 10 Most Common Genres:")
print(genre_count.head(10))

# Average movie rating
average_rating = df['Rating'].mean()

print("\nAverage Movie Rating:")
print(round(average_rating, 2))

# Convert Votes column to numeric (remove commas first)
df['Votes'] = df['Votes'].str.replace(',', '')
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

# Top 10 most voted movies
top_voted = df.sort_values(by="Votes", ascending=False)

print("\nTop 10 Most Voted Movies:")
print(top_voted[['Name', 'Votes']].head(10))