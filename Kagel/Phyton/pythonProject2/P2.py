import pandas as pd



# save filepath to variable for easier access


melbourne_file_path = 'd:/Git/AI/Kagel/winemag-data-130k-v2.csv'
#melbourne_file_path = 'melb_data.csv'0000

# read the data and store data in DataFrame titled melbourne_data
#melbourne_data = pd.read_csv(melbourne_file_path, index_col="price")
reviews = pd.read_csv(melbourne_file_path)

print(reviews.head())
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))

import numpy as np
import pandas as pd
df = pd.DataFrame(data=np.random.randint(0,10,(5,7)))
print(df)
df.apply(sum)
