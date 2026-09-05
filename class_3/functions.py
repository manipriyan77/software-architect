##FUNCTIONS

# Divide and Conquer

# Solving Problem Statements
# for eg.
# task : prepare Tea

# job1:  addIngredients()
# job2:  boil()
# job3:  serveTea()

# to represent a small task or  job python provides
# a concept called FUNCTION.
# function represents a block of code to do a specific
# task

# grammer or syntax #(do not execute the code below)

# def <Function_Name_Here>() :
#   Your CODE GOES HERE


def greet():
  print('Good Morning')

greet()

greet()
greet()
greet()


# Can i Transfer Data to a Function ?

# answer: YES , you can.


def broadCast(  msg ):
  print('Message : ', msg ,' broadcasted')

broadCast( 'OKRA' )


def whatisNext( num ):
  print('Next is ' , num+1)

whatisNext(7)

# Function with Return

def giveMeHundered():
  return 100


result  =     giveMeHundered()

print('i Recieved ', result)

# eg. that helps build confidence ( then closing this topic)

def calcSquare(  num ):
  result = num * num
  return result

answer = calcSquare( 7 )

print('Square is ', answer)