#program to let me know palendrome or not
user_string = input("Enter a string: ")
original_string = user_string
#cleaned_string = ''.join(c.lower() for c in user_string if c.isalnum())
reversed_string = user_string[::-1]
if user_string == reversed_string: 
    is_palindrome = True
print("Is the string a palindrome?", is_palindrome)