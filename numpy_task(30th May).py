import numpy as np
arr = np.arange(20).reshape(4,5)
print(arr)
print("\n")

even = np.arange(20,71,2)
print(even)
print("\n")

odd = np.arange(21,72,2)
print(odd)
print("\n")

random_dig = np.random.randint(0,101,15)
print(random_dig)
print(np.sort(random_dig))
print("\n")

zero_array = np.array([0]*10)
zero_array[4]=1
print(zero_array)
print("\n")

arr = [1,2,2,3,4,4,5]
unique_element = np.unique(arr)
print(unique_element)
print("\n")

arr = np.arange(0,11)
reverse_array = np.flip(arr)
print(reverse_array)
print("\n")

birds = ['spoonbills', 'plovers', 'plovers', 'plovers', 'plovers', 'cranes', 'plovers', 'plovers', 'cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
print("\n")

birds_arr = np.array(birds)
age_arr = np.array(age)
print("\n")

crane_ages = age_arr[birds_arr == 'cranes']
mean_age = round(np.mean(crane_ages), 2)
print(mean_age)
print("\n")

oldest_bird = np.array(birds)[np.array(age) == np.max(age)]
print(oldest_bird)
print("\n")

original = np.arange(60).reshape(6,10)
print(original)
subarray = original[1:4, -3:][::-1]
print(subarray)
print("\n")


