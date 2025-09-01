#from salary_manager import create_salary, read_all, read_by_salary,delete_by_salary,salaries,update
import salary_manager
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