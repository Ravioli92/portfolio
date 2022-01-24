from flask import Flask, render_template,url_for, request, redirect #added url_for as per 265.Template Engine
import csv
app = Flask(__name__)
print(__name__)

#Decorator: App.route decorator makes it so that anytime we hit /, it defines 'hello_world' and returns "Hello world"

@app.route("/") #refers to the end point
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:    #mode=a is append to that file because it already exists
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
    return

def write_to_csv(data): #CSV stands for comma seperated values
    with open('database.csv', mode='a') as database2:    #mode=a is append to that file because it already exists
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',newline='',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()    #this turns form data into dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except: 'did not save to database'
    else:
        return 'Something went wrong. Try again!'

''' THIS IS GOING TO BE SUPERSEDED - NEW DYNAMIC CODE THAT OPENS PER HTML FILE WILL BE WRITTEN
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

'''




'''
app = Flask(__name__)

@app.route("/")
def hello(): 
    return "You did it bro"

if __name__ == "__main__":
    app.run(port=5000)
'''