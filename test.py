accNum = 0
with open('bot.txt') as f:
    lines = [line.rstrip('\n') for line in f]
while accNum < len(lines):
    print(lines[accNum])
    accNum += 1