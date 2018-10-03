def reproduction(bunnies, reproduction_rate, duration):
    growth_chamber_even = 0
    growth_chamber_odd = 0
    adult_rabbits = 0
    i=0
    if duration % 2 == 0:
        growth_chamber_odd = growth_chamber_odd + bunnies
    else:
        growth_chamber_even = growth_chamber_even + bunnies
    duration = duration + 1
    while True:
        duration -= 1
        i += 1
        if duration == 0:
            print(total_rabbits)
            break
        elif duration % 2 == 0:
            adult_rabbits = adult_rabbits + growth_chamber_even
            growth_chamber_even = adult_rabbits * reproduction_rate
            total_rabbits = adult_rabbits + growth_chamber_odd
            # print("month %d:" % i + str(total_rabbits))
        elif duration % 2 != 0:
            adult_rabbits = adult_rabbits + growth_chamber_odd
            growth_chamber_odd = adult_rabbits * reproduction_rate
            total_rabbits = adult_rabbits + growth_chamber_even
            # print("month %d:" % i + str(total_rabbits))


reproduction(1,3,100)