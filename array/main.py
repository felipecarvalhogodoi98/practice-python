cars = ["Ford", "Volvo", "BMW"]

print("Cars len:", len(cars))

cars.append("Volvo")
cars.append("Honda")
cars.append("Volksvagem")
cars.append("Toyota")

print(cars)
print(cars.pop())
print(cars)
cars.remove("Honda")
print(cars)
cars.sort()
print(cars)
print(cars[2])
cars.extend([1,2,3])
print(cars)
print(cars.count("Volvo"))