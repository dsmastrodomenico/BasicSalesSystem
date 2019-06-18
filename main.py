

clients = ['Ramiro', 'Daniel', 'Jose']


def create_client(client_name):
    global clients
    if client_exists(client_name):
        _message_system(1)
    else:
        # clients += client_name
        # _add_coma()
        clients.append(client_name)
        

def delete_client(client_name):
    global clients
    if client_exists(client_name):
        clients.remove(client_name)
    else:
        _message_system(2)


def update_client(client_name, new_client_name):
    global clients
    if client_exists(client_name):
        # clients = clients.replace(client_name, new_client_name)
        pos = clients.index(client_name) 
        clients.pop(pos)
        clients.insert(pos, new_client_name)
    else:
        _message_system(2)


def client_exists(client_name):
    global clients
    # if client_name+','in clients:
    if client_name in clients:
        return True


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


def _message_system(num_message):
    if num_message == 0:
        return print('Thanks for everything.\nHave a nice day.')
    elif num_message == 1:
        return print('Client already is in the client\'s list!.')
    elif  num_message == 2:
        return print('Client isn\'t in the client\'s list!.')
    elif  num_message == 3:
        return print('Invalid command.')


def _get_cliente_name():
    return input('What is the client name?.\n').capitalize()


if __name__ == '__main__':
    _print_welcome()

    while True:
        command = input('Option:\t').upper()
        
        if command == 'C':
            client_name = _get_cliente_name()
            create_client(client_name)

        elif command == 'D':
            client_name = _get_cliente_name()
            delete_client(client_name)

        elif command == 'U':
            client_name = _get_cliente_name()
            if client_exists(client_name):
                update_client_name = input('Please, Write the new client name:\n').capitalize()
                update_client(client_name, update_client_name)
            else:
                _message_system(2)

        elif command == 'L':
            list_client()

        elif command == 'E':
            _message_system(0)
            break

        else:
            _message_system(3)
        
    