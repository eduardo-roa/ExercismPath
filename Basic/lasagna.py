import Exercism.Basic.lasagna as lasagna
lasagna.EXPECTED_BAKE_TIME = 40

elapsed_time = 30


def bake_time_remaining(elapsed_time):
    """
    Calculate bake_time_remaining
    :param elapsed_time: int - baking time already elapsed minus .
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    result = lasagna.EXPECTED_BAKE_TIME - elapsed_time
    return result

bake_time_remaining(elapsed_time)

def preparation_time_in_minutes(layers):
    """
    Calculate preparation_time_in_minutes
    :param layers: int - number of layers that we use in the lasagna
    :return: int - time (in minutes) that each layer take to cook, each layer cook in 2 minutes
    """
    result = layers * 2
    return result

preparation_time_in_minutes(2)


def elapsed_time_in_minutes(layers,elapsed_time):
    """Calculate the elapsed cooking time.

    :param layers: int - the number of layers in the lasagna.
    :param elapsed_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    total_time_elapse = preparation_time_in_minutes(layers) + elapsed_time
    return total_time_elapse
    
elapsed_time_in_minutes(2,elapsed_time)