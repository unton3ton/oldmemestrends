import pandas as pd 

df = pd.read_csv('trends.csv')
# df.to_excel("trends.xlsx")

# print(df)
# print(df.sample(5)) # пять случайных строчек
# print(df.shape)
# print(df.info)
# print(df.info(memory_usage=True)) # использованной памяти

# print(df.iloc[100:106]) # iloc получает строки и/или столбцы по числовому индексу
# print(df.iloc[103,4])

# print(df.loc[(df['location'] == "Russia") & (df['category'] == "Сериалы")]) 
# locвыдает строки и/или столбцы по нечисловому значению индекса

# print(df.loc[df['location'] == "Netherlands"])
# print(df.iloc[280:25625]) 
# print(df['category'][280:25625].value_counts())

# print(df.loc[(df['location'] == "Netherlands") & (df['category'] == "Recepten")])
# print(df.loc[(df['location'] == "United Kingdom") & (df['category'] == "Movies")].sort_values('rank'))

print(df.loc[df['category'] == "Memes"].sort_values('rank', ascending=False))
df_meme = df.loc[df['category'] == "Memes"].sort_values('year')
df_meme.to_excel("memestrends.xlsx")
