

clients = 'Ramiro, Daniel, Jose, '


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Cliente already is in the client\'s list!.')


def _add_coma():
    global clients
    clients += ', '


def list_client():
    global clients
    print(clients)


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS\n' + ('*' * 50))
    print('What do you like to do today?')
    print('[C]reate client.')
    print('[D]elete client.')
    print('[L]ist clients')


if __name__ == '__main__':
    _print_welcome()

    command = input('Option:\t')
    if command == 'C':
        client_name = input('What is the client name?.\n')
        create_client(client_name)
    elif command == 'D':
        pass
    elif command == 'L':
        list_client()
    else:
        print('Invalid command.')
    
    