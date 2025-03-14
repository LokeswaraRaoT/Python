#Example 5: Prime numbers in another way:
num = int(input("Enter the number: "))
cnt = 0
for i in range(2, num+1):
    if num % i == 0:
        cnt = cnt + 1
if cnt == 1 and num > 2:
    print(f"{i} is a prime")
else:
    print(f"{i} is not a prime")