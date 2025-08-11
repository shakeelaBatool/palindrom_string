# #  Create a program that checks whether a given string is a palindrome (reads the same forwards and backward).
# char = input("Enter a string: ").lower()
# re_char = ''           #reverse of char
# i = 0

# while i < len(char):
    
#     re_char = char[i] + re_char        
#     i += 1
# if re_char==char:
#     print (re_char," is a palindrom")    
# else:
#     print ("Not a palindrom")    

# # print(re_char)
    
  
# char=input("Enter a string: ").lower()         #madam

# re_char = ''

# i=0

# while i < len(char):

#     re_char += char[i]
#     i += 1
# if re_char==char:
#     print(char," is a palindrom.")
# else:
#     print(char ," is not a palindrom.")        
  

def palindrom(char):
    i=0
    re_char =''
    while i < len(char):
        re_char += char[i]
        i += 1
    if char == re_char:

           print(char, " is a palindrom.")
    else:
            print(char," is not a palindrom")    
    return char

char = input("Enter a string: ").lower() 
result = palindrom(char)

  
