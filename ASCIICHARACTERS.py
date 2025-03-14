#ASCII CHARACTERS : Each character have a number was declared.
#Ex: a = 97,
#Print A to Z in a small letters using function
start = 97
end = 120
def ascii_to_alpha(start_value, end_value):
    for i in range(start, end+1):
        print(chr(i), end=",")
        print(i, end=",")
ascii_to_alpha(start_value = start, end_value = end)