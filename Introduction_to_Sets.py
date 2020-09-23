def average(array):
    s=set(array)
    sum=0
    for x in s:
        sum=sum+x
    return(sum/len(s))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
