def power(num1,num2):
    ans = 1
    for nums in range(1,num2):
        ans = ans*num1
    return ans



answer = 99
answerhit = False
trials = 0
num1 = input("Input power num1: ")
num2 = input("Input power num2: ")
print ("Power answer: "+str(power(int(num1),int(num2))))
while answerhit == False and trials<4:
    tmpans = input("Please enter a number(1~99):")
    if int(tmpans) == answer:
        print("The answer is correct!!!")
        answerhit = True
    else:
        print("The answer is incorrect!!!")
        trials=trials + 1
        if trials == 4:
            print("Exceeds max guessing!!!")
print("Game completed!!!");