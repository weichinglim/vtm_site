import app

def test_calculate_current_age():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r")
    print(" -- calculate_current_age unit test")
    assert app.calculate_current_age(2000) == 22  #will change as the years progress


def test_calculate_future_age():
    """ 
    GIVEN a user age
    WHEN that age is passed to this function
    THEN 10 years are added to the user's age
    """
    print("-- calculate_future_age unit test")
    assert app.calculate_future_age(20) == 30  


def test_calculate_past_age():
    """ 
    GIVEN a user age
    WHEN that age is passed to this function
    THEN 10 years are subtracted from the user's agee
    """
    print("-- calculate_past_age unit test")
    assert app.calculate_past_age(20) == 10  