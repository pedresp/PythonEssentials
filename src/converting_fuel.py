k_miles = 1609.344
gallon = 3.785411784

def liters_100km_to_miles_gallon(liters):
    return ((liters/gallon)/(100000/k_miles))**-1

def miles_gallon_to_liters_100km(miles):
    return (((k_miles*miles)/gallon)**-1)*100000

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

