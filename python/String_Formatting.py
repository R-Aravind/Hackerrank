def print_formatted(number):
    w=len(bin(number))-2
    for i in range(1,number+1):
        print(str(i).rjust(w," "), end=" ")
        print(str(oct(i)[2:]).rjust(w," "), end=" ")
        print(str(hex(i)[2:].upper()).rjust(w," "), end=" ")
        print(str(bin(i)[2:]).rjust(w," "))

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
