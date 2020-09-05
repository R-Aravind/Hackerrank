def split_and_join(line):
    result=line.split(" ")
    return("-".join(result))
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
