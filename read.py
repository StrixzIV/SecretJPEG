path = input('image path: ')

with open(path, 'rb') as file:

    content = file.read()
    offset = content.index(bytes.fromhex('FFD9'))

    file.seek(offset + 2)

    print(str(file.read(), 'utf-8'))