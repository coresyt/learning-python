import os
import time

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

while True:
  time.sleep(5)
  clear()
  options = ('add', 'subtract', 'divide', 'multiply', 'exit')

  for i in range(len(options)):
    print('-' * 30)
    print(f"{i + 1} .- {str(options[i]).capitalize()}")
    
    if i == (len(options) - 1):
      print(f"{'-'*30}\n")
  
  optionUsed = int(input('What operation are you going to do? '))
  print()

  if optionUsed > len(options) or optionUsed < 0:
    print('Not exist your option required!!!')
    continue
  
  option = options[
    optionUsed - 1
  ]

  if option == 'exit':
    break

  operationSym = ''
  option1 = int(input('First Number => '))
  option2 = int(input('Second Number => '))
  result = 0

  if option == 'add':
    operationSym = '+'
    result = option1 + option2
  
  elif option == 'subtract':
    operationSym = '-'
    result = option1 - option2
  
  elif option == 'multiply':
    operationSym = '*'
    result = option1 * option2
  
  elif option == 'divide':
    operationSym = '/'
    result = option1 / option2

  while True:
    print(f"Your result is {result} of the operation is {option1} {operationSym} {option2}\n")
    continueOperations = int(input("Do you want continue operation's? 1 is yes "))
    
    if continueOperations == 1:
      break

    time.sleep(10)
