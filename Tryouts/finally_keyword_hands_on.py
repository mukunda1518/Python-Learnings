# https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python

def hands_on_finally():
    try:
        return 3
    finally:
        return 4  # The finally block is run before the method returns


def finally_():
    try:
        var1 = "tutorials"
        print(var1)
        print(var2)
    except NameError:
        print("variable is not found in local")
    finally:
        print("Finally block code here")


if __name__ == "__main__":
    print(hands_on_finally())
    finally_()

