file = open('abc.txt', 'r')
for each in file:
    print (each)
file.close()
file = open('abc.txt','a')
file.write("I am a CSE student")
file.close()
file = open('abc.txt','w')
file.write("I am a 3rd year student")
file.close()