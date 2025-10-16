 

#The players score is 0 at the start of the game. 
score = 0

#This is so random numbers and opertators can test the player.
import random 
operations = ["+", "-", "*", "/"] 
num_questions = 10 #repeats questions 10 times before final score. 

print("Hello User! Welcome to Math Test")
print("Solve the following questions:") 
input("Press Enter On Your Keyboard To Start The Quiz!")  

for i in range(num_questions): 
    
    op = random.choice(operations)

    if op == "/":
        num2 = random.randint(1,12) 
        result = random.randint(1,12)  #This is so division isnt too hard and in decimals. 
        num1 = num2 * result 
        answer = result 
    else:
        num1 = random.randint(1,12) 
        num2 = random.randint(1,12) 
        answer = eval(f"{num1} {op} {num2} ") 

    question = f"{num1} {op} {num2}"
    answer = eval(question) #python automatically solves the question. 

    user_input = input(f"What is {question}? ") 
#converts the user input to floats (for division)

    if float(user_input) == answer:
        score += 1
        print("Your answer is correct! Nice job!")
    else:
        print(f"Oops! Your answer was not correct. The correct answer was {answer}. Keep trying!") 

    print(f"{score}/{num_questions}") 

print(f"Your score is {score} out of {num_questions}")
print(f"{score}/{num_questions}")  
    
if score >= 1: 
    print("Good Job!")
else:
    print("Nice try, practice makes perfect!")



