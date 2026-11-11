#take any string from user and print the number of vowels in it
user_string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in user_string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)