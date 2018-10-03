# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT


id_number = []
id_string = []
gc_percentage = []


def entering_of_data():
    def calculation_of_gc(gc_string):
        gc_counter = 0
        for x in gc_string:
            if x.upper() == "G":
                gc_counter = gc_counter + 1
            elif x.upper() == "C":
                gc_counter = gc_counter + 1
            else:
                pass
        gc_length = len(gc_string)
        gc_content = gc_counter / gc_length * 100
        gc_percentage.append(gc_content)

    def result():
        for x in gc_percentage:
            if x == max(gc_percentage):
                y = gc_percentage.index(x)
                print("Rosalind_" + str(id_number[y])
                      + "\n" + str(x))
    i = 0
    while True:
        i += 1
        id_number_input = input("Please key in ID Number %d: " %i)
        if id_number_input == "":
            break
        else:
            id_string_input = input("Please key in ID String %d: " %i)
            id_number.append(id_number_input)
            id_string.append(id_string_input)
            calculation_of_gc(id_string_input)
    result()


entering_of_data()