import random

# In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.

name = "Nohely"

# Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.

question = "Is this life even real?"

#Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call.

random_number = random.randint(1, 9)

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.

answer = " "

# For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

# First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”

# Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

# Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.



if random_number == 1:
  answer = "Yes-definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"  
else:
  answer = "Please try again"

print(name + ' asks: ' + question)
print("Magic 8-ball's answer: " + answer)