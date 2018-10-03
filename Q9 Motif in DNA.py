print("I will help you find the position of things in strings")

dna_string = input("Please key in the string: ")
thing = input("Please key in the thing: ")

location_list = []

def locater():
    altered = dna_string
    number = 100
    while number > 0:
        number -= 1
        location = altered.find(thing)
        location_list.append(location)
        altered = altered[location:]
    print(location_list)



locater()


def locater():
    altered = dna_string
    location_list = []
    location = -1
    while True:
        location = altered.find(thing, location +1)
        if location == -1:
            break
        location_list.append(location + 1)
    print(location_list)



locater()