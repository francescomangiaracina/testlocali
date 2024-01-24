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
    

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

exit()