import lib

department = lib.Department(2)


department.add("John", "823193921")
department.add("Nate", "23123")
department.add("Mike", "23123")

print(department.getPeople())

print(department["John"])


# for dep in department:
#     for gg in dep:
#         print(gg)
#     break



# print(department.getPeople())3

# for i in department.getPeople():
#     print(i)