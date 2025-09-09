Data Engineering ETL Pipeline – Netflix Dataset

Overview
This project demonstrates a Data Engineering workflow using the ETL process.  
It ingests raw Netflix datasets (`titles.csv` and `credits.csv`), cleans and merges them, and loads the final dataset into a SQLite database for analysis.

Steps
1. Extract
   - Load `titles.csv` (movie/TV metadata) and `credits.csv` (cast & crew info) using Pandas.
2. Transform
   - Handle missing values (IMDb score, TMDB score, genres, etc.).
   - Standardize release years.
   - Clean duplicates in both datasets.
   - Fill missing actor/crew names and roles.
   - Merge both datasets on the `id` field.
3. Load
   - Store the cleaned, merged dataset in a SQLite database (`etl_netflix.db`).
   - Create a table called `netflix_data`.
4. SQL Queries
   - Example 1: Find the **Top 10 actors** by number of appearances.  
   - Example 2: Count the **number of movies per year** for the last 10 years.

Tech Stack
- Python (Pandas, SQLite3)
- SQLite (for data storage and querying)
- VS Code (for development)

