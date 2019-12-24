from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name)
    except:
        return render_template('index.html')


def write_to_file(data):
    with open('database.txt', 'a') as file:
        file.write(f'{data}\n')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


# @app.route('/index.html')
# def presshome():
#     return render_template('index.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


if __name__ == '__main__':
    app.run()
