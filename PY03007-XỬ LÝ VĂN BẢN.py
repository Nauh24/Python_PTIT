import re

text = str()
while True:
    try:
        line = input().lower()
        text += line + " "
    except EOFError:
        break

text = re.split("[.!?]", text) # tach theo cau

for i in text:
    if i.strip():
        i=i.split()
        i[0]=i[0].title()
        print(*i)