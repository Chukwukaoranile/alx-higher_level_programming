#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    conta = 0
    tell = 0
    while conta < x:
        try:
            print("{:d}".format(my_list[conta]), end="")
            tell += 1
        except IndexError:
            raise
        except:
            pass
        conta += 1
    print("")
    return tell
