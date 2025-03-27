  # TASK 4
def valid_data(names : list|str)-> list:
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
