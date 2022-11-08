import users as us


def back():
  dist = ['Exit', 'Back']
  us.show_menu(dist)
  select = int(input('\nSelect Option '))
  if select == 2:
    main()


def main():
  us.main_show('user.csv', ['name', 'email'], 'users')


main()
