my_file = open("C:\\Users\\walra\\OneDrive\\Bureau\\Machine Learning\\Python Projects\\OS commands\\data\\lesoir.txt")
my_content = my_file.read()
print(my_content)
my_content2 = my_file.read()
print("This is empty because we read the file a second time. We need to reinitialise " + my_content2)
print("------------------------")
my_file.seek(0)
my_content2 = my_file.read()
print(my_content2)
print("------------------------")
my_file.seek(0)
my_content2 = my_file.readlines()
for i in my_content2:
    print(i)
my_file.close()

import os
print(os.getcwd())
os.chdir("C:\\Users\\walra\\Documents")
print(os.listdir())
os.mkdir("test")
os.rmdir("C:\\Users\\walra\\Documents\\test")

my_file=open("Test.txt",mode="w")
my_file.close()
os.remove("Test.txt")
print("-----------------------------")
for (a,b,c) in os.walk(os.getcwd()):
    print("a:{} b:{} c:{}".format(a,b,c))

import sys
print("eeeeeeeeeeeeeeeeeeee")
print (sys.argv)