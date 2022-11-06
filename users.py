import pandas as pd
import os

def users(csv,list):
  
  enter ={}
  list_enter=[]
  for I in list:
    item = input('enter your '+ I +' ')
    list_enter.append(item)
    enter[I]=[item]
  df = pd.DataFrame(enter)
  print(df)
  if os.stat(csv).st_size ==0:
     df.to_csv(csv)
  else:
     data =pd.read_csv(csv,index_col=0)
     data.loc[len(data)] = list_enter
     data.to_csv(csv)
def get_data(csv):
    if os.stat(csv).st_size ==0:
     print('no data')
    else:
     data = pd.read_csv(csv,index_col=0)
     print(data)
  
  