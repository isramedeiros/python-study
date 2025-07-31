""" Define the constants of the recipe
"""

PREPARATION_TIME = 2
EXPECTED_BAKE_TIME = 40
LAYER_BAKE_TIME = 20


# tempo restante é igual ao tempo estimado menos tempo passado
def bake_time_remaining(elapsed_bake_time):
    """ Calculate the remaining time to bake the bake.

    :param elapsed_bake_time: int - time elapsed bake time.
    :return: int - the total expected bake time minus the elapsed bake time.
    """

    time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return time

# tempo de preparação é igual ao número de camadas vezes
def preparation_time_in_minutes(number_of_layers):
    """ Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time.
    """
    preparation = number_of_layers * PREPARATION_TIME

    return preparation

# tempo total passado é igual a número de camadas vezes o tempo de preparação + tempo de cozimento
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """

    elapsed = (number_of_layers * PREPARATION_TIME) + elapsed_bake_time

    return elapsed