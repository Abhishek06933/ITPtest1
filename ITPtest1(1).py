month=int(input("Enter the month in the numeric form :"))
day=int(input("Enter the month in the numeric form :"))
year=input("Enter the year as two numerical digits (for example: 98, 20, 21) :")

if month < 1 or month > 12:
    print("Error: Invalid Month Input")
elif day <= 1 or day >= 31:
    print("Error: Invalid Day Input")
elif year.isdigit() == False or len(year) != 2:
    print("Error: Invalid Year Input")
else:
    print("Success: Congratulations! you entered the correct date.")
    print("{}/{}/{}".format(month, day, year))


    