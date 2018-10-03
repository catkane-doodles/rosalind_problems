A = "dominant"
B = "recessive"

k = [A, A]
n = [B, B]
m = [A, B]

population_list = [k, k, m, m, n, n]

calculated_offspring_count = 0
dominant_count = 0


def calculate_offspring(subject1, subject2):
    for x in subject1:
        for y in subject2:
            global calculated_offspring_count
            global dominant_count
            calculated_offspring_count += 1
            if A in x + y:
                dominant_count += 1


def probability_counter():
    number_of_runs = len(population_list)
    for x in range(0, number_of_runs):
        altered_population = population_list[:]
        lucky_guy = altered_population.pop(x)
        for lucky_girl in altered_population:
            calculate_offspring(lucky_guy, lucky_girl)
    print(dominant_count/calculated_offspring_count)


probability_counter()