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

    This class should have one method:
    - To read input from from the keyboard, convert it to integer and return it
    """


class TextFileInputReader:
    """
    This class inherits InputReader
    and makes reading an integer from a text file.

    This class should have one attributes:
    - file_location (String): The location of the input file.

    This class should have one method:
    - To read input from the given file location, convert it to integer and return it

    """


class Calculator:
    """
    One method named: tribonacci
    - one parameter: n
    - one returned value: tribonacci of n using the recursive process
    """


class CalculatorBis:
    """
    One method named: tribonacci
    - one parameter: n
    - one returned value: tribonacci of n using the iterative process
    """


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


def main34():
    app1 = CalculatorApp(StdInputReader(), Calculator())
    print(app1.calculate())

    app2 = CalculatorApp(TextFileInputReader("./input.txt"), CalculatorBis())
    print(app2.calculate())


if __name__ == "__main__":
    main()
