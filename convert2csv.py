import pandas as pd 
df = pd.read_json('reviews.json')
df.to_csv('jio-reviews.csv')