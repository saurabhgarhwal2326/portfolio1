from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
   
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    mobile_number = request.form.get('mobile_number')
    email_subject = request.form.get('email_subject')
    message = request.form.get('message')

    print(f"Full Name: {full_name}")
    print(f"Email: {email}")
    print(f"Mobile Number: {mobile_number}")
    print(f"Subject: {email_subject}")
    print(f"Message: {message}")
    user_data = [full_name,email,mobile_number,email_subject,message]
    return f"Thank you, {full_name}! Your message has been received."


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4444,debug=True)
