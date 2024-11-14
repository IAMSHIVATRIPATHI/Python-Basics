# KBC Game Program
"""
KBC Game Program
This program simulates a simple version of the Kaun Banega Crorepati (KBC) game. It displays a series of questions to the user, 
each with multiple-choice answers. The user must input their answer, and the program will check if it is correct. 
If the answer is correct, the user wins a certain amount of prize money and proceeds to the next question. 
If the answer is incorrect, the game ends, and the user takes home the total amount won so far.
Functions:
- None
Variables:
- questions (list): A list of dictionaries, each containing a question, its options, and the correct answer.
- prize_money (list): A list of integers representing the prize money for each question.
- total_amount (int): The total amount of money the user has won so far.
Flow:
1. Iterate through each question in the questions list.
2. Display the question and its options to the user.
3. Prompt the user to input their answer.
4. Check if the user's answer is correct:
    - If correct, add the corresponding prize money to total_amount and display the current winnings.
    - If incorrect, end the game and display the total amount won.
5. After all questions or upon an incorrect answer, display the total amount the user is taking home.
"""

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    }
]

prize_money = [1000, 5000, 10000]
total_amount = 0

for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if answer == q['answer']:
        total_amount += prize_money[i]
        print(f"Correct! You have won {prize_money[i]} so far.\n")
    else:
        print("Incorrect answer. Game over.")
        break

print(f"You are taking home a total of {total_amount}!")