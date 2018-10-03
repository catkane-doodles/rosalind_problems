# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT


def hamming_dist_calculator():
    distance_counter = 0
    var1 = input("Please key in the first DNA string: ")
    var2 = input("Please key in the second DNA string: ")

    for x, y in zip(var1, var2):
        if x != y:
            distance_counter = distance_counter + 1
        else:
            pass

    print("The Hamming Distance is: %s" %distance_counter)

hamming_dist_calculator()