import pytest
from main import *

@pytest.mark.parametrize("ft_val, in_val, calcs", [(5, 6, 66), (4, 0, 48), (0, 0, -1), (-4, -5, -1)])
def test_ftin_to_in(ft_val, in_val, calcs):
    assert ftin_to_in(ft_val, in_val) == calcs

@pytest.mark.parametrize("total_in, weight_val, bmi_calcs", [(65, 160, 27.27), (65, 0, -1), (65, -160, -1)])
def test_calculate_bmi(total_in, weight_val, bmi_calcs):
    assert calculate_bmi(total_in, weight_val) == bmi_calcs

@pytest.mark.parametrize("bmi, statement", [(16.00, "Category: Underweight"), (0.00, "Invalid inputs. Please try again."), (0.50, "Category: Underweight"),
                                             (21.00, "Category: Normal Weight"), (18.50, "Category: Normal Weight"), (18.49, "Category: Underweight"), 
                                             (27.00, "Category: Overweight"), (25.0, "Category: Overweight"), (24.90, "Category: Normal Weight"), 
                                             (35.00, "Category: Obese"), (30.00, "Category: Obese"), (29.90, "Category: Overweight")])
def test_print_category(bmi, statement):
    get_category(bmi)
    assert get_category(bmi) == statement
