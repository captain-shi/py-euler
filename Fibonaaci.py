'''The sum of even-valued terms in the fibonacci sequence
not greater than four million'''

a = 1
b = 2
c = 0
fib_seq = [a,b]
Total_sum = 0

while c <= 4000000:
        c = a + b 
        a = b
        b = c
        if c % 2 == 0: 
            Total_sum += c
        fib_seq.append(c)
print(fib_seq)
print('Total sum of even numbers in the series', Total_sum)
             
#Another method

x = 1
y = 2
z = 0
result = 0

while z < 4000000:
    z = (x + y)
    if z % 2 == 0:
        result += z
        
        x = y
        y = z
print(result)


