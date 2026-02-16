# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
import random
def math_quiz():
    n1 = random.randint(1, 500)
    n2 = random.randint(1, 500)
    print(n1, "+", n2, "=")
    my_answer = n1 + n2
    your_answer = int(input("What is your answer? "))  
    if my_answer == your_answer:
        print("GREAT JOB!!! You are correct!")
    else:
        print("WRONG!! The answer was", my_answer)


math_quiz()
# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.