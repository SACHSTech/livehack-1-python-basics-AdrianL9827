print("***Chicken Distributor***")
Chicken = int(input("Enter the number of chickens: "))
Students = int(input("Enter the number of students: "))
Chicken_student = Chicken//Students
Remaining_chicken = Chicken%Students
print("Every student gets " + str(Chicken_student) + " and Mr Fabroa gets " + str(Remaining_chicken))