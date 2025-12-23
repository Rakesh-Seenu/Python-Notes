class QuizBrain:

    def __init__(self, question_list):
        """
        Docstring for __init__
        
        :param self: Description
        :param question_list: Description
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """
        Docstring for still_has_questions
        
        :param self: Description
        """
        return self.question_number < len(self.question_list)

    def next_question(self):# self.question_list[0]
        """
        Docstring for next_question
        
        :param self: Description
        """
        current_question = self.question_list[self.question_number] # current_question = question_list[0]
        self.question_number += 1# Increment question number
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Docstring for check_answer
        
        :param self: Description
        :param user_answer: Description
        :param correct_answer: Description
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
        
