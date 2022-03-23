# Function should throw an IndexError exception

random_list = [1, 2, 3]


def out_of_range_index(list):
    return list[4]

# result = out_of_range_index(random_list)
# print(result)