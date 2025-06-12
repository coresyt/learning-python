while True:
  options = ('add', 'subtract', 'divide', 'multiply', 'exit')

  for i in range(len(options)):
    print(f"{i} .- {str(options[i]).capitalize()}")
    if i == (len(options) - 1):
      print()
  
  option = options[
    int(input('What operation are you going to do? => '))
  ]

  if option == 'exit':
    break
  
  option1 = int(input('First Number =>'))
  option2 = int(input('Second Number =>'))
  result = 0

  if option == 'add':
    result = option1 + option2
  elif option == 'subtract':
    result = option1 - option2
  elif option == 'multiply': 
    result = option1 + option2
    
