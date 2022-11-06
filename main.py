import users as us

def back():
  dist = ['Exit','Back']
  us.show_menu(dist)
  select = int(input('\nSelect Option '))
  if select == 2:
    main()

def main():
  dist=['users','read users','delete users','update users']
  us.show_menu(dist)
  option =int(input('select option '))

  if option ==1:
    us.data_add('user.csv',['users','email'])
  if option==2:
    data= us.get_data('user.csv')
    print(data)
  if option==3:
    us.data_delete('user.csv')
  if option==4:
    us.update_data('user.csv',['users','email'])
  back()  


main()


     
