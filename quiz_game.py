import random

print("Welcome to Manvi's Game")

user = input("Do You Wanna Play Game? ")


if user not in ["yes" , "YES" , "Yes" , "yES" , "yaa" ]:
    quit()

print("Let's start the Game , Wohoo")

marks = 0

easy = [{"question" : "who is our prime minister? " , "answer" : "narendra modi"} ,
         {"question" : "what is india's national game ?" , "answer" : "hockey"}]

medium = [{"question" : "Is Mira road in mumbai? " , "answer" : "Kyu btaye"} ,
         {"question" : " Is Mira road in mumbai ?" , "answer" : "yes"}]

hard = [{"question" : "who is our first prime minister ? " , "answer" : "jawaharlal nehru"} ,
         {"question" : "what is india's national bird ?" , "answer" : "pecock"}]
for i in range(3):
    print("choose a level from easy , medium , hard: " )
    user = input()
    if user == "easy":
        easy_1 = random.choice(easy)
        print(easy_1["question"])
        user_answer = input()
        if user_answer == easy_1["answer"]:
            print("correct")
            marks = marks +1
            print("Your marks is :" ,  marks)
        else :
            print("wrong answer" )
            print("The right answer is ", easy_1["answer"] )
            print("Your marks is :" ,  marks)


    elif user == "medium":
        medium_1 = random.choice(medium)
        print(medium_1["question"])
        user_answer = input()
        if user_answer == medium_1["answer"]:
            print("correct")
            marks = marks +1
            print("Your marks is :" ,  marks)
        else :
            print("wrong answer" )
            print("The right answer is ", medium_1["answer"] )
            print("Your marks is :" ,  marks)
    else:
        hard_1 = random.choice(hard)
        print(hard_1["question"])
        user_answer = input()
        if user_answer == hard_1["answer"]:
            print("you are right")
            marks = marks +1
            print("Your marks is :" ,  marks)
        else :
            print("wrong answer" )
            print("The right answer is ", hard_1["answer"] )
            print("Your marks is :" ,  marks)

