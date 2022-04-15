import random
l = []
for i in range(6):
    num = random.randint(0,10)
    char_lower = chr(random.randint(97, 122))
    char_capital = chr(random.randint(65, 90))
    curr = random.choice([num, char_capital, char_lower])
    l.append(str(curr))

print(''.join(l))
