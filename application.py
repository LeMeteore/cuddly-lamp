import sys
from abc import ABC, abstractmethod

# Reminder Tribonacci serie

# trib(0) = 0
# trib(1) = 0
# trib(2) = 1

# trib(n) = trib(n-3) + trib(n-2) + trib(n-1) for n > 2

# n      : 0, 1, 2, 3, 4, 5, 6, 07, 08, 09, 10, 011, 012
# trib(n): 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274


class InputReader(ABC):
    """
    The abstract class of a number input reader which could be
    inherited by other classes.
    """

    @abstractmethod
    def get_input(self) -> int:
        """
        Method which reads some kind of input.
        This method should returns an integer
        """
        pass


class StdInputReader:
    """
    This class inherits InputReader.
    and makes reading an integer from the standard input.
    """

    def get_input(self) -> int:
        """
        Reads input from standard input and converts it to integer.
        """
        return int(input("Input a number: "))


class TextFileInputReader:
    """
    This class inherits InputReader
    and makes reading an integer from a text file.
    """

    def __init__(self, file_location: str):
        """
        Attributes:
        - file_location (String): The location of the input file.
        """
        self.file_location = file_location

    def get_input(self) -> int:
        """
        Reads input from the given file location and converts it to integer
        """
        f = open(self.file_location, "r")
        number = int(f.read())
        f.close()
        return number


class Calculator:
    def tribonacci(self, n):
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            res = (
                self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
            )
        return res


class CalculatorBis:
    def tribonacci(self, n):
        p3, p2, p1 = 0, 0, 1
        if n < 2:
            return 0
        elif n == 2:
            return 1
        else:
            for i in range(3, n+1):
                trib = p3 + p2 + p1
                p3 = p2
                p2 = p1
                p1 = trib
        return trib


class CalculatorApp:
    """
    2 attributes:
    - a reader of type StdInputReader, or TextFileInputReader
    - a calculator of type CalculatorIterative or CalculatorRecursive


    1 method named calculate:
    - to calculate the tribonacci of the number returned by the self.reader attribute
    - using the self.calculator attribute

    - That method shoud returns an integer
    """


def main():
    app1 = CalculatorApp(StdInputReader(), Calculator())
    app2 = CalculatorApp(TextFileInputReader("./input.txt"), CalculatorBis())

    choice = int(input("from stdin: 1 \n from file: 2 \n Everything else will stop the program and exit \n Your choice?... "))

    if choice == 1:
        print(app1.calculate())
    elif choice == 2:
        print(app2.calculate())
    else:
        sys.exit("Bye")


if __name__ == "__main__":
    main()
