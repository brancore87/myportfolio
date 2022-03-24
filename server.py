from dataclasses import field
from fileinput import filename
from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:bran>')
def html_page(bran):
    return render_template(bran)

def write_to_text(data):
    with open('database.txt', 'a') as db_file:
            db_file.write(f"{str(data)}\n")

def write2_to_text(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\nEmail:{email}\nSubject:{subject}\nMessage:{message}\n")

def write_to_csv(data):
    with open('database.csv', 'a', newline='\n') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        field_names = [email, subject, message]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(field_names)

# Post-> Browser wants us to save Info | Get-> Browser wants us to send Info
@app.route('/submit_form', methods=['POST', 'GET']) 
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_text(data)
            # write2_to_text(data)
            write_to_csv(data)
            return redirect('submitted.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again'