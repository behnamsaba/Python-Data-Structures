def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    my_dic = {}
    for char in phrase:
        if(phrase.count(char) == 1):
            my_dic[char] = 1
        else:
            my_dic[char] = phrase.count(char)
    
    return my_dic
