def is_leap(y):
 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
 return True
 return False
yr = int(input('enter the starting yr '))
yr += 1
i = 0
ls=[]
while i != 15:
 if is_leap(yr):
 ls.append(yr)
 i += 1
 yr += 1
print (ls)
