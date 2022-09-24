#initial settings
pointsAddCorrect = int(input('points added if correct : '))
pointsDeductWrong = int(input('points deducted if wrong: '))
pointsDeductBlank = int(input('points deducted if blank: '))
possibleAns = input('answer options: ')
possibleAns = possibleAns.lower()
numberOfQuestions = int(input('number of questions: '))
print()
#print index
print(f"{' '*7}index ",end='')
for i in range(1,numberOfQuestions+1):
    print(i%10,end='')
print()
#answers input
userAns = input('your answer: ')
correctAns = input('correctAns : ')
userAns = userAns.lower()
correctAns = correctAns.lower()
print()
#marking
wrong = []
correct = []
blank = []
for i in range(len(userAns)) :
    if userAns[i] == correctAns[i]:#correct
        correct.append(i+1)
    elif userAns[i] in possibleAns :#wrong
        wrong.append(i+1)
    else :#blank
        blank.append(i+1)
#process questions status
print(f'wrong{" "*(5-len(str(len(wrong))))}({len(wrong)}) : ',end='')
for i in wrong :
    print(i,end=''if wrong.index(i)==len(wrong)-1 else ' , ')
print()
print(f'correct{" "*(3-len(str(len(correct))))}({len(correct)}) : ',end='')
for i in correct :
    print(i,end=''if correct.index(i)==len(correct)-1 else ' , ')
print()
print(f'blank{" "*(5-len(str(len(blank))))}({len(blank)}) : ',end='')
for i in blank :
    print(i,end=''if blank.index(i)==len(blank)-1 else ' , ')
print()
print()
marks = len(correct)*pointsAddCorrect - len(wrong)*pointsDeductWrong - len(blank)*pointsDeductBlank
print(f'marks : {marks} of {numberOfQuestions*pointsAddCorrect}')
print(f'marks : {100/(numberOfQuestions*pointsAddCorrect)*marks} %')
print()
while True :
    pass
