name = input("Введите Ваше имя: ")
current_year = 2024
year_of_birth = int(input("В каком году Вы родились? "))
text_for_answer = " лет", " год", " года", " года", " года", " лет", " лет", " лет", " лет", " лет"
age = current_year - year_of_birth
age_help = age % 10
if 10 < age < 15 : age_help = 0
print("Здравствуйте, ", name, "!")
if age < 5 : print("Хорошая шутка")
if age >4 : print("В этом году Вам ", age, text_for_answer[age_help])
