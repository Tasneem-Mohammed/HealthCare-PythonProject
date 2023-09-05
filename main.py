from Model import start_project
from OtherFn import thanks_function


if __name__ == "__main__":

    welcoming = "WELCOME TO THE HEALTHCARE PROGRAM !"
    welcoming2 = "YOUR WEIGHT LOSS, DIET, AND NUTRITION ASSISTANT"
    print()
    print(welcoming.center(10_8))
    print(welcoming2.center(10_8))
    print()
    input_type = input('Do you want to load your info through CLI or Text File (cli/file): ').lower()
    start_project(input_type)
    thanks_function()
