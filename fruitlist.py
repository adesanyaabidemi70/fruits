print('hi there,what may i help you with')
user_fruit = input('enter the fruit')
fruits_lists = ['orange', 'apple', 'orange','pineapple','cherry','coconut','kiwi']

new_fruits = set(fruits_lists)

# fruits_lists = ['orange', 'apple', 'orange','pineapple','cherry','coconut','kiwi', user_fruit]
fruits_lists.append(user_fruit)

fruit = "orange"

if fruit in fruits_lists:
    print(f"{fruit} found!")

print(fruits_lists)

print(new_fruits)

original_fruits = list(new_fruits)

print(original_fruits)

first_three_fruits = fruits_lists[0:3]

last_fruit = fruits_lists[-1::-1]

print(fruits_lists[-3])

print(f"The last fruit on the list is {last_fruit}")

print(first_three_fruits)



