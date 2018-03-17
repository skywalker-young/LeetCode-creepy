def predictPartyVictory( senate):
    n = len(senate)
    countD = 0
    senate = [1 if i == "D" else -1 for i in senate]
    for i in senate:
        countD += i
        if countD * i > 0:
            senate.append(i)
        if abs(countD) > n:
            return "Dire" if countD > 0 else "Radiant"


print(predictPartyVictory("RD"))
