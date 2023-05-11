import pandas as pd
import numpy as np

#nltk.download('punkt')

df = pd.read_csv("/Users/jakobahlberg/cleaned_data3.csv")



print("Amount of missing values in - ")
for column in df.columns:
    percentage_missing = np.mean(df[column].isna())
    print(f'{column} : {round(percentage_missing*100)}%')

#df.dropna(inplace=True)
#print(df.isnull().sum())

df.info()

#df1 = df[["headline","application_deadline","experience_required",
 #"publication_date", "last_publication_date", "description.text"]].copy()

# Save the cleaned dataframe to a new CSV file
#df1.to_csv('cleaned_data3.csv', index=False)
