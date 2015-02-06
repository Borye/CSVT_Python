a = input('first: ')
x = raw_input('what to do +-*/: ')
b = input('second: ')

result = {'+': a + b,
          '-': a - b,
          '*': a * b,
          '/': float(a) / float(b)
          }

'''
print result[x]
this will lead to a error:
if you are using a x that not +-*/, it will have warning messege
'''

print result.get(x, 'please use +-*/')
