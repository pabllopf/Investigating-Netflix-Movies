# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Display the first few rows of the DataFrame to understand its structure
print(netflix_df.head())

# Filter movies released in the 1990s
movies_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]

# Display the first few rows of movies from the 1990s
print(movies_1990s.head())

# Find the most frequent movie duration in the 1990s
# We only consider rows where 'duration' is not null
duration_counts = movies_1990s['duration'].dropna().value_counts()

# Display the counts of each duration
print(duration_counts)

# The most frequent duration
most_frequent_duration = duration_counts.idxmax()
print(f"Most frequent movie duration in the 1990s: {most_frequent_duration}")

# Define the duration variable
duration = int(most_frequent_duration)

# Count the number of short action movies released in the 1990s
short_action_movies = movies_1990s[(movies_1990s['duration'] < 90) & (movies_1990s['genre'].str.contains('Action', na=False))]

# Display the count of short action movies
short_movie_count = len(short_action_movies)
print(f"Number of short action movies released in the 1990s: {short_movie_count}")

# Plot histogram of movie durations to visualize the distribution
plt.figure(figsize=(10, 6))
plt.hist(movies_1990s['duration'].dropna(), bins=range(0, 300, 10), edgecolor='black')
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()
