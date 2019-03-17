with open('pi_digits.txt') as file_obj: #First, we need to open the file
        contents = file_obj.read()
        print(contents)
        print(contents.__class__)# The variable having been read is of type string!
#We use the with statement so that our file is being properly closed autmatically
#after the block of code has been executed

#Absolute file paths
with open('/home/joshua/Documents/pi_digits_ver2.txt') as file_obj:
    contents = file_obj.read()
    print(contents)

#Reading line by line: Just iterate over the file_obj
file_path = '/home/joshua/Documents/pi_digits_ver2.txt'
with open(file_path) as file_obj:
    for line in file_obj:
        print(line.rstrip())


with open(file_path) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    pi_string += ''


print(pi_string)
print(len(pi_string))
pi = float(pi_string)
print(pi + 3.383)

file_path = 'pi_million_digits.txt'
with open(file_path) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "..." )

#Is my birthday contained in pi?
bday = input("Please enter your birthday in the form mmddyyyy: ")
if bday in pi_string:
    print("Your bday appears in the first million digits of pi!")
else:
    print("Your bday does not appear in the first million digits of pi!")

file_name = '/home/joshua/Programming/python/Merke/django_howto/django_howto.txt'
with open(file_name) as file_obj:
    lines = file_obj.readlines()

#Since strings are immutable pbjects, we have to assgin a new string to the output of the replace method
for line in lines:
    line = line.replace('Django', 'Django unchained')
    print(line.rstrip())

msg = "Django"
msg = msg.replace("Django", "nothing")
print(msg)
