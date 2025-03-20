# try:
#     fh = float(input("Enter hours: "))
#     fr = float(input("Enter rate: "))
#     xp = fh * fr
# except:
#     print("Error, please enter numeric input")
#     quit()
sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
    
except:
    print("Error, please enter numeric input")
    quit()
    
print(fh, fr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr    
print(f"Pay: {xp}")
