# About
This program calculates a user's body mass index (BMI) based on provided height and weight. BMI category is also determined and provided.

You can access the hosted version of this project at: http://jadethomp.pythonanywhere.com/

# Dependencies
Python must be installed on your system to run this program. If you do not have Python installed, access the latest version at https://www.python.org/downloads/ . Follow the website and installer's guidance for installation.

If you wish to run the unit tests included in this repository, you must have the Pytest testing framework installed. You can access instructions for installing Pytest at https://docs.pytest.org/en/7.1.x/getting-started.html .

As of 3/25/24, this program now uses a GUI! This local web app uses the Flask web framework. Install Flask on your machine using this command:

`pip install Flask`

You must have pip installed for this command to work. If it is not installed, follow the OS-specific instructions at https://pip.pypa.io/en/stable/installation/ .

# Running the Program
On a system that has Python installed, navigate to the directory containing main.py in your local command line. Run the following command:

`python3 main.py`

While the program is running, navigate to http://127.0.0.1:5000/ in your local browser. From here, you should be able to view and interact with the interface.

To run the unit tests, navigate to the directory containing main.py and test_main.py. Run the following command:

`python -m pytest`

You will then be able to review a summary of the conducted unit tests.

