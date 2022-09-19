coins = [100, 50, 25, 20, 15, 10, 5, 1]
change = 1030

def changeCalc(coinVector, pos, answers, changeValue):
    q = int(changeValue/coinVector[pos])
    answers.append(q)
    changeValue = changeValue-q*coinVector[pos]
    if(pos+1 >= len(coinVector)):
        return answers
    return changeCalc(coinVector, pos+1, answers, changeValue)

print(changeCalc(coins, 0, [], change))