list_length = int(input())
counter = 0

my_list = []
while counter < list_length:
    my_list.append(int(input()))
    counter += 1

#my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

aux_list = []
counter = 0

while counter < len(my_list):
    if my_list[counter] in aux_list:
        del my_list[counter]
    else:
        aux_list.append(my_list[counter])
        counter += 1

print(my_list)