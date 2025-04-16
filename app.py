from flask import Flask,render_template,request,flash
app=Flask(__name__)
app.secret_key="your_secret_name"
@app.route("/",methods=["GET","POST"])
def register():
    if request.method=="POST":
        FirstName=request.form.get("FirstName")
        LastName=request.form.get("LastName")
        Email=request.form.get("Email")
        PhoneNumber=request.form.get("PhoneNumber")
        Password=request.form.get("Password")
        ConfirmPassword=request.form.get("ConfirmPassword")
        Gender=request.form.get("Gender")
        errors=[]
        if not FirstName or not LastName or not Email or not PhoneNumber or not Password or not ConfirmPassword or not Gender:
            errors.append("All fields are required to fill.")
        if Password!=ConfirmPassword:
            errors.append("Passwords doesn't match.")
        if not PhoneNumber.isdigit() or len(PhoneNumber)!=10:
            errors.append("PhoneNumber must be exactly 10 digits and contain only numbers")
        if '@' not in Email or '.' not in Email or not Email.endswith("com"):
            errors.append("Invalid Email!")
        if errors:
            error_message="\\n".join(errors)
            return f"""
            <script>
            alert("{error_message}");
            window.history.back();
            </script>
            """
        return render_template("success.html")
    return render_template("register.html")
@app.route("/success.html")
def success():
    return render_template("success.html")
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=3000)