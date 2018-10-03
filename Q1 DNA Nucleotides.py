data_set = [x for x in "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"]

for x in data_set:
    count_a = [x for x in data_set if x == "A"]
    count_c = [x for x in data_set if x == "C"]
    count_g = [x for x in data_set if x == "G"]
    count_t = [x for x in data_set if x == "T"]


count_a = str(len(count_a))
count_c = str(len(count_c))
count_g = str(len(count_g))
count_t = str(len(count_t))

print("A shows up " + count_a + " number of times")
print("C shows up " + count_c + " number of times")
print("G shows up " + count_g + " number of times")
print("T shows up " + count_t + " number of times")