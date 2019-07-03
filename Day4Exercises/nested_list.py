import copy

nested_list = [ [ [2, 3, 45], 1, 2, 3] ] #lista zagnieżdżona
new_list = copy.deepcopy(nested_list) #copy.deepcopy() jest zainportowane z biblioteki "import copy"

nested_list[0][0][1] = 36

print(nested_list)
print(new_list)
