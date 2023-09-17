## 0x0A - Python Inheritance.

#### General
	* Why Python programming is awesome
	* What is a superclass, baseclass or parentclass
	* What is a subclass
	* How to list all attributes and methods of a class or instance
	* When can an instance have new attributes
	* How to inherit class from another
	* How to define a class with multiple base classes
	* What is the default class every class inherit from
	* How to override a method or attribute inherited from the base class
	* Which attributes or methods are available by heritage to subclasses
	* What is the purpose of inheritance
	* What are, when and how to use isinstance, issubclass, type and super built-in functions

#### Tasks:

##### 0. Lookup

	Write a function that returns the list of available attributes and method
	of an object;
		Prototype: def lookup(obj):
		Returns a list object
		You are not allowed to import any module

##### 1. My list
	Write a class MyList that inherits from list:
		Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
		You can assume that all the elements of the list will be of type int
		You are not allowed to import any module

##### 2. Exact same object
	Write a function that returns "True" if the object is exactly an instance
	of the specific class: Otherwise False.
		Prototype: def is_same_class(obj, a_class):
		You are not allowed to import any module

##### 3. Same class or inherit from
	Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
		Prototype: def is_kind_of_class(obj, a_class):
		You are not allowed to import any module

##### 4. Only sub class of
