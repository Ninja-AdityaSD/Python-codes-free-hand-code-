#program for count number of times vowel occur in string

Main_string=input("Enter the string:")
String=Main_string.lower()

vowel_list=["a","e","i","o","u"]

vowel_counter=0

for char in String:
    if char in vowel_list:
        vowel_counter += 1

print(f"Number of vowel occured in {Main_string} is {vowel_counter}")
