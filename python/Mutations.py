def mutate_string(s,p,c):
    s=list(s)
    s[p]=c
    return (''.join(s))

    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
