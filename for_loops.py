# 1) Read the Markdown file and describe the three main differences between a for loop and a while loop using comments:







# 2) Use a for loop to print the numbers 0-10, including 10! Use the for loop in the markdown file as a reference if you need it.
# HINT: The format of a for loop is like this: for variable in collection:








# 3) Remember, a for loop runs for each item in a collection. In python, we can consider a string as a collection of ordered characters. Let's say I had a string
#variable pizza = 'PizzaIsDelicious'. I can use a for loop to print each character in the string. In this case, instead of range(0,5), my collection is the variable
#pizza. Write a for loop that prints each character in your string variable:
pizza = 'PizzaIsDelicious'







# 4a) Another familiar collection we've worked with has been lists! For loops work really well with lists. Write a for loop that prints each item in the list below:
list1 = ['I', 'know', 'how', 'to', 'use', 'for', 'loops!']







# 4b) Write a for loop that prints each string in list1 three times:








# 5) For loops can also have an else statement paired with them, much like if/elif statements and while loops. Write a for loop that prints the integers between 0 and 100
# that are multiples of 10. Then, include an else statement that prints "Finished counting to 100 by 10!"
#HINT: The range function can accept 3 parameters that represent the min, max and step.








# 6) Just like in while loops, you can include conditionals inside of a for loop. Write a for loop that iterates from 1-10 (using range()). When your variable equals 3,
#print 'Your variable is equal to 3!', when your variable equals 6, print '6 is double 3!', when your variable equals 9 print '9 is triple 3!', and for every other number
#print 'Not 3, 6 or 9.'







# 7) You can also use a for loop using your turtle. Given the list of colors below, use your turtle to draw a square where each side is a different color!
#HINT: Think of two actions that your turtle can do each time through the list to complete a square. Don't forget to change the pen color each time through your list as well!
import turtle
t=turtle.Pen()
colors = ['red', 'blue', 'green', 'purple']









# 8) Lastly, you can have a for loop inside of a for loop (Loop-ception!). Given the two lists below, let's try and write a program that pairs and prints each
#adjective with each food. In order to do this, you will need to have a for loop inside of another for loop, and you will need to use a different variable for
#each for loop statement. For example, the format should look like the code below:
'''
for variable1 in list3:
  for variable2 in list4:
    print(variable1, variable2)
'''
#Try to use this formatting to pair and print every adjective in adj with every food in food using a nested for loop:
adj = ['Bloated', 'slippery', 'tiny', 'hairy']
food = ['banana', 'carrot', 'cookie', 'pizza']










####------------------Bonus Questions--------------------####


# 1) Let's say you wanted to allow the user to input a number, and then you wanted to use a for loop to add all of the integers up to and including that number,
#starting with 1. First you would create a variable that asks the user for a number, and you would convert that to an integer. Then, you would want to initiate a for
#loop that runs number+1 times and adds the value of each integer between 1 and the user-submitted number. Write this for loop below, and then print the sum of all
#integers after the loop is done running.
#HINT: For this question, you will have to initialize your sum variable before the for loop if you want to use it after the for loop.







# 2) Using a for loop, create a program that tells the user that every number from 0-100 is either an odd number or an even number. For example, it should print
# '1 is an odd number!', '2 is an even number', '3 is an odd number', etc. HINT: You will need conditionals inside of your for loop, and you will probably need to
#use the modulo operator.





# 3) Using a for loop, write a Python program that prints all the numbers from 0 to 6 except 3 and 6. HINT: You need to use a continue statement.





# 4) Using a for loop, write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five 
#print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". HINT: Modulo operator is your friend.






