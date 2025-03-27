import inspect
import re

# *********************************************************
# *********** THIS FILE IS FOR FACULTY USE ONLY ***********
# *********************************************************
def run_a_test(func, expected_result, *args):
    actual_result = func(*args)
    assert actual_result == expected_result


def is_elif_present(func):
    loop_found = False
    for line in inspect.getsourcelines(func)[0]:
        if re.match(r'elif.*:', line.strip()):
            loop_found = True
            break
    return loop_found


def is_else_present(func):
    loop_found = False
    for line in inspect.getsourcelines(func)[0]:
        if re.match(r'elif.*:', line.strip()):
            loop_found = True
            break
    return loop_found


def is_loop_present(func):
    loop_found = False
    for line in inspect.getsourcelines(func)[0]:
        if re.match(r'for.*:', line.strip()):
            loop_found = True
            break
        if re.match(r'while.*:', line.strip()):
            loop_found = True
            break
    return loop_found


def is_in_present(func):
    in_found = False
    for line in inspect.getsourcelines(func)[0]:
        if re.match(r'in.*:', line.strip()):
            in_found = True
            break
    return in_found


def is_ifin_present(func):
    in_found = False
    for line in inspect.getsourcelines(func)[0]:
        if re.match(r'if.*in.*:', line.strip()):
            in_found = True
            break
    return in_found

