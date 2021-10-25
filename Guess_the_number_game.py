'''
Question-
You have to make a python programme, in which you have to make a number guessing game.
followings steps to be remembered-
1. Guesses should be limited.
2. Structured layout.
3. No pips to be imported.
'''

print("Welcome to Number guessing game.")
print("[Note- Guesses are limited.(ie.- 20)]")

print("""
Now, let me give you a hint- 
What is a two digit number, when we write, it seems to be same as itself when flipped vertically?
""")

var1 = 69
var2 = int(input("""Enter a number \tfrom-0 to-100 \n"""))

if var1 == var2:
    print("Congrats, You won the game. 😍, It's 69.")

elif var1 > var2:
    print("You lost.🙁 , Run the code again and try.")

else:
    print("You lost.🙁 , Run the code again and try.")





























