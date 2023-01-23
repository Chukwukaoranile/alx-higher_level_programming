#!/usr/bin/python3
def safe_print_division(num1, num2):
    try:
        cac = num1 / num2
        return (cac)
    except ZeroDivisionError:
        cac = None
    except:
        pass
    finally:
        print("Inside result: {}".format(cac))
