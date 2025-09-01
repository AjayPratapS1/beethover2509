salaries = []
# CURD - Create, Read All, Read by Id, Update, Delete
# Read by salary

def create_salary(salary):
    global salaries
    salaries.append(salary)

create_salary(2000)
create_salary(3000)
create_salary(4000)
print("Employee Salaries: ", salaries)

def read_all():
    return salaries


result_salaries = read_all()
print("Current Salaries")
for salary in result_salaries: 
    print(salary)

#return first occurance index
def read_by_salary(salary):# range(start) | range(start, stop) | range(start,stop,step)
    for I in range(len(salaries)):# len(salaries)= 5 I=0,1,2,3,4
        if salaries[I] == salary:
            return I
    return -1
print(salaries)
print(read_by_salary(3000))
print(read_by_salary(10000))
print(salaries[read_by_salary(4000)])

def update(old_salary,new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index] = new_salary

update(8000,5000)
print("Update Salaries", read_all())

def delete_by_salary(salary):
    global salaries
    index = read_by_salary(salary)#index of 2000 = 0
    salaries.pop(index)

delete_by_salary(2000)
print(read_all())