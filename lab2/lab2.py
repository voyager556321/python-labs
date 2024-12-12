# Reading the file and processing lines
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    # Splitting the file into lines
    data = file.readlines()

# Splitting each line using split(',')
data_split = [line.strip().split(',') for line in data]

# Assuming the first line contains headers
headers = data_split[0]
data_rows = data_split[1:]

# a) Creating a list where the rating > 7.5 and keeping the first 5 columns
rating_index = headers.index('rating')
filtered_data = [
    [row[headers.index(col)] for col in headers[:5]] for row in data_rows
    if len(row) > rating_index and row[rating_index].replace('.', '', 1).isdigit() and float(row[rating_index]) > 7.5
]

# Generator function
def netflix_filter(rows, headers):
    # Indices of required columns
    language_index = headers.index('language')
    type_index = headers.index('type')
    end_year_index = headers.index('endYear')

    for row in rows:
        if (
            len(row) > max(language_index, type_index, end_year_index) and
            row[language_index] == 'English' and
            row[type_index] in ['series', 'movie'] and
            row[end_year_index].isdigit() and int(row[end_year_index]) > 2015
        ):
            yield {col: row[headers.index(col)] for col in headers}

# Using the generator function
generator_output = list(netflix_filter(data_rows, headers))

# For verification, print the results
print("Filtered list (rating > 7.5, first 5 columns):")
for item in filtered_data[:5]:
    print(item)

print("\nGenerator (language: English, after 2015):")
for item in generator_output[:5]:
    print(item)

