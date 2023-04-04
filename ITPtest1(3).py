def convertSalary(salary, dest_currency):
    conversion_rates = {
        "CAD": 1.47,
        "USD": 1.18,
        "POUND": 0.91,
        "CAMBODIA": 4847.38
    }
    converted_salary = salary * conversion_rates[dest_currency]
    return converted_salary

salary_euros = float(input("enter your salary in Germany: "))
dest_country = input("Enter the country you want to migrate to: ")

if dest_country == "Canada":
    average_salary_dest = 64000
    dest_currency = "CAD"

elif dest_country == "USA":
    average_salary_dest = 56516
    dest_currency = "USD"

elif dest_country == "Cambodia":
    average_salary_dest = 5649856
    dest_currency = "CAMBODIA"

elif dest_country == "United Kingdom":
    average_salary_dest = 35423
    dest_currency = "POUND"

else:
    print("Invalid country input!")
    dest_currency = None
    average_salary_dest = None

if average_salary_dest is not None and dest_currency is not None:
    converted_salary = convertSalary(salary_euros, dest_currency)

    if converted_salary >= average_salary_dest:
        print("You will be rich in", dest_country, "with a salary of", converted_salary, dest_currency)

    else:
        print("You will be poor in", dest_country, "with a salary of", converted_salary, dest_currency)
