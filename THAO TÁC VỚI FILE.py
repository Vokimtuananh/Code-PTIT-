# b1
f = open("DaySoINP.txt", 'r')
n = f.readline().strip()
a = list(map(int, f.readline().split()))
x = [i for i in a if i % 2 == 0]
file = open('DsySoOUT.txt', 'w')
for i in x:
    file.write(f'{i} ')
# b2
f = open("DaySoINP2.txt", 'r')
n = f.readline().strip()
a = list(map(int, f.readline().split()))
s = 0
for i in a:
    if i % 3 == 0:
        s += i
file = open('DaySoOUT2.txt', 'w')
file.write(str(s))
# b3
f = open('UOCINO.txt')
n = f.readline().strip()
a = [i for i in range(1, int(n) + 1)]
file = open('UOCOUT.txt', 'w')
for i in a:
    file.write(f'{i} ')
# b4
f = open('TBCINP.txt')
n = int(f.readline())
total = 0
count = 0
for line in f:
    a = int(line)
    total += a
    count += 1
if count > 0:
    k = total / count
else:
    k = 0
file = open('TBCOUT.txt', 'w')
file.write(str(k))
# b5
with open('TBCINP2.txt', 'r') as file:
    N = int(file.readline())
    with open('TBCOUT2.txt', 'w') as output_file:
        for i in range(N):
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
            if len(numbers) > 0:
                average = sum(numbers) / len(numbers)
            else:
                average = 0
            output_file.write(str(average) + '\n')
print( )