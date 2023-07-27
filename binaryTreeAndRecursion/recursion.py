#factorial
def calculateFactorial(num):

    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num -1)
    
print(calculateFactorial(5))

def calculateContigiousSum(num):

    if num == 0:
        return 0
    else:
        return num + calculateContigiousSum(num -1)
    
print(calculateContigiousSum(5))