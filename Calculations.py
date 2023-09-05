import datetime
import sys
from OtherFn import thanks_function


# AGE CALCULATOR:
def age_calculator(date_of_birth):
    # the code compares between today's date & b.d's date
    # if the expression is True : boolean= 1 ; False: boolean= 0
    today = datetime.date.today()
    is_the_bd_has_come_yet_or_not = ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    age = today.year - date_of_birth.year - is_the_bd_has_come_yet_or_not
    return age


# BMI calculator:
def body_mass_index(height, weight):
    bmi = round((weight / (height/100)**2), 2)
    return bmi


# Body Type:
def body_type(bmi, Q_of_body_type):
    if Q_of_body_type == "y":
        if bmi <= 18.5:
            return"You are underweight."
        elif 18.5 < bmi <= 24.9:
            return "Congratulations ! Your weight is normal."
        elif 25 < bmi <= 29.29:
            return "You are overweight."
        else:
            return 'You are obese.'
    elif Q_of_body_type == 'n':
        return input('OK then ,I guess you may want to know your BMR ,tap to calculate it')

    else:
        sys.exit("Incorrect Input")


# BMR calculator :
def bmr_calculator(height, weight, age, gender):
    bmr = None
    if gender == 'male':
        bmr = int(66.47+(13.75 * weight)+(5.003 * height)-(6.775*age))
    elif gender == 'female':
        bmr = int(655.1+(9.563*weight)+(1.850*height)-(4.676*age))
    else:
        print("Error!!!")
        thanks_function()
        return
    return bmr


# daily calories :
def daily_calorie_needed(bmr):
    print('Do you workout?:\n'
          "1)No, I don't. \n"
          '2)Only walks.\n'
          '3)1-2 times a week.\n'
          '4)3-5 times a week.\n'
          '5)More than 5 times a week.\n')
    activity = int(input("Your answer is number:"))
    if activity == 1:
        activity_index = 1.2
    elif activity == 2:
        activity_index = 1.375
    elif activity == 3:
        activity_index = 1.46
    elif activity == 4:
        activity_index = 1.725
    elif activity == 5:
        activity_index = 1.9
    else:
        print("Invalid Input")
        thanks_function()
        return

    daily_calorie_needed = int(bmr * activity_index)
    print(f'To maintain your current weight you need {daily_calorie_needed} calorie a day,')
    return daily_calorie_needed


# DAILY STEPS YOU HAVE TO WALK:
def steps_number(age):
    if age < 18:
        steps = "Also you need a minimum of 6,000 to 15,000 steps a day."
    elif (age == 18 or age > 18) and (age < 65):
        steps = "Also you need a minimum of 10,000 steps to 12,000 steps a day."
    else:
        steps = "Also you need a minimum of 3,000 steps to 10,000 steps a day."
    return steps


# RECOMMENDED HOURS TO SLEEP :
def sleep_hr(age):
    if 0 < age < 1:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 12 to 17 hours'  # newborns & infants
    elif 1 <= age <= 2:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 11 to 14 hours'  # Toddlers
    elif 3 <= age <= 5:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 10 to 13 hours'  # Preschool
    elif 6 <= age <= 12:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 9 to 12 hours'   # School age
    elif 13 <= age < 18:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 8 to 10 hours'   # Teen
    elif 18 <= age <= 60:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 7 or more hours'
    elif 61 <= age <= 64:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 7 to 9 hours'
    elif age > 65:
        hr = 'In order to stay healthy; according to your age ,the recommended hours of sleep per day is 7 to 8 hours'
    return hr


# NEW CALORIES CALCULATOR :
def new_calories(answer, body_type, daily_calorie_needed):
    if answer == 'y':
        if body_type == 'You are underweight.':
            new_calories_res = int(daily_calorie_needed + 750)
            return f'You have to gain weight,you need  {new_calories_res} calorie a day to gain one kg', new_calories_res
        elif body_type == 'You are obese.' or body_type == 'You are overweight.':
            new_calories_res = int(daily_calorie_needed - 750)
            return f'You have to lose weight ,you need {new_calories_res} calorie a day to lose one kg', new_calories_res
        else:
            return 'Your bmi is very good, you do not have to gain or lose weight', 0
    elif answer == 'n':
        return 'Ok but, remember that good health is above wealth !', -1


