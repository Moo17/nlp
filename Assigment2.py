

print("----------------------- First Solution-------------------")

array = {"m":"90", "c":"50"}
print(array)
array2 = {"m":"9000", "c":"5000"}
array.update(array2)
print(array)

print("----------------------- Second Solution-------------------")

array = {"m":"90", "c":"50"}
print(array)
array.update({"m":"9000", "c":"5000"})
print(array)

