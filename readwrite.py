#open name.text and save it as my name
with open('name.txt') as f:
    full_text = f.read()

#check of correctly used
print(full_text)

#Write a file with 'Hello, my name is Siddhant'
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is Siddhant Gokhale')
    f.write('\n')