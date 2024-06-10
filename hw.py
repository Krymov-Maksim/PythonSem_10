'''
Урок 10. Построение графиков
Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

'''

import pandas as pd
import random

# lst = ['robot'] * 2
# lst += ['human'] * 2
# lst += ['animal'] * 2

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# print(data)

# =============== Решение ====================

data['tmp'] = 1                                         # Ввожу доп.столбец tmp, все значениея в нем "1"
data.set_index([data.index, 'whoAmI'], inplace=True)    # Устанавливаем, что индексом является столбец 'whoAmI'
data = data.unstack(level=-1, fill_value = 0)           # Переворачиваем таблицу, где совпадает, то остаются "1", иначе "0"
print(data)