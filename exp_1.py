a = 12
b = 12
c = 1222

big = a

if (a > b):
  if (a < c):
    big = c
  else:
    big = a
else:
  if (b < c):
    big = c
  else:
    big = b
    
print(big)
