from datetime import datetime

a = str(input( ))
b = datetime.strptime(" ", "%m/%d/%Y").date()
c = float(input( ))
d = float(input( ))
e = float(input( ))
f = c + d + e
print(a, b, f )