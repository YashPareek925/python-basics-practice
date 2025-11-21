# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File 1/0
# using Java.
# I like programming in Java.

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File 1/0\n")
#     f.write("using Java.\nI like programming in Java.")

# WAF that replace all occurrences of "Java" with "python" in above file.

# with open("practice.txt","r") as f:
#     data=f.read()

# new_data=data.replace("Java","Python")

# with open("practice.txt","r+") as f:
#     f.write(new_data)

# Search if the word "learning" exists in the file or not.

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    line=data.readline(word)
    print(line)
