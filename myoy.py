#hellp python
import random

print("hello python")
print("hello world")
print("hello ANika")
x = 10
y = 20
if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y") 
else:
    print("x is greater than y") 

for i in range(5):
    print(i)


number_to_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number_to_guess:
    print("Congratulations! You guessed it!")
else:
    print("Sorry, the number was", number_to_guess)