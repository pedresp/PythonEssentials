from leap_years import is_year_leap

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(year, month):
    if month - 1 == 1:
        return 29 if is_year_leap(year) else 28
    return month_days[month - 1]
def day_of_year(year, month, day):
    '''check arguments'''
    if month < 1 or month > 12:
        return None
    if day < 1 or (day > month_days[month - 1] and month != 2):
        return None
    if month == 2 and day > (29 if is_year_leap(year) else 28):
        return None

    '''calculate solution'''
    count = 0
    for i in range(1, month):
        count += days_in_month(year, i)
    count += day
    return count

if __name__ == "__main__":
    test_data = [[1,13,6], [2004,2,99], [1900,1,1], [2124,5,189], [2004,2,99], [2000,12,31], [87,5,-25], [2005,2,29], [1900,12,31], [2004,2,29]]
    test_results = [None, None, 1, None, None, 366, None, None, 365, 60]
    for i in range(len(test_data)):
        print(test_data[i][0], "/", test_data[i][1], "/", test_data[i][2]," -> ", test_results[i], " -> ", end=" ", sep="")
        result = day_of_year(test_data[i][0], test_data[i][1], test_data[i][2])
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
'''
print('bad args')
print(day_of_year(1, 13, 6))
print(day_of_year(2004, 2, 99))
print(day_of_year(2124, 5, 189))
print(day_of_year(87, 5, -25))
print(day_of_year(2005, 2, 29))
print('good args')
print(day_of_year(1900, 1, 1))
print(day_of_year(1900, 12, 31))
print(day_of_year(2000, 12, 31))
print(day_of_year(2004, 2, 29))
'''