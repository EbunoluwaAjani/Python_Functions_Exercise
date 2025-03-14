  #TASK 1
def get_first_name(first_name: str) -> str:
    '''
    Takes two items within a string

    Args: 
    ln: string containing two items

    Returns the first item.
    '''
    firstname=first_name.split(' ')[0]
    return firstname

def get_last_name(last_name :str) ->str:
    '''
    Takes two items within a string

    Args: 
    ln: string containing two items

    Returns the last item.
    '''
    lastname=last_name.split(' ')[1]
    return lastname

def get_full_name(full_name: str) -> str:
    '''
    Takes the output of two functions

    Args:
        first_name:outputs a string
        last_name:outputs a string

    Returns:
        concatenated string containing output of both function.
    '''
    fullname = get_first_name(full_name) + ' ' + get_last_name(full_name)
    return f'My name is {fullname}'
y = 'Ebunoluwa Ajani'
print(get_full_name(y))