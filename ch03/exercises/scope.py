# If you get stuck or confused, send me a link to your REPL on Discord with your question

# I prewrote some of the code in this one to help you get started. You only need to complete the code inside the 3 functions

# Make sure you understand everything that is happening in the code.

def multiply(a = 0, b = 0):
    """
        multiplies two positive integers together using only a for loop and addition
    Args:
        a (int, optional): Defaults to 0.
        b (int, optional): Defaults to 0.
    Return:
        (int) result of operation
    """

def exponent(a = 0, b = 0):
     """
        raises positive integer a to exponent b using only a for loop and multiplication
    Args:
        a (int, optional): Defaults to 0.
        b (int, optional): Defaults to 0.
    Return:
        (int) result of operation
    """


def square(a = 0):
     """
        This should be a one line function. It should make a call to multiply(), and return the result from that.
    Args:
        a (int, optional): Defaults to 0.
        b (int, optional): Defaults to 0.
    Return:
        (int) result of operation
    """


def main():

    num_a = int(input("Please enter number A to multiply:"))
    num_b = int(input("Please enter number B to multiply:"))
    result = multiply(num_a, num_b)
    print(result)
    
    num = int(input("Please enter number to raise:"))
    exp = int(input("Please enter an exponent:"))
    result = exponent(num, exp)
    print(result)

    num = int(input("Please enter a number to square:"))
    result = square(num)
    print(result)

main()