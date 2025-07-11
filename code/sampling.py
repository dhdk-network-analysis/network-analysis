import pandas as pd

df = pd.read_csv("https://media.githubusercontent.com/media/metmuseum/openaccess/refs/heads/master/MetObjects.csv")
df = df.fillna("")

samp = df.sample(frac = 0.0177, random_state=42)

samp.to_csv('sample.csv')
