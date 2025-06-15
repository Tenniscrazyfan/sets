# file = open("quiz.txt",'r')
# content = file.read()
# print(content)
# file.close()

# file = open("quiz.txt",'a')
# file.write("\n alexa")
# file.close()

file = open("quiz.txt",'r')
content = file.readlines()
print(content)
file.close()
print(content[2])