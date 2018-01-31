"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to test the functions declared in
lab1.py. This file does not use pythons unit test framework.
This is because this file is intended to by used as a learning
tool as well.

Please see: https://docs.python.org/3/library/unittest.html for information
    on pythons unit testing framework.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def test_failed(results_dict):
    """
    Increments global variables tests_ran and tests_failed
    """
    results_dict['tests_ran'] += 1
    results_dict['tests_failed'] += 1

def test_passed(results_dict):
    """
    Increments global variables tests_ran and tests_passed
    """
    results_dict['tests_ran'] += 1
    results_dict['tests_passed'] += 1

def test_give_me_a_string(results_dict):
    """
    Checks that lab1.give_me_a_string() returns a string type
    """
    print("")
    print("Testing lab1.give_me_a_string()")
    message = "----"
    try:
        result = lab1.give_me_a_string()
        if not isinstance(result, str):
            message += 'Did not return a string - Fail'
            test_failed(results_dict)
        else:
            message += 'A string was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_string function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_an_integer(results_dict):
    """
    Checks that lab1.give_me_an_integer() returns an integer type
    """
    print("")
    print("Testing lab1.give_me_an_integer()")
    message = "----"
    try:
        result = lab1.give_me_an_integer()
        if not isinstance(result, int):
            message += 'Did not return an integer - Fail'
            test_failed(results_dict)
        else:
            message += 'An integer was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_an_integer function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_a_boolean(results_dict):
    """
    Checks that lab1.give_me_a_boolean() returns a booeal type
    """
    print("")
    print("Testing lab1.give_me_a_boolean()")
    message = "----"
    try:
        result = lab1.give_me_a_boolean()
        if not isinstance(result, bool):
            message += 'Did not return a boolean - Fail'
            test_failed(results_dict)
        else:
            message += 'A boolean was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_boolean function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_a_float(results_dict):
    """
    Checks that lab1.give_me_a_boolean() returns a boolean type
    """
    print("")
    print("Testing lab1.give_me_a_float()")
    message = "----"
    try:
        result = lab1.give_me_a_float()
        if not isinstance(result, float):
            message += 'Did not return a float - Fail'
            test_failed(results_dict)
        else:
            message += 'A float was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_float function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_a_list(results_dict):
    """
    Checks that lab1.give_me_a_list() returns a list type
    """
    print("")
    print("Testing lab1.give_me_a_list()")
    message = "----"
    try:
        result = lab1.give_me_a_list()
        if not isinstance(result, list):
            message += 'Did not return a list - Fail'
            test_failed(results_dict)
        else:
            message += 'A list was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_list function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_a_dictionary(results_dict):
    """
    Checks that lab1.give_me_a_dictionary() returns a dictionary type
    """
    print("")
    print("Testing lab1.give_me_a_dictionary()")
    message = "----"
    try:
        result = lab1.give_me_a_dictionary()
        if not isinstance(result, dict):
            message += 'Did not return a dictionary - Fail'
            test_failed(results_dict)
        else:
            message += 'A dictionary was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_dictionary function - Fail'
        test_failed(results_dict)
    print(message)

def test_give_me_a_tuple(results_dict):
    """
    Checks that lab1.give_me_a_tuple() returns a tuple type
    """
    print("")
    print("Testing lab1.give_me_a_tuple()")
    message = "----"
    try:
        result = lab1.give_me_a_tuple()
        if not isinstance(result, tuple):
            message += 'Did not return a tuple - Fail'
            test_failed(results_dict)
        else:
            message += 'A tuple was returned - Pass'
            test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.give_me_a_tuple function - Fail'
        test_failed(results_dict)
    print(message)

