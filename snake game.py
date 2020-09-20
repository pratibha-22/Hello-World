import random
print("you can select from"
      "1. snake"
      "2. water"
      "3. gun"
      "you have only 6 chances")
choice=6
start=1
comp_point=0
human_point=0
list=["snake","water","gun"]
while start<=choice:
    comp=random.choice(list)
    inp=int(input("enter your choice"))
    if (comp=='snake' and inp==1) or (comp=='water' and inp==2) or(comp=='gun' and inp==3):
        print("game tie ")
        print("you and computer has  point",human_point,comp_point)
        print("chance left",choice-start)
        start+=1
    elif (comp=='snake' and inp==2) or (comp=='water' and inp==3) or(comp=='gun' or inp==1):
        print("you lose,computer won")
        comp_point+=1
        print("your point",human_point,"computer point",comp_point)
        print("cahnces left",choice-start)
        start+=1
    elif (comp=='water' and inp==1) or (comp=='snake' and inp==3) or(comp=='gun' and inp==2):
        print("you win")
        human_point+=1
        print("your point",human_point,"and computer point",comp_point)
        print("chances left",choice-start)
        start+=1
    else:
        print("invalid choice")

print("your point",human_point,"and computer point",comp_point)
if(human_point>comp_point):
    print("you win the game")
elif(comp_point>human_point):
    print("you lose try again")
else:
    print("please try again .it is a tie")

