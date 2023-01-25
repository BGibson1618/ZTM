def first_recurring(input_array):
    dictionary = dict()
    for item in input_array:
        if item in dictionary:
            return item
        else:
            dictionary.update({item: True})
    return None
