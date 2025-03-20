# try:
#     fh = float(input("Enter hours: "))
#     fr = float(input("Enter rate: "))
#     xp = fh * fr
# except:
#     print("Error, please enter numeric input")
#     quit()
def case_1():
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

def case_2(temp):
    if temp == 'es':
        print("Hola")
    elif temp == 'fr':
        return "Bonjour"
    elif temp == 'de':
        print("Guten Tag")
    else:
        return "Hello"
# case_2('es')
# case_2('fr')
# case_2('de')
# case_2('test')

def case_3(h, r):
    if h > 40:
        reg = r * h
        otp = (h - 40.0) * (r * 0.5)
        return reg + otp
    else:
        return float(h * r)

hr = float(input("Enter Hours: "))
ra = float(input("Enter Rate: "))
p = case_3(hr, ra)
print("Pay", p)