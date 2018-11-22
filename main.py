login = input("Type l for login or N for new password")
Gerald = 0
wrongPassword = 0
if login == "N":
    while True:
        username = input("what is your username")
        if str(username) in open('names.txt').read():
            print("please choose another name " + username +
                  " is already taken")
        else:
            print("Hi " + username)
            file1 = open('names.txt', 'a')
            file1.write('\n')
            file1.write(username)
            file1.close()
            password = input("create a password")
            file2 = open('passwords.txt', 'a')
            file2.write('\n')
            file2.write(password)
            file2.close()
            break

#This here checks if the username is yours
while True:
    usernameL = input("what is your username")
    if str(usernameL) in open('names.txt').read():
        print("yay")
        Gerald += 1
    else:
        print("wrong")
    if Gerald == 1:
        break

with open('names.txt', 'r') as f:
    lines = f.read().split("\n")
word = usernameL  # dummy word. you take it from input
# iterate over lines, and print out line numbers which contain
# the word of interest.
for i, line in enumerate(lines):
  if word in line:  # or word in line.split() to search for full words
    linez = ("Word \"{}\" found in line {}".format(word, i + 1))
file1 = readline(LINEZ)
print(file1)
  
        

if Gerald > 0:
    while True:
        check = input("what is your password")
        if str(check) == file1:
            print("WELCOME WELCOME " + usernameL)
            wrongPassword += 1
        else:
            print("worng")
        if wrongPassword > 0:
            break
