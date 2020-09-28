marklist=[]
scorelist=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark=[name,score]
        marklist.append(mark)
        scorelist.append(score)

    marklist.sort()
    second_minimum = sorted(set(scorelist))[1]

    for i , j in marklist:
        if j== second_minimum:
            print(i)
