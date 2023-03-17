#pytho quiz 

questions= ("How many continents are ther in world?: ", 
            "Which country has the most number of worldcups in cricket?: ",
            "Who is the captain of indian cricket team?: ",
            "How many elements are there in periodic table?:", 
            "What is the captial city of telanagana?: ")

options = (("A. 5","B.6",'C.7',"D.10"),
("A.India","B.Austrila","C.England","D.Paksitan"),
("A.RohitSharma","B.VirtkKhoil","C.RishabPant","D.ShreyasIyer"),
("A.116","B.117","C.118","D.119"),
("A.Hyderabad","B.Mumbai","C.Banglore","D.Vishakpatnam"))
answers = ("C","B","A","C","A")
guesses=[]
score =0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score +=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1
    print('-------------------')
    print('      Results      ')
    print('                   ')
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")



