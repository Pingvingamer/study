# Python program a páros/páratlan számok szétválasztásá
# Egy szám páros, ha kettővel osztva a maradék 0
# Ha a maradék 1, a szám páratlan

num = int(input("Adj meg egy számot: "))
if (num % 2) == 0:
   print("{0} páros".format(num))
else:
   print("{0} páratlan".format(num))