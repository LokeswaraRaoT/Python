#POLINDROME : GIVES SAME 
#Given word is Polindrome or not. True/False
name = input("Enter the Word: ")
rev_word = name[::-1] # [::-1] index Gives the word in reverse order
print(name == rev_word)