
with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [int(x) for x in raw_data]

def calculate_fuel(mass):
    fuel =  (mass // 3 - 2)
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)
TOTAL_FUEL = 0
for d in data:
    TOTAL_FUEL += calculate_fuel(d)
print(TOTAL_FUEL)
