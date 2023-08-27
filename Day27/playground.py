def add(*args):
	print(type(args))
	print(args)
	total = 0
	for n in args:
		total += n
	return total


print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
	# for key, value in kwargs.items():
	# 	print(f"{key}:{value}")
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(2, add=3, multiply=5)


class Car:
	def __init__(self, **kw) -> None:
		self.make = kw.get("make")
		self.model = kw.get("model")
		self.colour = kw.get("colour")
		self.seats = kw.get("seats")

	def __str__(self) -> str:
		return f"Make: {self.make} \nModel: {self.model}"

car = Car(make="Audi")
print(car)