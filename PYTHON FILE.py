def check(a):
    a = a.lower()
    if a.endswith('.py'):
        return 'yes'
    else:
        return 'no'
a = input()
print(check(a))