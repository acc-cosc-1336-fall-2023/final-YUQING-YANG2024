#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    list = []

    for i in range(0, (len(dna_string1)-len(dna_string2) + 1)):

        if dna_string1[i : (i + len(dna_string2))] == dna_string2:
           list.append(i+1)

        i += 1

    return list