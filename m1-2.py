# Практическое задание по работе в Pycharm - "Переменные".
quantity_of_homeworks = 12
quantity_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = quantity_of_hours_spent / quantity_of_homeworks
final_str = ('Курс: ' + course_name + ', всего задач: '
             + str(quantity_of_homeworks) + ', затрачено часов:' + str(quantity_of_hours_spent))
print(final_str, ', среднее время выполнения ', time_for_one_task, ' часа.')
