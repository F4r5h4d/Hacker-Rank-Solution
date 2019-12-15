import math
import dis

d = compile('u"\N{DEGREE SIGN}"', '', 'eval')
a = int(input("Enter ab length: "))
b = int(input("Enter BC length: "))
c = a / b
print(round(math.degrees(math.atan(c))), chr(176), sep='')