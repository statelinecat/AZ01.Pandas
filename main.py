import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
#     'Age': [25, 30, 35, 24],
#     'City': ['New York', 'Paris', 'London', 'Berlin']
# }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df[df['Country name'] == 'Russia'])