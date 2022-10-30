food_dict = {}
food1 = input("Enter a food you like: ")
food_dict[1] = food1
food2 = input("Enter another food you like: ")
food_dict[2] = food2
food3 = input("Enter one last food you like: ")
food_dict[3] = food3
print(food_dict)
dislike = int(input("Which of these do you want to get rid of? "))
del food_dict[dislike]
print(sorted(food_dict.values()))