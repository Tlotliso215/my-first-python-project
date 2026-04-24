print("""
FULL NAME: TLOTLISO SETEBE
STUDENT NUMBER: 4636286 """)

print("")
print("EXERCISE 1")
print("")

speed_above_limit = int(input("Enter km/h above the speed limit: "))

if  0<speed_above_limit<10:
    print("Warning")
elif 11<speed_above_limit<20:
    print("Fine: R500")
else:
    print("Fine: R1000")


