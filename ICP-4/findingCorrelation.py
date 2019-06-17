# import libraries
import pandas as pd

# read csv file using pandas library (pd.read_csv
train_df = pd.read_csv("data/train.csv")

# find correlation using grouping by 'Sex' and finding mean and sorting
print(train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False)
      .mean().sort_values(by='Survived', ascending=False))
