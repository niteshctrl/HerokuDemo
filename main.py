# Integrate HTML with Flask // Jinja
# HTTP verb : GET and POST


# Jinja2 template
'''{%...%} for statements // if statements // etc
{{   }} expressions to print output
{#...#} this is for comments
'''


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)   # App name # WSGI App


@app.route('/')         # Decorator; '/' = String which is the URL we will go in that webpage
def welcome():          # This is the function which will be trigerred whenever we goto the decorator webpage
    return render_template('index.html')


'''@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=40:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html', result=res, marks=score)'''


@app.route('/success/<int:score>')
def success(score):
    return render_template('result1.html', result=score)


# Result checker submit HTML page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score_avg = 0
    if request.method =='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        
        total_score_avg = (science + maths + c + data_science) / 4


    return redirect(url_for('success',score=total_score_avg))


if __name__=='__main__':
    app.run(debug=True)           # debug=True will create a live server
