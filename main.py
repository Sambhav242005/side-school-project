import users as us
def list(dist):
  num =1
  for i in dist :
     print('{'+str(num)+'} '+i)
     num = num +1
def main():
  dist=['users','read users']
  list(dist)
  option =int(input('select option '))
  if option ==1:
    us.users('user.csv',['users','email'])
  if option==2:
    us.get_data('user.csv')

main()


     
