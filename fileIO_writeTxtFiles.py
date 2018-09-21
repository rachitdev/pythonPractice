cities = ["New Delhi", "Noida", "Gurgaon", "Bhopal", "Allahabad", "Lucknow", "Chandigarh"]

c = open("cities.txt", 'w')

for city in cities:
    print(city, file=c)