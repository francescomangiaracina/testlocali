x = 5
y = 6

print(x+y)

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
    
words = ['primo', 'secondo', 'terzo']

for w in words:
    print(w, len(w))
    

exit()