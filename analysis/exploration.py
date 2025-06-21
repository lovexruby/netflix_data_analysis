import pandas as pd
import os

#print("Aktuelles Arbeitsverzeichnis: ", os.getcwd())

# Load cvs-file
df = pd.read_csv("data/netflix_titles.csv")


# Number of rows and columns
print("\nForm (Rows, Columns):", df.shape)




"""
# Name of columns
print("\nName of columns:")
print(df.columns)

# Show all datatypes and missing information
print("\nGeneral Information:\n", df.info)





#Missing data per column
print("\nMissing Data per column:")
print(df.isnull().sum())
"""

# Show datatypes
print("\nDatatype of the column:")
print(df.dtypes)

# Transform 'date_added' into 'datetime64'
print(df['date_added'].dtype)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors = 'coerce')
# Test
print("\nDatatype of 'date_added':", df['date_added'].dtype)
print(df['date_added'].head(10))
print(df['date_added'].dtype)
print("Missing Dates:", df['date_added'].isnull().sum())

# Extract ints and words from duration into seperate new columns
df[['duration_int', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
# Transform 'duration_int' from 'object' into 'int'
df['duration_int'] = pd.to_numeric(df['duration_int'])
# Test
print("\nDuration_int types:\n", df[['duration', 'duration_int', 'duration_unit']].head(10))

"""
# Show the first five lines
print(df.head())

# Show Column and Datatypes
print("\nColumn und Datatypes:")
print(df.info())
"""