import unittest
import poetry_functions

SMALL_PRONOUNCING_LIST = [
    'HOW  HH AW1',
    'NOW N AW1',
    'BROWN  B R AW1 N',
    'COW C AW1',
    'CHOWDER  CH AW1 D ER0',
    'SHOW  SH OW1',
    'TOWN T AW1 N',
    'TOUT T AW1 T',
    'THEMISTOCLES DH EH1 M AH0 S T OW1 K L IY0 Z',
    'THERMOPYLAE TH ER2 M AA1 P IH1 L AY1',
    'THE  DH AH0',
    'PELOPONESSIAN  P EH1 L OW1 P OW1  N IY2 ZH EH1 N',
    'WAR W AO1 R',
    'X IH0 K S',
    'SQUARED S K W EH1 R D',
    'Y W AY1',
    'WHY W AY1',
    'H2SO4 EY1 CH T UW1 EH2 S OW1 F AO1 R',
    'SOFTWOOD S AO1 F T W UH2 D',
    'ORBER AO1 R B ER0',
    'COOPERATIVE  K OW0 AA1 P ER0 EY2 T IH0 V',
    'ACCELERATING AE0 K S EH1 L ER0 EY2 T IH0 NG',
    'THINKING TH IH1 NG K IH0 NG',
    'SARONG S ER0 AO1 NG',
]

pronunciation_dict = {}
for w in SMALL_PRONOUNCING_LIST:
    w_list = w.split()
    pronunciation_dict[w_list[0]] = w_list[1:]

class TestCheckVowelPhonemeCounts(unittest.TestCase):
	
    def test_check_vowel_phoneme_counts_one_line_poem(self):
        """ Test check_vowel_phoneme_counts on a one line poem. """

        poem_lines = ['How now brown cow.']
        pattern = ([4], ['A'])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected)

    # Place your unit test definitions after this line.

    def test_check_vowel_phoneme_counts_mutation(self):
        """ Confirm that check_vowel_phonemes_counts does not mutate
        the list poem_lines. """

        poem_lines = ['Orber chowder.', 'Y Peloponessian?']
        pattern = ([4, 7], ['*', '*'])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = ['Orber chowder.', 'Y Peloponessian?']
        self.assertEqual(poem_lines, expected)


    def test_check_vowel_phoneme_counts_no_requisites(self):
        """ Test check_vowel_phonemes_counts on a poem with no restrictions on
        the number of vowel phonemes. """

        poem_lines = ['How now brown cow.', 'Orber chowder.', 'Y Peloponessian?']
        pattern = ([0, 0, 0], ['A', 'A', 'A'])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected)
        
    def test_check_vowel_phoneme_counts_all_different(self):
        """ Test check_vowel_phoneme_counts on a poem where every line must have
        a different number of vowel phonemes. """

        poem_lines = ['The squared war,', 'the tout.', 'Why thinking?']
        pattern = ([2, 1, 3], ['A', 'B', 'C'])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = ['The squared war,', 'the tout.']
        self.assertEqual(actual, expected)
        
    def test_check_vowel_phoneme_counts_all_equal(self):
        """ Test check_vowel_phoneme_counts on a poem where every line must have
        the same number of vowel_phonemes. """

        poem_lines = ['The war,', 'the tout.', 'How thinking?']
        pattern = ([2, 2, 2], ['*', '*', '*'])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = ['How thinking?']
        self.assertEqual(actual, expected)

    def test_check_vowel_phoneme_counts_empty(self):
        """ Test check_vowel_phoneme_counts on a list of empty string. """

        poem_lines = ['']
        pattern = ([], [])
        actual = poetry_functions.check_vowel_phoneme_counts(poem_lines, 
                     pattern, pronunciation_dict)
        expected = []

# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
