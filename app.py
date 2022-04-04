from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='Vertical Tank Maintenance')

@app.route('/estimate', methods=['POST', 'GET'])
def estimate():
    price=''
    if request.method == 'POST':
        form = request.form
        tankHeight = float(form['height'])
        tankRadius = float(form['radius'])

        #Area of tank top
        pi = 3.14
        area_top = 2*(pi*tankRadius*tankRadius)

        #Area of tank sides
        area_sides = 2*(pi*(tankRadius*tankHeight))

        #Calculate total area
        total_area = area_top+area_sides

        #Convert total area in inches to square feet
        total_sf = total_area/144

        #Calculate material cost
        materialCost = 25.00 #per square foot
        total_mc = total_sf*materialCost

        #Calculate labor cost
        laborCost = 15.00 #per square foot
        total_lc = total_sf*laborCost

        #Total price
        total_ce = total_mc+total_lc #total_ce = total cost estimate

        #return redirect(url_for('index'))
        return render_template('estimate.html', price=total_ce)
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=False)