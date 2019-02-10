a = input('Enter Hours: ')
b = input('Enter pay: ')
try:
    a = float(a)
    b = float(b)
except:
    print('error, please enter a numeric input')
    a = input('Enter Hours: ')
    b = input('Enter wages: ')
    a = float(a)
    b = float(b)

print('Total Hours entered', a,'. Pay Entered', b)
if a>40:
    print('Overtime')
    Pay = 40*b + (a-40)*b*1.5
else:
    print("Regular")
    Pay = a*b

print('Total wage recieved by you in a week:', Pay)
