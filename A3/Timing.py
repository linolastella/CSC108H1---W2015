import time
import poetry_functions as f
import poetry_reader as r


t1 = time.perf_counter()


##
##poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
##pattern = ([5, 5, 4], ['*', '*', '*'])
##word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
##                    'GAP': ['G', 'AE1', 'P'],
##                    'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
##                    'LEADS': ['L', 'IY1', 'D', 'Z'],
##                    'WITH': ['W', 'IH1', 'DH'],
##                    'LINE': ['L', 'AY1', 'N'],
##                    'THEN': ['DH', 'EH1', 'N'],
##                    'THE': ['DH', 'AH0'], 
##                    'A': ['AH0'], 
##                    'FIRST': ['F', 'ER1', 'S', 'T'], 
##                    'ENDS': ['EH1', 'N', 'D', 'Z'],
##                    'POEM': ['P', 'OW1', 'AH0', 'M'],
##                    'OFF': ['AO1', 'F']}
##poetry_functions.check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes)
##
a = open('/Users/lino/Desktop/University/Computer Science/108/a3/dictionary.txt')
r.read_pronunciation(a)

t2 = time.perf_counter()
print('The code took {: .2f}ms'.format((t2 - t1) * 1000.))
