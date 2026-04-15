import pandas as pd
import numpy as np

# Simulate a movie database
genres = ['Action', 'Sci-Fi', 'Comedy', 'Drama', 'Horror']
np.random.seed(42)

data = {
    'Movie_ID': range(1, 1001),
    'Title': [f"Movie_{i}" for i in range(1, 1001)],
    'Genre': np.random.choice(genres, 1000),
    'Rating': np.random.uniform(1.0, 5.0, 1000),
    'Release_Year': np.random.randint(1990, 2024, 1000)
}

pd.DataFrame(data).to_csv('movies.csv', index=False)
print("Recommendation dataset 'movies.csv' created.")
