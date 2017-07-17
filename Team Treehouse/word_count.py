# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(some_string):
    my_dict = {}
    new_string = some_string.lower().split()
    for word in new_string:
        if word in my_dict:
            my_dict[word] += 1
        else: 
            my_dict[word] = 1
    return my_dict