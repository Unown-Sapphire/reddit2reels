number_list = []
for i in range(1, 581):
    number_list.append(i)

a = 3
while a <= len(number_list):
    number_list.insert(a, "\n")
    a+=4

print(number_list)