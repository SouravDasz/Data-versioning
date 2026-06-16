import pandas as pd
import numpy as np
import os

data = {
    "name": ["sourav", "ankan"],
    "age": [1, 20]
}

df = pd.DataFrame(data)

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save DataFrame
df.to_csv("data/users.csv", index=False)

print("File saved successfully!")
