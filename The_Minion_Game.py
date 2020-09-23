def minion_game(string):
    vowels='AEIOU'
    kev=0
    stuart=0
    for i in range(0,len(string)):
        if string[i] in vowels:
            kev+=(len(string)-i)
        else:
            stuart+=(len(string)-i)
    if  stuart==kev:
        print("Draw")
    elif kev>stuart:
        print("Kevin {}".format(kev))
    else:
        print("Stuart {}".format(stuart))


if __name__ == '__main__':
    s = input()
    minion_game(s)
