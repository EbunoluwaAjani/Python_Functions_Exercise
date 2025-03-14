                #TASK 3
def extract_patterns(lst :list)-> list:
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