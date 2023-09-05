import sys


# GREETING FUNCTION
def greeting(first_name, last_name):
    print(f'Hello {first_name} {last_name} How are you?')
    return first_name, last_name


# THANKS FN:
def thanks_function():
    print()
    print("Thanks for using our program!".center(10_8))
    print()
    sys.exit("")


def save_user_info(file_name, first_name, last_name, user_age, day, month, year, gender, height, weight, bmi, bmr, body_type,
                   daily_calorie_needed_sentence, classification_of_calories_sentence, sports_result,
                   cal_taken, fat_taken, protein_taken, carbs_taken):

    user_info = open(f'{file_name}.txt', 'w+')

    user_info.write('First Name:  '+str(first_name)+'\n')
    user_info.write('Last Name:  '+str(last_name)+'\n')
    user_info.writelines('Age:  '+str(user_age)+'\n')
    user_info.write('Birthday date:  '+str(day)+'/'+str(month)+'/'+str(year)+'\n')
    user_info.writelines('Gender:  '+gender+'\n')
    user_info.writelines('Height in cm:  '+str(height)+'\n')
    user_info.writelines('Weight in kg:  '+str(weight)+'\n')
    user_info.writelines('Your BMI =  '+str(bmi)+'\n')
    user_info.writelines('Your BMR =  '+str(bmr)+'\n')
    user_info.writelines('Body type:  '+str(body_type)+'\n')
    user_info.writelines('Daily Calorie Needed:  '+str(daily_calorie_needed_sentence)+'\n')
    user_info.writelines('Classification of Calories:  '+str(classification_of_calories_sentence)+'\n')
    user_info.writelines('Sports:  '+str(sports_result)+'\n')
    user_info.writelines(f"The total Calories in your meals are {sum(cal_taken)}g.\n")
    user_info.writelines(f"The total grams of Fat in your meals are {sum(fat_taken)}g.\n")
    user_info.writelines(f"The total grams of Protein in your meals are {sum(protein_taken)}g.\n")
    user_info.writelines(f"The total grams of Carbohydrates in your meals are {sum(carbs_taken)}g.\n")
    user_info.close()
