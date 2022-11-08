import pandas as pd
import os


def show_menu(dist):
  num = 1
  for i in dist:
    print('{' + str(num) + '} ' + i)
    num = num + 1


def check(csv):
  if os.stat(csv).st_size == 0:
    return False
  else:
    return True


def get_data(csv):
  if check(csv) == True:
    data = pd.read_csv(csv, index_col=0)
    return data


def data_add(csv, list):

  enter = {}
  list_enter = []
  for I in list:
    item = input('enter your ' + I + ' ')
    list_enter.append(item)
    enter[I] = [item]
  df = pd.DataFrame(enter)
  if check(csv) == False:
    df.to_csv(csv)
    print(df)
  else:
    data = get_data(csv)
    data.loc[len(data)] = list_enter
    data.to_csv(csv)
    print(data)
  print(list_enter)


def data_delete(csv):
  if check(csv) == True:
    data = get_data(csv)
    print(data)
    option = int(input("\nSelect index row to delete "))
    data.drop(option, inplace=True)
    data.reset_index(inplace=True)
    print(data)
    data.to_csv(csv)


def update_data(csv, list):
  dist = {}
  num = 1
  for i in list:
    dist[num] = i
  show_menu(list)
  select = int(input("\nSelect Option To Update "))
  column = dist[select]

  if check(csv) == True:
    data = get_data(csv)
    print(data)
    row = int(input("\nSelect index to Be Updated "))
    value = input("\nEnter Value To Update ")
    data.loc[row, column] = value
    print(data)
    data.to_csv(csv)


def main_show(csv, list, name):
  dist = [
    'enter ' + name + ' data', 'read all ' + name + ' data',
    'update existing ' + name + ' data', 'delete existing ' + name + ' data'
  ]
  show_menu(dist)
  select = int(input(' select following option '))
  if select == 1:
    data_add(csv, list)
  elif select == 2:
    data = get_data(csv)
    print(data)
  elif select == 3:
    update_data(csv, list)
  elif select == 4:
    data_delete(csv)
