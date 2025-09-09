import pandas as pd
import sqlite3

# -----------------------------
# Step 1: Extract
# -----------------------------
titles = pd.read_csv("titles.csv")
credits = pd.read_csv("credits.csv")

print("Raw Titles sample:")
print(titles.head())
print("\nRaw Credits sample:")
print(credits.head())

# -----------------------------
# Step 2: Transform
# -----------------------------

# Clean titles dataset
titles = titles.drop_duplicates()

# Fix release_year
titles['release_year'] = pd.to_numeric(titles['release_year'], errors='coerce')
titles['release_year'] = titles['release_year'].fillna(0).astype(int)

# Handle missing values in important columns
titles['imdb_score'] = titles['imdb_score'].fillna(0)
titles['tmdb_score'] = titles['tmdb_score'].fillna(0)
titles['genres'] = titles['genres'].fillna("Unknown")
titles['age_certification'] = titles['age_certification'].fillna("Unrated")

# Clean credits dataset
credits = credits.drop_duplicates()
credits['name'] = credits['name'].fillna("Unknown")
credits['role'] = credits['role'].fillna("Unknown")

# Merge datasets on 'id'
merged = pd.merge(titles, credits, on="id", how="inner")

print("\nCleaned + Merged sample:")
print(merged.head())

# -----------------------------
# Step 3: Load into SQLite
# -----------------------------
conn = sqlite3.connect("etl_netflix.db")
merged.to_sql("netflix_data", conn, if_exists="replace", index=False)
print("\nData loaded into SQLite database: etl_netflix.db")

# -----------------------------
# Step 4: Run SQL Queries
# -----------------------------

# Example 1: Top 10 actors with most appearances
query1 = """
SELECT name, COUNT(*) as appearances
FROM netflix_data
WHERE role = 'ACTOR'
GROUP BY name
ORDER BY appearances DESC
LIMIT 10;
"""
actors = pd.read_sql(query1, conn)
print("\nTop 10 Actors by appearances:")
print(actors)

# Example 2: Number of movies per year
query2 = """
SELECT release_year, COUNT(*) as movie_count
FROM netflix_data
WHERE type = 'MOVIE'
GROUP BY release_year
ORDER BY release_year DESC
LIMIT 10;
"""
movies_by_year = pd.read_sql(query2, conn)
print("\nMovies per Year (last 10 years):")
print(movies_by_year)

conn.close()
