from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

def calculate_area(tankHeight, tankRadius):
    #Area of tank top
    pi = 3.14
    area_top = pi*tankRadius*tankRadius

    #Area of tank sides
    area_sides = 2*(pi*(tankRadius*tankHeight))

    #Calculate total area
    total_area = area_top+area_sides

    #Convert total area in inches to square feet
    total_area_sqft = total_area/144
    return total_area_sqft

def calculate_material_cost(total_area_sqft):
    #Calculate material cost
    materialCost = 25.00 #per square foot
    total_material_cost = total_area_sqft*materialCost
    return total_material_cost

def calculate_labor_cost(total_area_sqft):
    #Calculate labor cost
    laborCost = 15.00 #per square foot
    total_labor_cost = total_area_sqft*laborCost
    return total_labor_cost

def calculate_price(total_material_cost, total_labor_cost):
    #Total price
    return total_material_cost+total_labor_cost

@app.route('/estimate', methods=['POST', 'GET'])
def estimate():
    price=''
    if request.method == 'POST':
        form = request.form
        tankHeight = float(form['height'])
        tankRadius = float(form['radius'])

        total_area_sqft = calculate_area(tankHeight,tankRadius)
        total_material_cost = calculate_material_cost(total_area_sqft)
        total_labor_cost = calculate_labor_cost(total_area_sqft)

        if 'price_estimate' in request.form:
            price_est = calculate_price(total_material_cost, total_labor_cost)

        return render_template('estimate.html', pageTitle='VTM Estimator', price=price_est) #price=jinja , price_est=python
    return render_template('estimate.html', pageTitle='VTM Estimator')

if __name__ == '__main__':
    app.run(debug=False)