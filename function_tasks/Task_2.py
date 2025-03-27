         # TASK 2

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

