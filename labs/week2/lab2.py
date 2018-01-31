"""
lab2.py
Andrea Murphy
1/30/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: listof these numbers squared
    """
    new_list = []
    for num in num_list:
        sq_num =pow(num, 2) # num **2
        new_list.append(sq_num)
    return new_list
