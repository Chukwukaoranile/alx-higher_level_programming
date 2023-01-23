#!/usr/bin/python3
def list_division(my_l_1, my_l_2, list_len):
    var = 0
    my_new_list = []
    while var < list_len:
        try:
            c = my_l_1[var] / my_l_2[var]
        except TypeError:
            c = 0
            print("wrong type")
        except IndexError:
            c = 0
            print("out of range")
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        finally:
            my_new_list.append(c)
        var = var + 1
    return my_new_list
