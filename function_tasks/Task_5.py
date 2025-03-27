def bad_entry_filter(entries):
    '''
    Extract the bad input and output them line by line
    Args:
        List of strings
    Returns:
        line by line output.
    '''
    import re
    for entry in entries:      
        if re.findall('[^A-Za-z]', entry):
           yield entry