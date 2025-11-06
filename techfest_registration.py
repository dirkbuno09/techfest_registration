import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Dirk Sebastian A. Buño of APPDAET BTCS2")

participants = int(input("\nHow many participants will register?: "))

if participants <= 0:
    print("Invalid number of participants.")
    sys.exit()

