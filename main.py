# Jade Thompson, jet475
# This program prompts a user for their height and weight, then calculates and outputs the corresponding body mass index (BMI).

# This program was created for CSE 4283 Software Testing & QA. 
# This assignment covers test-driven development (TDD), unit testing, and boundary testing.

def ftin_to_in(feet, inches):
    return inches + (feet * 12)

def calculate_bmi(inches, weight):
    kg = weight * 0.45
    m_sq = (inches * 0.025) ** 2
    return kg / m_sq

if __name__ == '__main__':
    while(1):
        # ask for height
        user_input = input("Please input your height in feet and inches, separating the two values with a space.\nFor instance, if you are 5\'0\", input 5 0.\n>> ")
        height_list = user_input.split()
        if(len(height_list) < 2):
            print("Not enough values. Please try again.")
            continue
        try:
            if(int(height_list[0]) < 0 or int(height_list[1]) < 0):
                print("Invalid height. Please try again.")
                continue
        except ValueError:
            print("Input not accepted. Please try again.")
            continue
        total_inches = ftin_to_in(int(height_list[0]), int(height_list[1]))

        while(1):
            # ask for weight
            user_input = input("Please input your weight in pounds.\n>> ")
            try:
                if(int(user_input) < 0):
                    print("Invalid weight. Please try again.")
                    continue
            except ValueError:
                print("Input not accepted. Please try again.")
                continue
            print("Your BMI is " + str(round(calculate_bmi(total_inches, int(user_input)))) + ".")
            break
        break

