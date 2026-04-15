import pandas as pd
import joblib

# Load and clean
df = pd.read_csv('movies.csv')

# In a real system, you'd calculate cosine similarity here.
# For this API, we save the processed dataframe as our 'model'.
joblib.dump(df, 'recommender_data.pkl')
print("Recommender data saved successfully.")
