#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0)
    ars = 0
    itel = 0
    while ars < x:
        try:
            print("{:d}".format(my_list[ars]), end="")
            itel += 1
        except IndexError:
            raise
        except:
            pass
        ars += 1
    print("")
    return itel
