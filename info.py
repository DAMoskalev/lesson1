user_info = {'first_name': 'Name', 'last_name': 'Sername'}
print(user_info.get('first_name'))
print('Фамилия?')
user_info['last_name'] = input()
print(user_info.get('last_name'))