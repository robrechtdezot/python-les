sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp
else:
    xp = fh * fr    
print(f"Pay: {xp}")

x=-2.0
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')

