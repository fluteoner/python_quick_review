# Abstract Class
# A class that never expects to be instantiated
# Ex. Animal


#### Object Oriented 3 Principles ####
###################
## Encapsulation ##
###################
# Access restriction - preventing one object from accessing another's internal state, for example.
# Namespaces/scopes - allowing the same name to have different meanings in different contexts.

#################
## Inheritance ##
#################
# Ex. Dog and Cat inheritates Animal

##################
## Polymorphism ##
##################
# Each subclass implemnts its own method with the same name
# Ex. speak(), move()

class Circle():

    # CLASS OBJECT ATTRIBUTE
    PI = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.PI

    def get_circumference(self):
        return self.radius * 2 * self.PI


class Animal():
	def __init__(self, name):
		self.name = name
		print('Im Animal!!')
	def speak(self):
		raise NotImplementedError("speak must be implement!!")
	def move(self):
		print('Animal moves')


class Dog(Animal):
	def speak(self):
		return self.name + " woof!"
	def move(self):
		super().move()
		print('Dog moves')

class Cat(Animal):
	def speak(self):
		return self.name + " meow!"
	def move(self):
		super().move()
		print('Dog moves')


class Book():
	
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
	
	def __str__(self):
		return f"{self.title} by {self.author}"

	def __len__(self):
		return self.pages

	def __del__(self):
		print(f'{self.title} has been deleted')

if __name__ == '__main__':

    print('=================')
    print('== Basic Class ==')
    print('=================')

    c = Circle(30)
    circum = c.get_circumference()

    print("circum = {}".format(circum))
    print(c.radius)
    print(c.area)


    print('===========================')
    print('== Inheritance of Class ==')
    print('===========================')

    my_dog = Dog("MayMay")
    print(my_dog.speak())
    my_dog.move()

    my_cat = Cat("MeowMeow")
    print(my_cat.speak())
    my_cat.move()


    print('=============================')
    print('== Magic Method with Class ==')
    print('=============================')

    b = Book('Python rocks', 'Jose', 200)

    print(b)          
    print(str(b))
    print(len(b))
    del b # Free the memory
