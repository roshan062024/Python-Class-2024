simple_set1 = {1, 2, 3}
simple_set = {1, 2, 3}
# new_set = simple_set.copy()
# print(f"{simple_set =} {id(simple_set) =}")
# print(f"{new_set    =} {id(new_set)    =}")

# simple_set.clear()
# print("\n After simple_set.clear()")
# print(f"{simple_set =} {id(simple_set) =}")
# print(f"{new_set    =} {id(new_set)    =}")


simple_set1.add("tomoto")
print(f"{simple_set1} \n")

simple_set.update("tomoto")
print(f"{simple_set}")


# Assignment
#  1. Try adding a string to both set.add & set.update &
#  observe the difference
#  'tomoto'