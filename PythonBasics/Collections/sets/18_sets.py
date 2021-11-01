# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}
#
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# dishes.update(utensils)                  #combine utensils+dishes in dishes set
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))        # print what dishes has but utensils does not
# print(utensils.intersection(dishes))

for x in utensils:
    print(x)
