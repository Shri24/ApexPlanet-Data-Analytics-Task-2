# Import pandas for data handling
import pandas as pd

# Import matplotlib.pyplot for visualization
import matplotlib.pyplot as plt

# Load the cleaned IMDb dataset from local system
df = pd.read_csv(
    r"C:\Users\srika\Downloads\cleaned_IMDB_dataset.csv",
    sep=",",
    encoding="latin1"
)

# Display first 5 rows to preview the dataset
print(df.head())

# Display column names to verify structure
print(df.columns)


# Display number of rows and columns in the dataset
print("Dataset Shape:", df.shape)

# Show data types and non-null values of each column
df.info()

# Generate statistical summary of numeric columns
df.describe()

# Check total missing values in each column
df.isnull().sum()


# Convert release_date column to datetime format (invalid values become NaT)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Extract year from release_date into a new column
df['release_year'] = df['release_date'].dt.year

# Convert duration column to numeric (invalid values become NaN)
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')

# Convert income column to numeric (invalid values become NaN)
df['income'] = pd.to_numeric(df['income'], errors='coerce')

# Convert votes column to numeric (invalid values become NaN)
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

# Convert score column to numeric (invalid values become NaN)
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# Display updated data types after conversions
df.info()


# Import matplotlib for visualization
import matplotlib.pyplot as plt

# Create a figure with specified size
plt.figure(figsize=(8,5))

# Plot histogram to show distribution of IMDb scores
plt.hist(df['score'], bins=20)

# Add title to the chart
plt.title("Distribution of IMDb Scores")

# Label the X-axis
plt.xlabel("Score")

# Label the Y-axis
plt.ylabel("Frequency")

# Display the histogram
plt.show()


# Create a figure with specified size
plt.figure(figsize=(10,5))

# Plot number of movies released each year (sorted by year)
df['release_year'].value_counts().sort_index().plot()

# Add title to the chart
plt.title("Movies Released Per Year")

# Label the X-axis
plt.xlabel("Year")

# Label the Y-axis
plt.ylabel("Number of Movies")

# Display the line chart
plt.show()


# Import numpy for numerical operations
import numpy as np

# Check and count infinite values in duration column
print("Infinite values in duration:",
      np.isinf(df['duration']).sum())

# Replace positive and negative infinite values with NaN
df = df.replace([np.inf, -np.inf], np.nan)

# Create a figure with specified size
plt.figure(figsize=(8,5))

# Plot histogram to show distribution of movie duration
plt.hist(df['duration'], bins=20)

# Add title to the chart
plt.title("Movie Duration Distribution")

# Label the X-axis
plt.xlabel("Duration (Minutes)")

# Label the Y-axis
plt.ylabel("Frequency")

# Display the histogram
plt.show()


# Create a figure with specified size
plt.figure(figsize=(8,5))

# Plot scatter plot to show relationship between income and IMDb score
plt.scatter(df['income'], df['score'])

# Add title to the chart
plt.title("Income vs IMDb Score")

# Label the X-axis
plt.xlabel("Income")

# Label the Y-axis
plt.ylabel("Score")

# Display the scatter plot
plt.show()


# Create a figure with specified size
plt.figure(figsize=(10,5))

# Plot bar chart of top 10 most frequent genres
df['genre'].value_counts().head(10).plot(kind='bar')

# Add title to the chart
plt.title("Top 10 Genres")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the bar chart
plt.show()


# Sort dataset by score in descending order and select top 10 movies
top_movies = df.sort_values(by='score', ascending=False).head(10)

# Display title and score of top 10 highest-rated movies
top_movies[['title', 'score']]


# Import seaborn for advanced visualizations
import seaborn as sns

# Import numpy for numerical operations
import numpy as np

# Create a figure with specified size
plt.figure(figsize=(8,6))

# Plot heatmap to visualize correlation between numeric variables
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True)

# Add title to the heatmap
plt.title("Correlation Matrix")

# Display the heatmap
plt.show()


# Create a boxplot to visualize distribution and detect outliers in IMDb scores
sns.boxplot(x=df['score'])


# Create a pairplot to visualize relationships between all numeric variables
sns.pairplot(df.select_dtypes(include='number'))
