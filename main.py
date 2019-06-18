

clients = ['Ramiro', 'Daniel', 'Jose']


def create_client(client_name):
    global clients
    if client_name not in clients:
        # clients += client_name
        # _add_coma()
        clients.append(client_name)
    else:
        print('Cliente already is in the client\'s list!.')


def delete_client(client_name):
    global clients
    if client_name not in clients:
        clients.remove(client_name)
    else:
        print('Cliente isn\'t in the client\'s list!.')


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
    print('[E]xit')


if __name__ == '__main__':
    _print_welcome()
    while True:
        command = input('Option:\t')
        if command == 'C':
            client_name = input('What is the client name?.\n')
            create_client(client_name)
            list_client()
        elif command == 'D':
            pass
        elif command == 'L':
            list_client()
        elif command == 'E':
            break
        else:
            print('Invalid command.')
        
    