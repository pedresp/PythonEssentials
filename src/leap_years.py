def is_year_leap(year):
    if year % 100 == 0:
        return True if year % 400 == 0 else False
    else:
        return True if year % 4 == 0 else False

test_data = [1900, 2000, 2016, 1987, 2100, 2232, 1911]
test_results = [False, True, True, False, False, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
