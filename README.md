Data Engineering ETL Pipeline – Netflix Dataset

Overview
This project demonstrates a Data Engineering workflow using the ETL process.  
It ingests raw Netflix datasets (titles.csv and credits.csv), cleans and merges them, and loads the final dataset into a SQLite database for analysis.

Steps
1. Extract
- Load titles.csv (movie and TV metadata) and credits.csv (cast and crew information) using Pandas.

2. Transform
- Remove duplicate records.
- Handle missing values (IMDb score, TMDB score, genres, etc.).
- Standardize release years.
- Fill missing actor and role values in credits.
- Merge both datasets on the id field.

3. Load
- Store the cleaned, merged dataset in a SQLite database (etl_netflix.db).
- Create a table called netflix_data.

4. SQL Queries
- Query 1: Top 10 actors by number of appearances.
- Query 2: Number of movies released per year for the last 10 years.

Example Outputs

Top 10 Actors by appearances
name                   appearances
Kareena Kapoor Khan    25
Boman Irani            25
Shah Rukh Khan         23
Takahiro Sakurai       21
Priyanka Chopra Jonas  20
Paresh Rawal           20
Amitabh Bachchan       20
Yuki Kaji              19
Nawazuddin Siddiqui    19
Junichi Suwabe         19

Movies per Year (last 10 years)
release_year   movie_count
2022           2788
2021           7384
2020           7842
2019           8042
2018           7061
2017           6052
2016           3739
2015           2152
2014           1830
2013           1904

Tech Stack
- Python (Pandas, SQLite3)
- SQLite for database storage and querying
- VS Code for development

How to Run
1. Clone the repository:
   git clone https://github.com/hxppyKhoza/Data-Pipeline
   cd netflix-etl-pipeline

2. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate   

3. Install dependencies:
   pip install -r requirements.txt

4. Run the ETL pipeline:
   python etl_pipeline.py

5. Inspect the database:
- The script creates etl_netflix.db automatically.
- Open the file in DB Browser for SQLite, or run SQL queries using Python’s sqlite3 library.

Files
- etl_pipeline.py → main ETL script
- titles.csv → Netflix titles metadata
- credits.csv → Netflix credits dataset
- etl_netflix.db → generated SQLite database (excluded from repo due to size)
- requirements.txt → dependencies
- README.md → project documentation

Notes
- The SQLite database file (etl_netflix.db) is not uploaded to GitHub due to size.  
- Running the script will recreate the database on your local machine.
