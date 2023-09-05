import json
from Calculations import *
from OtherFn import *


def start_project(input_type):
    if input_type == 'cli':
        f_name = input("What's your First name? ").capitalize()
        l_name = input("What's your Last name? ").capitalize()
        greeting(first_name=f_name, last_name=l_name)

        # splitting the date(which is str) according to slashes '/' :
        day, month, year = input("Please, Enter your birthday date in  dd/mm/yyyy :").split('/')
        # then converting the date (str) to int :
        day = int(day)
        month = int(month)
        year = int(year)
        date_of_birth = datetime.date(year, month, day)

        user_age = age_calculator(date_of_birth)
        print(f'Your age is {user_age}')

        height = int(input("Please, enter your Height in cm: "))
        weight = int(input("Please, enter your Weight in kg: "))
        bmi_result = body_mass_index(height, weight)
        print("Your BMI is: ", bmi_result)

        Q_of_body_type = input('Do you want to know your body type y/n: ').lower()
        body_type_sentence = body_type(bmi_result, Q_of_body_type)
        print(body_type_sentence)

        gender = input("What is your gender? ").lower()

        bmr_result = bmr_calculator(height, weight, user_age, gender)
        print("Your BMR is :", bmr_result)

    # Only INFO will be entered from the file , other questions will be entered through command lines when the program asks
    elif input_type == 'file':
        file_name = input("Enter the file name ending with .txt: ")
        info_file = open(file_name, 'r')
        user_info = info_file.readlines()   # This is a list of file inputs (str)/ list of lines
        print(user_info)
        for i in range(len(user_info)):
            user_info[i] = user_info[i].strip()
        info_file.close()

        f_name = user_info[0]
        l_name = user_info[1]
        day, month, year = user_info[2].split('/')     # splitting the date(which is str) according to slashes '/' :

        day = int(day)                                 # then converting the date (str) to int :
        month = int(month)
        year = int(year)
        height = int(user_info[3])
        weight = int(user_info[4])
        Q_of_body_type = user_info[5]
        gender = user_info[6]

        greeting(first_name=f_name, last_name=l_name)
        date_of_birth = datetime.date(year, month, day)
        user_age = age_calculator(date_of_birth)
        print(f'Your age is {user_age}')
        bmi_result = body_mass_index(height, weight)
        print("Your BMI is: ", bmi_result)
        print(Q_of_body_type)
        body_type_sentence = body_type(bmi_result, Q_of_body_type)
        print(body_type_sentence)
        bmr_result = bmr_calculator(height, weight, user_age, gender)
        print("Your BMR is :", bmr_result)

    else:
        print("You didn't enter a valid option")
        thanks_function()

    input("Tap to continue".center(10_8))

    daily_calorie_needed_sentence = daily_calorie_needed(bmr_result)
    print(steps_number(user_age))
    print(sleep_hr(user_age))

    answer = input('Do you want to be healthy and lose weight? y/n :').lower()
    new_calories_sentence, new_calories_res = new_calories(answer, body_type_sentence, daily_calorie_needed_sentence)
    print(new_calories_sentence)

    classification_of_calories_sentence = None
    if new_calories_res not in [0, -1]:
        classification_of_calories_sentence = classification_of_calories(new_calories_res)
        print(classification_of_calories_sentence)

    question = input('Do you prefer to know the recommended sports to play or not? y/n :').lower()
    sports_result = sports(question, body_type_sentence)
    print(sports_result)

    # and this how the program reads the json file  that includes the dictionaries
    with open('food.json') as json_file:
        food_data = json.load(json_file)

    print("Now let's plan our meals together and go for healthy choices!\nHow many meals a day would you like to have?\n2 or 3 or 4 or 5 ? ")
    num = int(input("No.of meals: "))

    cal_taken, fat_taken, protein_taken, carbs_taken = no_of_meals(num, food_data)

    print(f"The total Calories in your meals are {sum(cal_taken)}g.")
    print(f"The total grams of Fat in your meals are {sum(fat_taken)}g.")
    print(f"The total grams of Protein in your meals are {sum(protein_taken)}g.")
    print(f"The total grams of Carbohydrates in your meals are {sum(carbs_taken)}g.")

    save_user_info('results', f_name, l_name, user_age, day, month, year, gender, height, weight, bmi_result, bmr_result, body_type_sentence, daily_calorie_needed_sentence,
                   classification_of_calories_sentence, sports_result, cal_taken, fat_taken, protein_taken, carbs_taken)

    print(f"Your Info and Outputs are saved to \"results.txt\"")



