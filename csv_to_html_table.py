import pandas as pd
import os
filepath = os.path.join("static", "cities.csv")
df = pd.read_csv(filepath)
df = df.set_index("City_ID")
df.to_html("data1.html")
    