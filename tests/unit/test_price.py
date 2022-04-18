import app

def test_calculate_area():
    """ 
    GIVEN a user enters the radius and height in inches 
    WHEN that radius and height is passed to this function
    THEN the tank area in square feet is accurately calculated 
    """
    print("\r")
    print(" -- calculate_area unit test")
    assert app.calculate_area(360, 180) == 3532.50  #will change


def test_calculate_material_cost():
    """
    GIVEN the total area of tank in square feet
    WHEN that total area in square feet is passed to this function
    THEN material cost of $25 is multiplied with the given total area (in sqft)
    """
    print("-- calculate_material_cost unit test")
    assert app.calculate_material_cost(3532.50) == 88312.50  


def test_calculate_labor_cost():
    """
    GIVEN total area of tank in square feet
    WHEN that total area in square feet is passed to this function
    THEN labor cost of $15 is multiplied with the given total area (in sqft)
    """
    print("-- calculate_labor_cost unit test")
    assert app.calculate_labor_cost(3532.50) == 52987.50 


def test_calculate_price():
    """
    GIVEN the total material cost and total labor cost
    WHEN that total material cost and total labor cost is passed to this function
    THEN the total cost estimate of tank painting is accurately calculated
    """
    print("\r")
    print(" -- calculate_price unit test")
    assert app.calculate_price(88312.50, 52987.50) == 141300.00
