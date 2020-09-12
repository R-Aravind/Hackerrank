# import re
# function to count all occurence of substring (non-overlapping)
# def count_substring(string, sub_string):
#     count=0
#     string = ''.join(string)
#     sub_string = ''.join(sub_string)
#     pattern= re.compile(r'{}'.format(sub_string))
#     matches = pattern.findall(string)
#     for match in matches:
#         count+=1
#     return count


# function to count all occurence of substring (overlapping)
def count_substring(string, sub_string):
    count=0
    pos=0
    string = ''.join(string)
    sub_string = ''.join(sub_string)
    while pos<len(string):
        pos=(string.find(sub_string,pos))
        if pos != -1:
            pos+=1
            count+=1
        else:
            break
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
