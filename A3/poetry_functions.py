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


# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.

def is_vowel_phoneme(phoneme):
    """ (str) -> bool
    
    Return True if and only if phoneme is a vowel_phoneme.
    
    >>> is_vowel_phoneme('AE1')
    True
    >>> is_vowel_phoneme('')
    False
    """
    
    return phoneme.endswith('0') or phoneme.endswith('1') or \
           phoneme.endswith('2')


def split_into_phonemes(line, word_to_phonemes):
    """ (str, pronunciation dictionary) -> list of list of str

    Precondition: every word in line appears in word_to_phonemes.
    
    Return a list of phonemes line is made of.
    
    >>> word_to_phonemes = {'DANIEL': ['D', 'AE1', 'N', 'Y', 'AH0', 'L'],
    ...                     'IS': ['IH1', 'Z'],
    ...                     'GOOFY': ['G', 'UW1', 'F', 'IY0']}
    >>> split_into_phonemes('Daniel is goofy', word_to_phonemes)
    [['D', 'AE1', 'N', 'Y', 'AH0', 'L'], ['IH1', 'Z'], ['G', 'UW1', 'F', 'IY0']]
    """
    
    phonemes = []
    words_to_analyze = line.split()
    for word in words_to_analyze:
        phonemes.append(word_to_phonemes[clean_up(word)])
    return phonemes


def is_rhyme(line1, line2, word_to_phonemes):
    """ (str, str, pronunciation dictionary) -> bool
    
    Return True if and only if line1 and line1 rhyme.

    >>> word_to_phonemes = {'ON' : ['AA1', 'N'],
    ...                     'THE' : ['DH', 'AH0'],
    ...                     'ABSURD' : ['AH0', 'B', 'S', 'ER1', 'D'],
    ...                     'A' : ['AH0'],
    ...                     'TRICERATOPS' : ['T', 'R', 'AY2', 'S', 'EH1', 'R', 'AH0', 'T', 'AO2', 'P', 'S'],
    ...                     'CLIMBS' : ['K', 'L', 'AY1', 'M', 'Z'],
    ...                     'TREETOPS': ['T', 'R', 'IY1', 'T', 'AO2', 'P', 'S'],
    ...                     'ADJOURNS' : ['AH0', 'JH', 'ER1', 'N', 'Z']}
    >>> is_rhyme('On the', 'absurd, a', word_to_phonemes)
    True
    >>> is_rhyme('The adjourns.', 'triceratops climbs treetops.', word_to_phonemes)
    False
    """
    
    # Split the lines into phonemes.
    first_line = split_into_phonemes(line1, word_to_phonemes)
    second_line = split_into_phonemes(line2, word_to_phonemes)
    
    # Extract the last vowel_phonemes and subsequent(s).
    end1 = last_phonemes(first_line[-1])
    end2 = last_phonemes(second_line[-1])

    # See if they rhyme and return the result.
    for i in range(len(end1)):
        if end1[i] != end2[i]:
            return False
    return True


def group_lines(poem_lines, line_index, poem_pattern):
    """ (list of str, int, poem pattern) -> list of str

    Return a list of lines that must rhyme with the one at index line_index.
    
    >>> poem_pattern = ([0, 0, 0, 0], ['A', 'A', 'B', 'B', 'A'])
    >>> poem_lines = ['On the', 'plains, a', 'triceratops climbs treetops.', 'The day adjourns.', 'Absurd!']
    >>> group_lines(poem_lines, 4, poem_pattern)
    ['On the', 'plains, a', 'Absurd!']
    """
    
    lines_group = []
    for i in range(len(poem_pattern[1])):
        if poem_pattern[1][i] == poem_pattern[1][line_index]:
            lines_group.append(poem_lines[i])
    return lines_group


def should_rhyme(poem_lines, poetry_pattern):
    """ (list of str, poetry pattern) -> list of tuples of int

    Return a list of tuples of int where each tuple contains the indices of two
    lines that should rhyme according to the poetry_pattern.

    >>> poetry_pattern = ([0, 0, 0, 0, 0, 0], ['A', 'A', 'A', 'B', 'B', 'A'])
    >>> poem_lines = ['first_line', 'second_line', 'third_line', 'fourth_line', 'fifth_line', 'sixth_line']
    >>> should_rhyme(poem_lines, poetry_pattern)
    [(0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 5), (3, 4)]
    """
    
    should_rhyme_set = set()
    scheme = poetry_pattern[1]

    for i in range(len(scheme)):
        j = i
        while j < len(scheme):

            # If this is True, then the two corresponding lines should rhyme.
            if scheme[i] != '*' and scheme[j] != '*' and \
               scheme[i] == scheme[j] and i != j:
                
                should_rhyme_set.add((i, j))
            j += 1

    should_rhyme_list = list(should_rhyme_set)
    should_rhyme_list.sort()
    
    return should_rhyme_list

