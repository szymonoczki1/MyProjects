import os

class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b



result = 0
print("Your initial value is {}".format(result))
while True:
    print('0. Exit')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Clear')
    
    choice = input('Select: ')

    if choice not in ['1','2','3','4','5','0']:
        os.system('cls')
        print('Invalid option')
    else:
        choice = int(choice)
    
    if choice == 0:
        break
    if choice == 1:
        secondNumber = float(input('What number do you want to add to the result: '))
        obj = calculator(result, secondNumber)
        result = obj.add()
        os.system('cls')
        print("Result: {}".format(result))
    if choice == 2:
        secondNumber = float(input('What number do you want to subtract from the result: '))
        obj = calculator(result, secondNumber)
        result = obj.sub()
        os.system('cls')
        print("Result: {}".format(result))
    if choice == 3:
        secondNumber = float(input('What number do you want the result to be multiplied by: '))
        obj = calculator(result, secondNumber)
        result = obj.mul()
        os.system('cls')
        print("Result: {}".format(result))
    if choice == 4:
        secondNumber = float(input('What number do you want the result to be divided by: '))
        if secondNumber == 0:
            os.system('cls')
            input('You are a retard!')
            exit()
        obj = calculator(result, secondNumber)
        result = obj.div()
        os.system('cls')
        print("Result: {}".format(result))
    if choice == 5:
        result = 0
        os.system('cls')
        print("Your initial value is now {}".format(result))
    


