# For Loops

A for loop is similar to a while loop in some ways, and different in other ways. For example, a for loop will allow us to execute some code over and over again, much like a while loop. However, a major difference between the two is that a while loop has a boolean expression, and a for loop does not. In a while loop, the loop will run repetitively until the boolean expression evaluates to false, at which point the loop ends. This is useful when you're creating a loop that runs an unspecified number of times (e.g. our Rock, Paper Scissors game could run over and over again until we choose to quit). A for loop executes the code inside of it for each item in a collection (list, range, etc.).

For example, let's say I wanted to print the 'hello world' 5 times. Without a for loop making this easier for us, our code would look like this:
```
print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
```
However, we can consolidate this by using a for loop:
```
for x in range(0,5):
  print('hello world')
```

The other major differences between while loops and for loops is that a for loop doesn't have a variable creation statement, and it doesn't have an update that changes the variable over time. To see the difference, I've written a while loop below that accomplishes the same thing as the for loop above:
```
x=0
while x<5:
  print('hello world')
  x+=1
```
Notice how in the for loop I don't have to ever initialize the variable, and I don't have to change it using an expression like x+=1. That's because in the for loop x changes automatically each time through the loop, starting at the first item in the collection. The range function generates a list of numbers between 0 and 5. So, the first time through the for loop, x=0. Then x=1, x=2, x=3, and x=4. The range function doesn't include the maximum (in this case 5), so the loop only runs 5 times. Navigate to the Python file to learn more about for loops!
