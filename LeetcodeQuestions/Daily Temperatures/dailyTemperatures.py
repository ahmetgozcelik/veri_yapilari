temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

def solution():
    
    result = [0] * len(temperatures)
    myStack = [] # temp&index

    for ix, temperature in enumerate(temperatures):
        while myStack and temperature > myStack[-1][0]:
            stackTemp, stackIndex = myStack.pop()
            result[stackIndex] = ix - stackIndex
        myStack.append([temperature, ix])
    return result

print(solution())