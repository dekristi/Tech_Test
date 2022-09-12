print("I am so happy!")

ask_name = input("What is your name ? ")

user_age = input(f'{ask_name}, how old you are?')
import datetime
current_year = datetime.datetime.now().year

age = int(user_age)

hundred = int(current_year) - age + 100

print(f'{ask_name} in {hundred} you will be 100 years old!')