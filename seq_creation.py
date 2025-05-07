import random

# random.seed(10)

alphabet = ('A','C','G','T')

pattern1 = 'ATTAGA'
pattern2 = 'ACGCATTT'
pattern3 = 'AGGACTCAA'
pattern4 = 'ATTTCAGT'

def select_rand_elem(amount, lst):
    selected = []
    for _ in range(amount):
        selected.append(random.choice(lst))

    return selected
    

def select_rand_pos(amount, lst):
    if amount != 0:
        positions = random.sample(range(0, len(lst)), amount)
        return positions
    else:
        positions = []
        return positions
    

def replace_symbols(pattern):
    pattern_copy = '%s' % pattern
    pattern_copy = list(pattern_copy)

    amount_2 = random.randint(0,2)
    positions = select_rand_pos(amount_2, pattern_copy)
    
    if not positions:
        return "".join(str(item) for item in pattern_copy)
    else:
        for x in positions:
            ab_with_null = ['A','C','G','T','']
            ab_with_null.remove( pattern_copy[x] )
            pattern_copy[x] = random.choice(ab_with_null)

        pattern_copy = "".join(str(item) for item in pattern_copy if item != '')
        return pattern
        


def create_string():

    amount_1 = random.randint(1,3)
    new_string = "".join(str(c) for c in select_rand_elem(amount_1, alphabet))

    new_p_1 = replace_symbols(pattern1)
    new_p_2 = replace_symbols(pattern2)
    new_p_3 = replace_symbols(pattern3)
    new_p_4 = replace_symbols(pattern4)

    new_string += new_p_1+new_p_2+new_p_3+new_p_4 

    amount_3 = random.randint(1,2)
    selected_2 = "".join(str(c) for c in select_rand_elem(amount_3, alphabet))
    new_string += selected_2

    return new_string
    
strings_100 = []

for x in range(100):
    strings_100.append(create_string())

random.shuffle(strings_100)

datasetA = strings_100[:10]
datasetB = strings_100[10:80]
datasetC = strings_100[80:]    

with open("Auxiliary2025/datasetA.txt", "w") as file:
    for seq in datasetA:
        file.write(f"{seq}\n")

with open("Auxiliary2025/datasetB.txt", "w") as file:
    for seq in datasetB:
        file.write(f"{seq}\n")

with open("Auxiliary2025/datasetC.txt", "w") as file:
    for seq in datasetC:
        file.write(f"{seq}\n")