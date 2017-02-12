"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of vowel phonemes required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


# ===================== Helper Function ======================

def get_pattern(rough_string):
    r""" (str) -> poetry pattern
    
    Precondition: rough_string is in the format of a poetry form.
    
    Return a valid poetry pattern from rough_string.
    
    >>> get_pattern('8 A\n8 A\n8 B\n8 B\n8 A\n8 A\n8 A\n8 B\n4 C\n8 A\n' 
    ... + '8 A\n8 B\n8 B\n8 A\n4 C\n')
    ([8, 8, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 4], ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'C', 'A', 'A', 'B', 'B', 'A', 'C'])
    >>> get_pattern('8 A\n8 A\n5 B\n5 B\n8 A')
    ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A'])
    """
    
    new_list = rough_string.split('\n')
    vowel_phonemes = []
    ryme_scheme = []
    for item in new_list:
        if item[:item.find(' ')].isdigit():
            vowel_phonemes.append(int(item[:item.find(' ')]))
            ryme_scheme.append(item[-1])
    return (vowel_phonemes, ryme_scheme)



# ===================== Required Functions =====================

def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    
    # I create a accumulator and start reading the file.
    pronunciation_dict = {}
    line = pronunciation_file.readline()

    # If the line starts with three semicolons, then it is a comment,
    # and so I need to skip it and move to the next line.
    while line.startswith(';;;'):
        line = pronunciation_file.readline()

    # Once I moved over all the comments, I can start populating the 
    # pronunciation dictionary by adding as keys the string slices made of
    # the line from the beginning up to but not including the double white
    # space, and as values everything that comes after.
    pronunciation_dict[line[:line.find('  ')]] = \
                                         line[line.find('  ') + 2:].split()
    for line in pronunciation_file:
        pronunciation_dict[line[:line.find('  ')]] = \
        line[line.find('  ') + 2:].split()

    # I read every line of the file, so my pronunciation dictionary is complete.
    return pronunciation_dict


def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    
    # I first accumulate the content of the file in a big string, and then
    # turn it into a list in which each item is a poetry form.
    whole_string = ''
    for line in poetry_forms_file:
        whole_string = whole_string + line
    whole_list = whole_string.split('\n\n')
    
    # Now I populate the requested dictonary.
    poetry_form_to_poetry_pattern = {}
    for poetry_form in whole_list:
        index = poetry_form.find('\n')
        poetry_form_to_poetry_pattern[poetry_form[:index]] = \
                                            poetry_form[index + 1:].strip()
        
    # Finally, I fix every value of the dictionary to be a poetry pattern and
    # return the dictionary.
    for name in poetry_form_to_poetry_pattern:
        poetry_form_to_poetry_pattern[name] = \
        get_pattern(poetry_form_to_poetry_pattern[name])
    return poetry_form_to_poetry_pattern
