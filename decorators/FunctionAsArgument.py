
def print_result_of_op(operation):
    print("Resul of operation is: {}".format(operation(2, 3)))


def op_sum(num1, num2): return num1 + num2


print_result_of_op(op_sum)
print_result_of_op(lambda num1, num2: num1 ** num2)
