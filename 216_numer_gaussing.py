from random import randint
print("<---welcome to gauss number game-->")
print("rules------->")
print("you guess randome number ")
print("please guess between 1 to 10 ")
print("you win game if guess number is correct")
print("otherwise game play again till you not win")
num=input("lets play so press 1 : ")
if num=="1":
    while(True):
        number=int(input("guess a number : "))
        random_number=randint(1,10)
        if number==random_number:
           print("you won !")
           break
        else:
           print("you loss !")
           print("Correct number is : ",random_number)
           print("batter luck next time !")    
else:
    print("thanks visit our game")