# CLASSIFICATION OF CALORIES
def classification_of_calories(new_calories_value):
    value = new_calories_value
    calories_from_protein = round(0.4 * value)
    calories_in_protein = round(calories_from_protein/4)
    calories_from_carbs = round(0.4 * value)
    calories_in_carbs = round(calories_from_carbs/4)
    calories_from_fats = round(0.2 * value)
    calories_in_fats = round(calories_from_fats/9)
    return f'Here are the classification of nutrients for your body,you need :\n ' \
           f'{calories_from_protein}  Calories from protein which are {calories_in_protein} grams of protein.\n ' \
           f'{calories_from_carbs}  Calories from carbs which are {calories_in_carbs} grams of carbs. \n ' \
           f'{calories_from_fats}  Calories from fats which are {calories_in_fats} grams of fats.'


def total_cal_eaten(food_db, user_order, serving):
    cal_taken = food_db[user_order]['cal']*serving
    fat_taken = food_db[user_order]['fat']*serving
    protein_taken = food_db[user_order]['pro']*serving
    carbs_taken = food_db[user_order]['carb']*serving
    return cal_taken, fat_taken, protein_taken, carbs_taken


# NUMBER OF DAILY MEALS:
def no_of_meals(num, food_db):

    cal_taken = []
    fat_taken = []
    protein_taken = []
    carbs_taken = []

    order_complete = True
    order_list = []
    if num == 2:
        meal = 'breakfast,dinner'
    elif num == 3:
        meal = 'breakfast,lunch ,dinner'
    elif num == 4:
        meal = 'breakfast,lunch,dinner ,snack'
    elif num == 5:
        meal = 'breakfast,lunch,dinner ,2 snacks'
    print(f'Good choice, you will have {meal}')

    meal = meal.split(',')
    for i in meal:
        print(f'Now,choose your favourite food  you would like to have in your {i}:')
        while order_complete:
            user_order = input('Food: ')
            if user_order in food_db:
                order_list.append(user_order)
            while user_order not in food_db:
                print("Sorry! Your food choice is not in my database,\nPlease choose another option")
                user_order = input('Food: ')
                order_list.append(user_order)
            print(f"serving size : {food_db[user_order]['serve']}")
            print(f'How much (serving) do you want from "{user_order}" ?')
            serving = int(input("Serving: "))
            another = input("Do you want to have anything else ?(y/n) ").lower()

            cal, fat, protein, carbs = total_cal_eaten(food_db, user_order, serving)
            cal_taken.append(cal)
            fat_taken.append(fat)
            protein_taken.append(protein)
            carbs_taken.append(carbs)

            if another == 'y':
                continue
            elif another == 'n':
                break

    print(f' I loved your healthy choices, keep going!\n '
          f'Here are all your meal ingredients you have ordered:{set(order_list)} ')

    return cal_taken, fat_taken, protein_taken, carbs_taken


# SPORTS RECOMMENDATION:
def sports(question, body_type):
    if question == 'y':
        if body_type == 'You are underweight.':
            return f'You will gain weight by building muscles , so you should try weightlifting and squats\n' \
                   f'and it is better to prevent endurance sports as they burn alot of cal without stimulating muscle growth'
        elif body_type == 'You are obese.' or body_type == 'You are overweight.':
            return f'You should try boxing or cycling as they burn up to 800 calories/hr !'
        elif body_type == 'Congratulations ! Your weight is normal.':
            return f'Squash, Swimming, gymnastics and running are ultimately the best sports to play to make your body more healthy!'
    elif question == 'n':
        return 'Ok, but do not forget to exercise at least once a week to keep your body healthy'





