

clients = ['Ramiro', 'Daniel', 'Jose']

def create_client(client_name):
    global clients
    if client_name not in clients:
        # clients += client_name
        # _add_coma()
        clients.append(client_name)
    else:
        _message_error(1)


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        _message_error(2)


def update_client(client_name, new_client_name):
    global clients
    if client_name in clients:
        # clients = clients.replace(client_name, new_client_name)
        pos = clients.index(client_name) 
        clients.pop(pos)
        clients.insert(pos, new_client_name)
    else:
        _message_error(2)


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
    print('[U]pdate client.')
    print('[L]ist clients')
    print('[E]xit')


def _message_error(num_message):
    if num_message == 1:
        return print('Cliente already is in the client\'s list!.')
    elif  num_message == 2:
        return print('Client isn\'t in the client\'s list!.')


def _get_cliente_name():
    return input('What is the client name?.\n')


if __name__ == '__main__':
    _print_welcome()

    while True:
        command = input('Option:\t')
        command = command.upper()
        
        if command == 'C':
            client_name = _get_cliente_name()
            create_client(client_name)

        elif command == 'D':
            client_name = _get_cliente_name()
            delete_client(client_name)

        elif command == 'U':
            client_name = _get_cliente_name()
            update_client_name = input('Please, Write the new client name:\n')
            update_client(client_name, update_client_name)

        elif command == 'L':
            list_client()

        elif command == 'E':
            break

        else:
            print('Invalid command.')
        
    