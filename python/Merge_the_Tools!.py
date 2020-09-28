def merge_the_tools(string, k):
    for i in range(0,len(string)-1,k):
        s=string[i:i+k]
        s1=set(s)
        for j in s:
            if j in s1:
                print(j,end="")
                s1.remove(j)
        print("")
        s=""
        s1=""

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
