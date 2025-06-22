import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# Create Baseroute
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create routes to the directories
csv_path = os.path.join(base_path, "data", "netflix_titles.csv")
plot_dir = os.path.join(base_path, "plots")

# Create plot directory if not existent
os.makedirs(plot_dir, exist_ok=True)


# Load csv-file
df = pd.read_csv(csv_path)
# Number of rows and columns
print("\nForm (Rows, Columns):", df.shape)


# Clean and transform data
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Extract 'duration'
df[['duration_int', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

# Add to missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

# Remove rows with missing data
df = df.dropna(subset=['date_added'])



# First plot movies vs. shows
df['type'].value_counts().plot(kind='bar', color=['#e50914', '#221f1f'])
plt.title("Distribution: Movies vs. Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "movies_vs_shows.png"))
plt.clf()

# Second plot - releases per year
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(kind='bar', figsize=(10,5))
plt.title("Releases per year")
plt.xlabel("Year")
plt.ylabel("Count Releases")
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "releses_per_year.png"))
plt.clf()

# Third plot - top 10 countries
df['country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 countries most releases")
plt.xlabel("Country")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig(os.path.join(plot_dir, "top_10_countries.png"))
plt.clf()


# Finish
print("Visuals saved succesfully")












"""
# Name of columns
print("\nName of columns:")
print(df.columns)

# Show all datatypes and missing information
print("\nGeneral Information:\n", df.info)





#Missing data per column
print("\nMissing Data per column:")
print(df.isnull().sum())


# Show datatypes
#print("\nDatatype of the column:")
#print(df.dtypes)

# Transform 'date_added' into 'datetime64'
#print(df['date_added'].dtype)


df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors = 'coerce')
# Test
#print("\nDatatype of 'date_added':", df['date_added'].dtype)
#print(df['date_added'].head(10))
#print(df['date_added'].dtype)
#print("Missing Dates:", df['date_added'].isnull().sum())

# Extract ints and words from duration into seperate new columns
df[['duration_int', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
# Transform 'duration_int' from 'object' into 'int'
df['duration_int'] = pd.to_numeric(df['duration_int'])
# Test
#print("\nDuration_int types:\n", df[['duration', 'duration_int', 'duration_unit']].head(10))


# Show the first five lines
print(df.head())

# Show Column and Datatypes
print("\nColumn und Datatypes:")
print(df.info())




# Alter or remove rows with missing information
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] =df['rating'].fillna('UNknown')

df = df.dropna(subset=['date_added'])

# Test
print(df.isnull().sum())


# Comparing
# Films vs. Series
df['type'].value_counts()
# Top 10 Countries with most items
df['country'].value_counts().head(10)
# Most counted genre
df['listed_in'].value_counts()
# Change of count over time


df['type'].value_counts().plot(kind='bar')
plt.title("Distribution: Movies vs. Series")
plt.show()

"""