f = open('input')

def get_fuel(mass):
    fuel = int(int(mass) / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + get_fuel(fuel)

sum = 0
for l in f:
    sum += get_fuel(l)

print sum
