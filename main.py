# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
#
# В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.

import pandas as pd

df = pd.read_csv('1980sClassics.csv')
print(df.head(5))

df.info()
df.describe()

dfdz = pd.read_csv('dz.csv')
print(dfdz)

dfdz.dropna(inplace=True)

print(dfdz)

group = dfdz.groupby('City')['Salary'].mean()

print(group)
