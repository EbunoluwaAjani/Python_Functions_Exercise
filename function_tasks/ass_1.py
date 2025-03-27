        #Task 1
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





                #Task 2
def adjust_pattern(lst :list) ->list:
    '''
    Replaces spaces with underscores in each string of a given list.

    Args:
        lst (list of str): A list of strings where spaces should be replaced with underscores.

    Returns:
        list of str: A new list with modified strings where spaces are replaced by underscores.
    '''
    new_list = []
    for item in lst:
        if ' ' in item:
            a=item.replace (' ', '_')
            new_list.append(a)
        else:
            new_list.append(item)
    return new_list
my_list = ['first name', 'last_name', 'date of birth']
print(adjust_pattern(my_list))




                    #Task 3
def extract_patterns(lst: list)-> list:
    '''
    Extracts each string of a given list that starts with an uppercase and ends with 'a', If a name begins with a capital letter but doesn't end with 'a',
    convert its last letter to 'a'

    Args:
        lst (list of str): A list of strings containing names.

    Returns:
        list of str: A new list with modified strings where all names that start with an uppercase 
        and ends with 'a' are included.
    '''
    new_list = []
    for item in lst:
        if item[0].isupper() and item.endswith('a'):
            x =item
            new_list.append(x)
        elif item[-1] != 'a' :
            y =item.replace(item[-1],'a')
            new_list.append(y)
                        
       
    return new_list
dec = ['Mayowa', 'chizoba', 'Chigozie']            
print(extract_patterns(dec))


                    #Task 4
def valid_data(names list|str)-> list:
    '''
    Checks each name in the list to ensure it contains only alphabetic characters

    Args:
        lst (list of str): A list of strings containing the inputted names.

    Returns:
        valid_entry: a list of valid names
        wrong_entry : a list of invalid names.
    '''
    import re
    valid_entry= []
    wrong_entry =[]
    print('Enter customer name')
    customer_name = input()
    names.append(customer_name)
    for name in names:
               
        if re.findall('[^A-Za-z]', name) :
            err_message = f'{name} appears to be a wrong entry'
            wrong_entry.append(err_message)
        else: 
            valid_entry.append(name)
    return (f'valid_Entries:{valid_entry}, Wrong_Entries:{wrong_entry}')
marketing_list =['Wofai', 'Zainab', 'A4atullah']  
print(valid_data(marketing_list))
