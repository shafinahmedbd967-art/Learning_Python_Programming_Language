# Zreverse a string without using inbuilt function

text = "Shafin"
# text = "Python"
reverse_text = ""
for ch in text:
    reverse_text = ch + reverse_text
print(reverse_text)

'''
output: 
nifahS
'''


# another way:
text = "Shafin"
reverse_text = text[::-1]
print(reverse_text)
'''
output: nifahS
'''


# another way: 
text = "Shafin"
reverse_text = ""
for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]
print(reverse_text)
'''
output: nifahS
'''