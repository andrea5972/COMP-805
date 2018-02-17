"""
lab3.py
Andrea Murphy
COMP-805
2/17/2018
doctests
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: listof these numbers squared

    >>> squared_nums([1, 2, 3])
    [1, 4, 9]

    >>> squared_nums([])
    []

    >>> squared_nums ([-1, -2])
    [1, 4]
    """
    new_list = [ ]
    for num in num_list:


        # num **2
        sq_num =pow(num, 2)
        new_list.append(sq_num)

    return new_list


def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles

    >>> check_title(['Hello World', 'Hello_world','Title'])
    ['Title']

    >>> check_title(['Hello_World', 'A great 3 Days' 'hello World'])
    []

    >>> check_title(['10,11,12'])
    []
    """
    new_list= [ ]
    for title in title_list:
        if title.istitle() and title.isalpha():
                new_list.append(title)

    return new_list


def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Retuns: updated dictionay where each item is restocked

    >>> restock_inventory({'pencil':10, 'pen':8, 'paper':7})
    {'pencil': 20, 'pen': 18, 'paper': 17}

    >>> restock_inventory({'pencil':0, 'pen':-3, 'paper':0.0})
    {'pencil': 10, 'pen': 7, 'paper': 10.0}

    >>> restock_inventory({'pencil':0.5, 'pen':-3.2, 'paper':11.0})
    {'pencil': 10.5, 'pen': 6.8, 'paper': 21.0}
    """
    new_inventory = { }
    for key, val in inventory.items():
        val = val +10
        new_inventory[key] =val

    return new_inventory


def filter_0_items(inventory):
    """
    Removes: item that have a vaule of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: string that is the name of the inventory item
        value: integers that equals the number of that item currently on hand
    Returns: the same inventory_dic with any item that had quantity removed

    >>> filter_0_items({'pencil':10, 'pen':8, 'paper':7})
    {'pencil': 10, 'pen': 8, 'paper': 7}

    >>> filter_0_items({'pencil':0, 'pen':-3, 'paper':-11})
    {'pen': -3, 'paper': -11}

    >>> filter_0_items({'pencil':0.5, 'pen':-3.2, 'paper':11.0})
    {'pencil': 0.5, 'pen': -3.2, 'paper': 11.0}

    """
    new_inventory = [ ]

    for item in inventory:
        if inventory[item] ==0:
            new_inventory.append(item)

    for keys in new_inventory:
        del inventory[keys]

    return inventory


def average_grades(grades):
    """
    Takess grade values from a dictionary and averages them into a final grade
    grade: a dictionary with of grades with:
        key: string of student names
        value: list of integers grades receieved in class
    Returns: dictionary that averages out the grades of each student

    >>> average_grades({'Michael':[100,78,88,900/10], 'Daniel':[80,95,77,64.0] , 'Josh':[99,89,94,66]})
    {'Michael': 89.0, 'Daniel': 79.0, 'Josh': 87.0}

    >>> average_grades({'Michael':[5*20,188*.5,88], 'Daniel':[80.5,.15,66,64.0] , 'Josh':[99,+1* -2,40/.5]})
    {'Michael': 94.0, 'Daniel': 52.6625, 'Josh': 59.0}

    >>> average_grades({'Michael':[78], 'Daniel':[90] , 'Josh':[900/-9]})
    {'Michael': 78.0, 'Daniel': 90.0, 'Josh': -100.0}
    """
    grades_mean = { }
    for key, value in grades.items():
        grades_mean[ key] = sum(value)/ len(value)

    return grades_mean


if __name__ == '__main__':
    import doctest
    doctest.testmod( )













