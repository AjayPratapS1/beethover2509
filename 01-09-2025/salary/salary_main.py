#from salary_manager import create_salary, read_all, read_by_salary,delete_by_salary,salaries,update
import salary_manager
def menu():
    message = '''
1 - Create Salary
2 - Read All Salary
3 - Read By Salary
4 - Update
5 - Delete
6 - Exit/ Logout
'''
    choice = int(input(message))
    if choice ==1:
        salary = int(input('Salary: '))
        salary_manager.create_salary(salary)
    elif choice == 2:
        result_salaries = salary_manager.read_all()
        print('Salaries')
        for salary in result_salaries:
            print(salary)
    elif choice == 3:
        salary = int(input('Search Salary: '))
        index = salary_manager.read_by_salary(salary)
        if salary == -1:
            print('Salary not found')
        else:
            print(f'Salary is at index,{index}')
    elif choice == 4:
        old_salary = int(input('Salary to update:'))
        new_salary = int(input('New Salary: '))
        salary_manager.update(old_salary,new_salary)
    elif choice == 5:
        old_salary = int(input('Salary to Delete: '))
        salary_manager.delete_by_salary(old_salary)
    return choice
def menus():
    print("Salary Management App")
    choice = menu()
    while choice !=6:
        choice = menu()
    print('Thank you for using app')

menus()
'''

#Creating Salary
salary_manager.create_salary(2000)
salary_manager.create_salary(3000)
salary_manager.create_salary(4000)
print("Create Employee Salaries: ", salary_manager.salaries)

#Read All salary
result_salaries = salary_manager.read_all()
print("Current Salaries")
for salary in result_salaries: 
    print(salary)

#Reading by salary
print(salary_manager.read_by_salary(3000))
print(salary_manager.read_by_salary(10000))
print(salary_manager.salaries[salary_manager.read_by_salary(4000)])

#Update salary
salary_manager.update(2000,5000)
print("Update Salaries", salary_manager.read_all())

#delete Salary
salary_manager.delete_by_salary(4000)
print(salary_manager.read_all())
'''