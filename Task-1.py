my_list = [59,63,96,75,25]
print(my_list)
my_list.append(47)
my_list.remove(59)
my_list.insert(5,"Ritik")
print(my_list)

my_dict = {
    "name" : "Ritik",
    "age" : 20,
    "subject" : ["maths","physics","chemistry"],
    "language" :"python"
}
print(my_dict)
my_dict.update({"presentage" : 89.5})
print(my_dict)
print(my_dict.values())
print(my_dict.keys())

sets = {56,95,"ritik","student"}
print(sets)
print(sets.add("maths"))
print(sets.remove(56))

set2 = {95,"ritik",100}
print(sets.intersection(set2))