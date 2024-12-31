import pandas as pd

file_path = 'netflix_list.csv'  
data = pd.read_csv(file_path)

# Завдання 1: Ітератор для основного акторського складу (>50 символів)
class CastIterator:
    def __init__(self, dataset):
        self.dataset = dataset
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.dataset):
            row = self.dataset.iloc[self.index]
            self.index += 1
            if len(row['cast']) > 50:
                return row['cast']
        raise StopIteration

# Використання ітератора
print("Перші 10 записів основного акторського складу (довжина > 50):")
cast_iterator = CastIterator(data)
for i in range(10):
    print(next(cast_iterator))

# Завдання 2: Функція для підрахунків
print("\nСтатистика шоу/фільмів:")
def analyze_dataset(dataset):
    # Перетворення стовпця isAdult у числовий формат
    dataset['isAdult'] = pd.to_numeric(dataset['isAdult'], errors='coerce').fillna(0).astype(int)
    
    # Кількість шоу/фільмів для дорослих
    adult_count = sum(dataset['isAdult'] == 1)
    
    # Середній рейтинг для шоу/фільмів з понад 1000 голосів
    high_votes = dataset[dataset['numVotes'] > 1000]
    average_rating = high_votes['rating'].mean()
    
    return adult_count, average_rating

adult_count, avg_rating = analyze_dataset(data)
print("Кількість шоу/фільмів для дорослих:", adult_count)
print("Середній рейтинг для шоу/фільмів з понад 1000 голосів:", avg_rating)

# Завдання 3: Генератор заголовків шоу
print("\nШоу з понад 10 епізодами і рейтингом вище середнього:")
def get_filtered_titles(dataset):
    average_rating_all = dataset['rating'].mean()
    return [
        row['title']
        for _, row in dataset.iterrows()
        if row['episodes'] > 10 and row['rating'] > average_rating_all
    ]

filtered_titles = get_filtered_titles(data)
for title in filtered_titles[:10]:
    print(title)

