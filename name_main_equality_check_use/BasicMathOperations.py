
class MathOperations:

    @staticmethod
    def add_op(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2


if __name__ == "__main__":
    print("3 + 5 = {}".format(MathOperations.add_op(3, 5)))
    print("5 - 3 = {}".format(MathOperations.subtract(5, 3)))
