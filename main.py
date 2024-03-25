# Jade Thompson, jet475
# This program prompts a user for their height and weight, then calculates and outputs the corresponding body mass index (BMI).

# This program was created for CSE 4283 Software Testing & QA. 
# This assignment covers test-driven development (TDD), unit testing, and boundary testing.

from flask import Flask, request, render_template

app = Flask(__name__)

# initialize routing/index page
@app.route("/", methods=['GET','POST'])
def index():
    # if submit button pushed
    if request.method == 'POST':
        bmi = 0
        # extract from form
        heightft = request.form['heightfeet']
        heightin = request.form['heightinches']
        weightlbs = request.form['weight']

        # bmi of -1 is processed as invalid on client side
        try:
            if(int(heightft) <= 0 or int(heightin) < 0):
                bmi = -1
        except ValueError:
                bmi = -1
        try:
            if(int(weightlbs) < 0):
                bmi = -1
        except ValueError:
            bmi = -1
        # calculate bmi if no errors detected
        if bmi == 0:
            total_inches = ftin_to_in(int(heightft), int(heightin))
            bmi = calculate_bmi(total_inches, int(weightlbs))
        return render_template('index.html', bmi=bmi, category=get_category(bmi))
    else:
        # if no post request, just render blank form page
        return render_template('index.html', data=[0, 0])

# calculates total inches from user-given feet and inches
def ftin_to_in(feet, inches):
    if(inches + (feet * 12)) > 0:
        return inches + (feet * 12)
    return -1

# calculates BMI using total inches and weight in lbs
def calculate_bmi(inches, weight):
    kg = weight * 0.45
    m_sq = (inches * 0.025) ** 2
    if(kg / m_sq) > 0:
        return round(kg / m_sq, 2)
    return -1

# detects BMI range
def get_category(final_bmi):
    if(final_bmi <= 0.00):
        # print("Invalid BMI")
        return "Invalid inputs. Please try again."
    if(final_bmi >= 30.00):
        # obese
        # print("Category: Obese")
        return "Category: Obese"
    elif(final_bmi >= 25.00):
        # overweight
        # print("Category: Overweight")
        return "Category: Overweight"
    elif(final_bmi >= 18.50):
        # normal weight
        # print("Category: Normal Weight")
        return "Category: Normal Weight"
    else:
        # underweight
        # print("Category: Underweight")
        return "Category: Underweight"


if __name__ == '__main__':
    app.run(debug = True)

