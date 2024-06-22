# 1 m1-hw6.py Словари и множества

# 2 Работа со словарями

my_dict = {"Sasha": 2000, "Masha": 2001, "Katty": 2002}
print(my_dict)
print(my_dict["Masha"])
print(my_dict.get("Vikky"))
my_dict["Nick"] = 2003
my_dict.update({"Bob": 1955})
print(my_dict)
print(my_dict.pop("Sasha"))
print(my_dict)

# 3 Работа с множествами

my_set = {"Sasha", 1975, "Masha", 1999, "Katty", 2002}
print(my_set)
my_set.update(["Katty", "Nick", "Bob", 1565])
print(my_set)
my_set.discard("Sasha")
print(my_set)
my_set.discard("Sasha")
