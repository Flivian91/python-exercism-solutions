"""
Functions used in preparing Guido's gorgeous lasagna.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """
    Calculates the bake time remaining
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calculates the preparation time in minutes
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total elapsed cooking time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

print(elapsed_time_in_minutes(3, 20))