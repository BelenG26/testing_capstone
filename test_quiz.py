from unittest import TestCase
import unittest
import quiz_01

class TestAnswerChecker(TestCase):

    def test_check_answer_exact_same(self):
        # Arrange
        correct_answer = 'Saturn'
        user_answer = 'Saturn'
        #Action
        result = quiz_01.check_answer(user_answer, correct_answer)
        # Assert
        self.assertEqual(True, result) # dont need
        self.assertTrue(result)

    def test_check_answer_is_wrong(self):
        # Arrange
        correct_answer = 'Saturn'
        user_answer = 'Jupiter'
        # Action
        result = quiz_01.check_answer(user_answer, correct_answer)
        # Assert
        self.assertEqual(False, result)
        self.assertFalse(result)

    def test_check_answer_is_correct_even_with_spaces(self):
        correct_answer = 'Seattle'
        user_answer = '   Seattle   '
        # Action
        result = quiz_01.check_answer(user_answer, correct_answer)
        # Assert
        self.assertTrue(result)

    def test_wrong_answer_is_correct_even_with_spaces(self):
        correct_answer = 'Seattle'
        user_answer = '   Portland   '
        # Action
        result = quiz_01.check_answer(user_answer, correct_answer)
        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()