# ===================== Required Functions =====================

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> get_poem_lines('Jen sits quietly,\n  Thinking of assignemnt three.  '
    ... + '\n\nAll ideas bad.  \n')
    ['Jen sits quietly,', 'Thinking of assignemnt three.', 'All ideas bad.']
    >>> get_poem_lines('       \n\n\n\n    ')
    []
    """
    
    poem_lines = poem.split('\n')
    for i in range(len(poem_lines)):
        poem_lines[i] = poem_lines[i].strip()
    while '' in poem_lines:
        poem_lines.remove('')
    return poem_lines


def count_vowel_phonemes(phonemes):
    """ (list of list of str) -> int

    Return the number of vowel phonemes in phonemes.

    >>> phonemes = [['N', 'OW1'], ['Y', 'EH1', 'S']]
    >>> count_vowel_phonemes(phonemes)
    2
    >>> phonemes = [['B', 'IH0', 'F', 'AO1', 'R'], ['G', 'AE1', 'P']]
    >>> count_vowel_phonemes(phonemes)
    3
    """
    
    vowel_phonemes = 0
    for phoneme in phonemes:
        for word in phoneme:
            if is_vowel_phoneme(word):
                vowel_phonemes += 1
    return vowel_phonemes


def last_phonemes(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and subsequent consonant phoneme(s) in 
    phoneme_list.

    >>> last_phonemes(['AE1', 'B', 'S', 'IH0', 'N', 'TH'])
    ['IH0', 'N', 'TH']
    >>> last_phonemes(['IH0', 'N'])
    ['IH0', 'N']
    >>> last_phonemes(['B', 'S'])
    []
    >>> last_phonemes(['S', 'K', 'AA1', 'L', 'ER0', 'SH', 'IH2', 'P', 'S'])
    ['IH2', 'P', 'S']
    """
    
    index = 0
    found_one = False
    for i in range(len(phoneme_list)):
        if is_vowel_phoneme(phoneme_list[i]):
            index = i
            found_one = True
    if not found_one:
        return []
    else:
        return phoneme_list[index:]


def check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    vowel phonemes for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of vowel phonemes, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_vowel_phoneme_counts(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    >>> word_to_phonemes = {'ON' : ['AA1', 'N'],
    ...                     'ABSURD' : ['AH0', 'B', 'S', 'ER1', 'D'],
    ...                     'A' : ['AH0'],
    ...                     'TRICERATOPS' : ['T', 'R', 'AY2', 'S', 'EH1', 'R', 'AH0', 'T', 'AO2', 'P', 'S'],
    ...                     'CLIMBS' : ['K', 'L', 'AY1', 'M', 'Z'],
    ...                     'TREETOPS': ['T', 'R', 'IY1', 'T', 'AO2', 'P', 'S'],
    ...                     'ADJOURNS' : ['AH0', 'JH', 'ER1', 'N', 'Z'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'PLAINS' : ['P', 'L', 'EY1', 'N', 'Z'],
    ...                     'DAY' : ['D', 'EY1']}
    >>> poem_lines = ['On the', 'plains, a', 'triceratops climbs treetops.', 'The day adjourns.', 'Absurd']
    >>> pattern = ([2, 2, 3, 4, 2], ['A', 'A', 'B', 'B', 'A'])
    >>> check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes)
    ['triceratops climbs treetops.']
    """
    
    wrong_count = []
    i = 0
    while i < len(pattern[0]):
        if pattern[0][i] == 0:
            i += 1
        else:
            line_to_check = split_into_phonemes(poem_lines[i], word_to_phonemes)
            vowel_phonemes_num = count_vowel_phonemes(line_to_check)
            if vowel_phonemes_num != pattern[0][i]:
                wrong_count.append(poem_lines[i])
            i += 1
    return wrong_count



def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    >>> poem_lines = ['On the', 'plains, a', 'triceratops climbs treetops.', 'The day adjourns.', 'Absurd!']
    >>> pattern = ([0, 0, 0, 0], ['A', 'A', 'B', 'B', 'A'])
    >>> word_to_phonemes = {'ON' : ['AA1', 'N'],
    ...                     'ABSURD' : ['AH0', 'B', 'S', 'ER1', 'D'],
    ...                     'A' : ['AH0'],
    ...                     'TRICERATOPS' : ['T', 'R', 'AY2', 'S', 'EH1', 'R', 'AH0', 'T', 'AO2', 'P', 'S'],
    ...                     'CLIMBS' : ['K', 'L', 'AY1', 'M', 'Z'],
    ...                     'TREETOPS': ['T', 'R', 'IY1', 'T', 'AO2', 'P', 'S'],
    ...                     'ADJOURNS' : ['AH0', 'JH', 'ER1', 'N', 'Z'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'PLAINS' : ['P', 'L', 'EY1', 'N', 'Z'],
    ...                     'DAY' : ['D', 'EY1']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['On the', 'plains, a', 'Absurd!'], ['triceratops climbs treetops.', 'The day adjourns.']]
    """
    
    # I create an accumulator and determine which lines should rhyme.
    not_rhyme = []
    lines_to_rhyme = should_rhyme(poem_lines, pattern)

    # If there are none, then I'm done.
    if lines_to_rhyme == []:
        return not_rhyme

    # Otherwise, I check if the lines that are supposed to rhyme actually rhyme
    # and accumulate the ones that do not.
    else:
        for pair in lines_to_rhyme:
            line1 = poem_lines[pair[0]]
            line2 = poem_lines[pair[1]]
            if not is_rhyme(line1, line2, word_to_phonemes):
                lines_group = group_lines(poem_lines, pair[1], pattern)
                if lines_group not in not_rhyme:
                    not_rhyme.append(lines_group)
                    
    # Finally, I return them.
    return not_rhyme


if __name__ == '__main__':
    import doctest
    doctest.testmod()
