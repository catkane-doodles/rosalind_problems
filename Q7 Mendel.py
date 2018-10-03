population = ['k', 'm', 'n', 'k', 'm', 'n']

kk = 1
kn = 1
km = 1
mm = 0.75
mn = 0.5
nn = 0


def probability_counter():
    kk_counter = 0
    kn_counter = 0
    km_counter = 0
    mm_counter = 0
    mn_counter = 0
    nn_counter = 0

    picked_counts = 0
    number = len(population)
    i = -1
    while number > 0:
        number -= 1
        i += 1
        altered_population = population[:]
        lucky_person = altered_population.pop(number)
        for x in altered_population:
            picked_counts += 1
            sorted_couple = "".join(sorted(lucky_person + x))
            if sorted_couple == "kk":
                kk_counter += 1
            elif sorted_couple == "kn":
                kn_counter += 1
            elif sorted_couple == "km":
                km_counter += 1
            elif sorted_couple == "mm":
                mm_counter += 1
            elif sorted_couple == "mn":
                mn_counter += 1
            else:
                nn_counter +=1
    print((kk_counter*kk + kn_counter*kn + km_counter*km + mm_counter*mm + mn_counter*mn + nn_counter*nn)/picked_counts)



probability_counter()