import unittest
import poetry_functions

class TestCountVowelPhonemes(unittest.TestCase):
	
    def test_count_vowel_phonemes_empty(self):
        """ Test count_vowel_phonemes on an empty list of lists. """

        actual = poetry_functions.count_vowel_phonemes([[]])
        expected = 0
        self.assertEqual(actual, expected)

    # Place your unit test definitions after this line.
    
    def test_count_vowel_phonemes_mutation(self):
        """ Confirm that count_vowel_phonemes does not mutate the list
        phonemes. """
        
        phonemes = [['D', 'AE1', 'N', 'Y', 'AH0', 'L'], ['UW1', 'F', 'IY0']]
        actual_list = phonemes
        poetry_functions.count_vowel_phonemes(actual_list)
        expected_list = phonemes
        
        self.assertEqual(actual_list, expected_list)

    def test_count_vowel_phonemes_all_stressed(self):
        """ Test count_vowel_phonemes on a list of lists where each phoneme
        is a vowel phoneme. """
        
        phonemes = [['AY1'], ['EY1'], ['IY1', 'AH0'], ['AY1', 'OW0']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 6
        self.assertEqual(actual, expected)

    def test_count_vowel_phonemes_none(self):
        """ Test count_vowel_phonemes on a list of lists with no vowel
        phonemes. """

        phonemes = [['R', 'W', 'N', 'K', 'L', 'C', 'D'], ['P'], ['B']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_count_vowel_phonemes_every_type(self):
        """ Test count_vowel_phonemes on a list of lists where every type of
        vowel phoneme occur. """
        
        phonemes = [['AY1', 'ER0', 'N', 'K', 'L', 'AE2', 'D']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 3
        self.assertEqual(actual, expected)

    def test_count_vowel_phonemes_end(self):
        """ Test count_vowel_phonemes on a list of lists where a 
        vowel phoneme appears only at the end. """
        
        phonemes = [['P', 'R',], ['SH', 'L', 'IY1']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 1
        self.assertEqual(actual, expected)        

    def test_count_vowel_phonemes_middle(self):
        """ Test count_vowel_phonemes on a list of lists where a 
        vowel phoneme appears in the middle. """

        phonemes = [['B', 'R', 'AE1', 'K']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 1
        self.assertEqual(actual, expected)

    def test_count_vowel_phonemes_start(self):
        """ Test count_vowel_phonemes on a list of lists where a 
        vowel phoneme appears at the beginning. """

        phonemes = [['EH1', 'M'], ['IH1', 'NG', 'K']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 2
        self.assertEqual(actual, expected)

    def test_count_vowel_phonemes_several_equal_vowel_phonemes(self):
        """ Test count_vowel_phonemes on a list of list where appear
        several pairs of equal vowel phonemes. """

        phonemes = [['AH0', 'D', 'V', 'ER1', 'T', 'AH0', 'Z', 'M', 'AH0',
                     'N', 'T'],
                    ['AO1', 'F', 'SH', 'AO1', 'R']]
        actual = poetry_functions.count_vowel_phonemes(phonemes)
        expected = 6
        self.assertEqual(actual, expected)
        
# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
