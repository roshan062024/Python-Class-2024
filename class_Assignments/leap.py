
century = int(input("enter the century : "))


start_year = century * 100
end_year = start_year + 100

leap_years = []


for year in range(start_year, end_year):

    if (year % 4 != 0):
        continue  
    elif (year % 100 != 0):
        leap_years.append(year)  
    elif (year % 400 != 0):
        continue  
    else:
        leap_years.append(year)  

# Print the leap years in the century
print(f"Leap years in the {century}st century:")
print(leap_years)
