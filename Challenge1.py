#Get the data in a list 
with open("challenge_1.txt", "r") as file:
    data = file.read().split("\n\n")

#Seperate the cpu usage of each bot and put it in a list
datalist = []
for str in data:
    datalist.append(str.split("\n"))

#Get the top 5 bots who uses the most cpu
result = [0, 0, 0, 0, 0]
for lists in datalist:
    currentValue=0
    for string in lists:
        currentValue+=int(string)
    for i in range(len(result)):
        if currentValue > result[i]:
            result.insert(i, currentValue)
            del result[-1]
            break

#Print the top 5 usages
print(result)


        


