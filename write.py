path = input('image path: ')
data = input('data: ')

with open(path, 'ab') as file:
    file.write(bytes(data, encoding='utf-8'))