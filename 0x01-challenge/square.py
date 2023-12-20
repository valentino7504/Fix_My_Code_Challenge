#!/usr/bin/python3
"""

This is a module used to define a square


"""
class Square():
    """
    A square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Init method for square class
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """
        returns the perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        this is how the square will be printed
        """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
