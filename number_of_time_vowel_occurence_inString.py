#Program for count how many time vowel occurs in string

Main_string=input("ENter the String:")
vowel_list=["a","e","i","o","u"]        

string= Main_string.lower()             
value_holder={}                         

for char in string:                     
    if char in vowel_list:
        if char in value_holder:
            value_holder[char] += 1
        else:
            value_holder[char]=1

print(value_holder)
