import time

def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Mike&#39;s Friends" in res.data # &#39; was used in place of '
        assert b"My List of Friends" in res.data
        assert b"My Friends" in res.data


def test_mike_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/mike' route is requested (GET)
    THEN check that the response is valid
    """
    print("-- /mike GET test")
    with app.test_client() as test_client:
        res = test_client.get('/mike')
        assert res.status_code == 200
        assert b"Hello Mike!!" in res.data


def test_add_friend_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/add_friend' route is requested (GET)
    THEN check that the user is redirected to the home page
    """
    print("-- /add_friend GET test")
    with app.test_client() as test_client:
        res = test_client.get('/add_friend')
        assert res.status_code == 302
        assert res.headers["Location"] == "/" # where are you redirecting the user


def test_add_friend_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/add_friend' route is requested (POST)
    THEN check that the new user is added to the list
    """
    print("-- /add_friend POST test")
    #add a name to the list and test for redirection
    with app.test_client() as test_client:
        new_friend = {"fname":"amy", "lname":"colbert"}
        res = test_client.post('/add_friend', data=new_friend)
        assert res.status_code == 302 # Found

    #after redirection, see if the name is on the list
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"amy colbert" in res.data    

    
def test_age_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/age' route is requested (GET)
    THEN check that the correct page is displayed
    """
    print("-- /age GET test")
    with app.test_client() as test_client:
        res = test_client.get('/age')
        assert res.status_code == 200
        assert b"What year were you born?" in res.data

def test_age_future_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'future' button is selected (POST)
    THEN check that the correct age is returned to the user
    """
    print("-- /age 'future' POST test")
    # Functional test - it puts POST data in the age route and looks for the correct value to be returned
    # individual functions to perform the calculations are tested in the Unit tests
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        # passing future age value as 'x' because I look for the key(future_age), not the value in app.py if/then stmt
        calc_age = {"birth_year":"1972", "future_age":"x"} 
        res = test_client.post('/age', data=calc_age)
        assert res.status_code == 200 
        assert b"60.0" in res.data # may need adjusted depending on current year

def test_age_past_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'past' button is selected (POST)
    THEN check that the correct age is returned to the user
    """
    print("-- /age 'past' POST test")
    # Functional test - it puts POST data in the age route and looks for the correct value to be returned
    # individual functions to perform the calculations are tested in the Unit tests
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        # passing future age value as 'x' because I look for the key(future_age), not the value in app.py if/then stmt
        calc_age = {"birth_year":"1972", "past_age":"x"} 
        res = test_client.post('/age', data=calc_age)
        assert res.status_code == 200 
        assert b"40.0" in res.data # may need adjusted depending on current year