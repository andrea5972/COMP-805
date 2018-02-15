"""
lab2.py
Andrea Murphy
COMP-805
1/30/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: listof these numbers squared
    """
    new_list = [ ]
    for num in num_list:

        sq_num =pow(num, 2)
        new_list.append(sq_num)

    print (new_list)


def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    new_list= [ ]
    for title in title_list:
        if (title.istitle() , title.isalpha()):
                new_list.append(title)

    print (new_list)


def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item currently on hand
    Retuns: updated dictionay where each item is restocked
    """
    new_inventory = { }
    for key, val in inventory:
        val = val +10
        new_inventory[key]= val

    return new_inventory


def filter_0_items(inventory):
    """
    Removes: item that have a vaule of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: string that is the name of the inventory item
        value: integers that equals the number of that item currently on hand
    Returns: the same inventory_dic with any item that had quantity removed
    """
    results = { }
    for key, value in inventory.items():
        if key in inventory ==0:
            inventory.pop(key, None)
        else:
            inventory.update()

    return results


def average_grades(grades):
    """
    Takess grade values from a dictionary and averages them into a final grade
    grade: a dictionary with of grades with:
        key: string of student names
        value: list of integers grades receieved in class
    Returns: dictionary that averages out the grades of each student
    """
    gradesMean = { }
    for key, value in grades.items():

        grades = value
        gradesMean = float(sum(item for item in grades)) / len(grades)
        value.append(gradesMean)
        gradesMean = grades

    return gradesMean













