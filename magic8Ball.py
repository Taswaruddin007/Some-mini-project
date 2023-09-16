import random

answer = ["Yes-you are!", "It's sweet.", "People love it.", "People appreciate it.", "You need to push yourselves."
"Try to overcome from it.", "You should practice it more."]

print("         WELCOME TO THE MAGIC 8 BALL         ")
print()
print()
print("Hello, my friend, what is your name?")
name = input()

def magic8():
    print(f"Ok, {name}. What do you want to know ?")
    print()
    question = input()
    ans = answer[random.randint(0, len(answer)-1)]
    print(ans)
    print()
    print("Hopefully, this message help you.")
    reply()

def reply():
    print()
    print("Do you want to know further ?\nWrite yes or no.")
    print()
    reply1 = input().lower()
    if(reply1 == "yes"):
        magic8()
    elif(reply1 == "no"):
        exit1()
    else:
        print("I cannot understand your response. Please write again.")
        reply()

def exit1():
    print("Thank you for playing the game.")

magic8()