def test_check_is_even(results_dict):
    """
    Checks that lab1.check_is_even() returns true for even numbers
    """
    print("")
    print("Testing lab1.check_is_even()")
    message = "----"
    try:
        result = lab1.check_is_even(2)
        if not isinstance(result, bool):
            message += 'Did not return a boolean - Fail'
            test_failed(results_dict)
        else:
            message += 'A boolean was returned - Pass'
            test_passed(results_dict)
            # now check if true
            if result is True:
                message += '\n----check_is_even(2) returns True - Pass'
                test_passed(results_dict)
            else:
                message += '\n----check_is_even(2) returns False - Fail'
                test_failed(results_dict)
            # try again, with odd number
            result = lab1.check_is_even(1)
            if result is False:
                message += '\n----check_is_even(1) returns False - Pass'
                test_passed(results_dict)
            else:
                message += '\n----check_is_even(1) returns True - Fail'
                test_failed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.check_is_even function - Fail'
        test_failed(results_dict)
    print(message)

def test_sum_numbers_one_to_ten(results_dict):
    """
    Checks that lab1.sum_numbers_one_to_ten() returns a the correct value
    """
    print("")
    print("Testing lab1.sum_numbers_one_to_ten()")
    message = "----"
    try:
        result = lab1.sum_numbers_one_to_ten()
        if not isinstance(result, int):
            message += 'Did not return an integer - Fail'
            test_failed(results_dict)
        else:
            message += 'An integer was returned - Pass'
            test_passed(results_dict)
            # now check if the value is correct, should be 55
            if result is not 55:
                message += '\n----Did not return the correct number - Fail'
                test_failed(results_dict)
            else:
                message += '\n----The correct value (55) was returned - Pass'
                test_passed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.sum_numbers_one_to_ten function - Fail'
        test_failed(results_dict)
    print(message)

def test_check_is_less_than(results_dict):
    """
    Checks that lab1.check_is_less_than(number1, number2) returns
    True if number1 is less than number2, else False
    """
    print("")
    print("Testing lab1.check_is_less_than()")
    message = "----"
    try:
        result = lab1.check_is_less_than(2, 4)
        if not isinstance(result, bool):
            message += 'Did not return a boolean - Fail'
            test_failed(results_dict)
        else:
            message += 'A boolean was returned - Pass'
            test_passed(results_dict)
            # now check if the result is true (2 is less than 4)
            if result is True:
                message += '\n---- 2 is less than 4, True - Pass'
                test_passed(results_dict)
            else:
                message += '\n---- 2 is less than 4, False - Fail'
                test_failed(results_dict)
            # try again, with number1 > number2
            result = lab1.check_is_less_than(6, 4)
            if result is False:
                message += '\n---- 6 is less than 4, False - Pass'
                test_passed(results_dict)
            else:
                message += '\n---- 6 is less than 4, True - Fail'
                test_failed(results_dict)
    except AttributeError:
        message += 'Could not find lab1.check_is_less_than function - Fail'
        test_failed(results_dict)
    print(message)

def run():
    """
    This function is the test runner. It calls the functions
    declared in this file that are used to test the functions
    declared in lab1.py
    """
    results_dict = {
                    'tests_ran': 0,
                    'tests_passed': 0,
                    'tests_failed': 0,
                    }

    test_give_me_a_string(results_dict)
    test_give_me_an_integer(results_dict)
    test_give_me_a_boolean(results_dict)
    test_give_me_a_float(results_dict)
    test_give_me_a_list(results_dict)
    test_give_me_a_dictionary(results_dict)
    test_give_me_a_tuple(results_dict)
    test_sum_numbers_one_to_ten(results_dict)
    test_check_is_even(results_dict)
    test_check_is_less_than(results_dict)

    print("")
    print("Final Results:")
    results = "%s tests ran: %s passed - %s failed." % (
                                                        results_dict['tests_ran'],
                                                        results_dict['tests_passed'],
                                                        results_dict['tests_failed']
                                                        )
    print(results)
    if results_dict['tests_ran'] == results_dict['tests_passed']:
        print('GOOD JOB! ALL TESTS PASSED!')
    else:
        print('Please correct your errors and run again')


if __name__ == "__main__":
    try:
        import lab1
        print("Found your lab1.py file. Running tests...")
    except ImportError:
        print("Could not import lab1.py. Please make sure both files are"
            " in the same directory")
        exit()
    run()
