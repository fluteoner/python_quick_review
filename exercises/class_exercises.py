class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[1]-self.coor1[1])**2 + (self.coor2[0]-self.coor1[0])**2)**0.5

    def slop(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (self.radius*self.radius*3.14*self.height)

    def surface_area(self):
        return (self.radius*self.radius*3.14*2 + self.radius*2*3.14*self.height)



class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		ret = f"Account owner: {self.owner}\n"
		ret += f"Account balance: ${self.balance}"
		return ret

	def deposit(self, money):
		self.balance += money
		print('Deposit Accepted')

	def withdraw(self, money):
		if (self.balance >= money):
			self.balance -= money
			print('Withdraw Accepted')
		else:
			print('Funds Unavailable!')

if __name__ == '__main__':

    print('################')
    print('## class Line ##')
    print('################')
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    li = Line(coordinate1, coordinate2)
    print(li.distance())
    print(li.slop())


    print('####################')
    print('## class Cylinder ##')
    print('####################')
    c = Cylinder(2, 3)
    print(c.volume())
    print(c.surface_area())


    print('###################')
    print('## class Account ##')
    print('###################')
    acct1 = Account('Jose', 100)
    print(acct1)
    acct1.deposit(50)
    print(acct1)
    acct1.withdraw(75)
    print(acct1)
    acct1.withdraw(500)
    print(acct1)
