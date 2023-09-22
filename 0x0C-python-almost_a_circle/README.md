## 0x0C. Python - Almost a circle

#### General:
*   what is Unit testing and how to implement it in a large project.
*   How to serialize and deserialize a class
*   How to write and read a JSON file
*   What is *args and how use it
*   What is **kwargs and how to use it
*   How to handle named arguments in a function


#### Tasks:

##### 0. If it's not tested it doesn't work
    All your files, classes and methods must be unit tested and be PEP 8
    validated.


##### 1. Base class
    Write the first class Base:
    Create a folder named 'models' with an empty file __init__.py inside - with
    this file, the folder will become a Python package.
    Create a file named 'models/base.py:
       class Base:
            private class attribute __nb_objects = 0
            class constructor: def __init__(self, id=None):
                if id is not None, assign the public instance attribute id with
                this argument value-you can assume id is an integer and you
                don't need to test the type of it
                Otherwise, increment __nb_objects and assign the new value to the public instance attribute id    
    This class will be the "base" of all other classes in this project. The goal
    of it is to manage id attribute in all your future classes and to avoid
    duplicating the same code (by extension, same bugs)


##### 2. First Rectangle
    Write the class "Rectangle" that inherits from Base:

        1. In the file "models/rectangle.py"
        2. Rectangle inherits from Base
        3. Private instance attributes, each with its own public getter and setter:
            . __width -> width
            . __height -> height
            . __y -> y
        4. class constructor: "def __init__(self, width, height, x=0, y=0,
            id=None)":
            . Call the super class with id - this super call with use the
                logic of the __init__ of the Base class
            . Assign each argument width, height, x and y to the right
                attribute

    Why private attributes with getter/setter? Why not directly public attribute?

    Because we want to protect attributes of our class. With a setter, you are
        able to validate wha a developer is trying to assign to a variable. So
        after, in your class you can 'trust' these attributes.


##### 3. Validate attributes
    Update the class Rectangle by adding validation of all setter methods and
        instantiation(id excluded):
        1. If the input is not an integer, raise the TypeError exception with
            the message: <name of the attribute> must be an integer.
        2.  If width or height is under or equals 0, raise the ValueError
             exception with the message: <name of the attribute> must be > 0.
        3. If x or y under 0, raise the valueError exception with the message:
             <name of the attribute must be >= 0


##### 4. Area first
    Update the class Rectangle by adding the public method def area(self):
         that reutrns the area value of the Rectangle instance.


##### 5. Display #0
    Update the class Rectangle by adding the public method def display(self):
        that prints in stdout the Rectangle instance with the character # you
           you don't need to handle x and y here



