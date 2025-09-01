salaries = []
# salaries = list() (constructor)
# append method is use to add new element in list
salaries.append(1000)
salaries.append(2000)
salaries.append(3000)
# print salaries
print(salaries)
print(salaries[2])
# dir(salaries) dir for fetching the all funcion of list or salaries list
dir(salaries)
# remove to the back
salaries.pop()
print(salaries)
# remove method
salaries.remove(1000)
print(salaries)
salaries.append(5000)
salaries.append(6000)
salaries.append(9000)
print(salaries)

# Search Salary
search = 5000
index = -1
I = 0
for salary in salaries:
    if salary == search:
        index = I
        break
    I+= 1

print("Index of the salary: ",index)

class Employee:
    def __init__(self,id,name,role,salary,bonus):
          self.id = id
          self.name = name
          self.role = role
          self.salary = salary
          self.bonus = bonus
  
        
    def __repr__(self):
         return f'id = {self.id},name = {self.name}, role= {self.role}, salary = {self.salary}, bonus= {self.bonus}'
    
    def __str__(self):
         return self.__str__()
         
ajay = ('101','ajay','software engineer',50000,400)
print(ajay)

jai = ('102','jai','software engineer',5000,200)
print(jai)
employee = [ajay,jai]
print(employee)      

ajay_set = {10,20,10,30}
ajay_dist = {101:"ajay",102:"jai"}
ajay_list = ["ajay","jai"]
ajay_tuple = (10,"ajay",20.5)
print(type(ajay_tuple))