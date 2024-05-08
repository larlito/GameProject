import bl_low

def commands():
    command = input('Введите команду которую хотите использовать >> ')
    
    if command == 'create':
        result = bl_low.create_catalog()

    if command == 'delete catalog':
        result = bl_low.delete_catalog()

    if command == 'info':
        result = bl_low.info_catalogs()

    if command == 'book':
        result = bl_low.add_book()

    if command == 'read':
        result = bl_low.read_catalog()

    if command == 'find':
        result = bl_low.find_book()

    if command != 'create' and command != 'delete catalog' and command != 'info' and command != 'book' and command != 'read' and command != 'find':
        print('\nОшибка:введена несуществующая команда\n')



