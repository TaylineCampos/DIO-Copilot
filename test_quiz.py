import unittest

from quiz import Quiz, Question  # Adjust the import based on your actual implementation

class TestQuiz(unittest.TestCase):

    def setUp(self):
        # Setup a sample quiz and questions
        self.question1 = Question("What is the capital of France?", "Paris")
        self.question2 = Question("What is 2 + 2?", "4")
        self.quiz = Quiz([self.question1, self.question2])

    def test_question_text(self):
        self.assertEqual(self.question1.text, "What is the capital of France?")
        self.assertEqual(self.question2.text, "What is 2 + 2?")

    def test_question_answer(self):
        self.assertEqual(self.question1.answer, "Paris")
        self.assertEqual(self.question2.answer, "4")

    def test_quiz_initial_score(self):
        self.assertEqual(self.quiz.score, 0)

    def test_quiz_ask_question(self):
        self.quiz.ask_question(0)
        self.assertEqual(self.quiz.current_question, 0)

    def test_quiz_check_answer_correct(self):
        self.quiz.ask_question(0)
        self.quiz.check_answer("Paris")
        self.assertEqual(self.quiz.score, 1)

    def test_quiz_check_answer_incorrect(self):
        self.quiz.ask_question(0)
        self.quiz.check_answer("London")
        self.assertEqual(self.quiz.score, 0)

    def test_quiz_next_question(self):
        self.quiz.ask_question(0)
        self.quiz.next_question()
        self.assertEqual(self.quiz.current_question, 1)

if __name__ == '__main__':
    unittest.main()