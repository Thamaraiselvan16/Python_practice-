f=open("text.txt", "w")
f.write("i am writter")
f.close()

f=open("text.txt", "r")
print(f.read())