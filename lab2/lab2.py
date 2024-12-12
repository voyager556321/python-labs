import csv

# Load data from the CSV file
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    netflix_data = list(reader)

# Function to filter rows based on a condition
def filter_data(data, condition):
    return [row for row in data if condition(row)]

# Helper function to safely convert string to float
def safe_float(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default

# Generator function for gradual filtering
def generate_english_shows_after_2015(data):
    for row in data:
        if row['language'] == 'English' and row['type'] in {'Movie', 'TV Show'}:
            if row['endYear'].isdigit() and int(row['endYear']) > 2015:
                yield row

# 1. Filtered list: Rating > 7.5
filtered_high_rating = filter_data(
    netflix_data, 
    lambda row: safe_float(row['rating']) > 7.5
)

# Display the first 5 rows for filtered_high_rating
high_rating_output = [
    [row['imdb_id'], row['title'], row['rating'], row['certificate'], row['startYear']]
    for row in filtered_high_rating[:5]  # Limit to 5 rows
]

print("Filtered list (rating > 7.5, first 5 rows):")
for row in high_rating_output:
    print(row)

# 2. Filtered list: English series or movies after 2015
filtered_english_after_2015 = filter_data(
    netflix_data,
    lambda row: row['language'] == 'English' and row['startYear'].isdigit() and int(row['startYear']) > 2015
)

# Display the first 5 rows for filtered_english_after_2015
english_after_2015_output = [
    [row['imdb_id'], row['title'], row['rating'], row['certificate'], row['startYear']]
    for row in filtered_english_after_2015[:5]  # Limit to 5 rows
]

print("\nGenerated list (English series or movies after 2015, first 5 rows):")
for row in english_after_2015_output:
    print(row)

# Generator function: English language, Movie/TV Show ended after 2015
def generate_english_shows_after_2015(data):
    for row in data:
        if (
            row['language'] == 'English' 
            and row['type'] in ['tvSeries', 'movie'] 
            and row['endYear'].isdigit() 
            and int(row['endYear']) > 2015
        ):
            yield row

# Generator function usage
print("\nGenerated rows (English language, Movie/TV Show ended after 2015, first 5 rows):")
english_shows_generator = generate_english_shows_after_2015(netflix_data)

# Display the first 5 rows only
for _ in range(5):  
    try:                
        row = next(english_shows_generator)
        print([row['imdb_id'], row['title'], row['language'], row['type'], row['endYear']])  # Adjusted columns
    except StopIteration:
        print("No more data available in generator.")
        break

