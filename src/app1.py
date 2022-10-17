from flask import *

from dbconnection import *
from datetime import datetime
app=Flask(__name__)


@app.route('/')
def log():
    return render_template("login2.html")

#login function
@app.route('/login', methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry=" SELECT * FROM login WHERE username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="login_index"</script>'''
    elif res['usertype'] == "admin":
        return '''<script>alert("valid");window.location="admin"</script>'''
    elif res['usertype'] == "patient":
         return '''<script>alert("valid");window.location="Patienthome"</script>'''
    elif res['usertype'] == "doctor":
         return '''<script>alert("valid");window.location="Doctor"</script>'''
    elif res['usertype'] == "nurse":
         return '''<script>alert("valid");window.location="Nurse"</script>'''
    elif res['usertype'] == "pharmacist":
         return '''<script>alert("valid");window.location="Pharmacist"</script>'''
    else:
        return '''<scrpit>alert("invalid");window.location="login"</scrpit>'''

#Registration Function
@app.route('/registration', methods=['post'])
def registration():
    name=request.form['textfield']
    home=request.form['home']
    place=request.form['place']
    city=request.form['city']
    pincode=request.form['pincode']
    Bloodgroup=request.form['textfield3']
    Gender=request.form['radiobutton']
    age=request.form['textfield2']
    Email=request.form['textfield3']
    DOB=request.form['textfield5']
    Phone=request.form['textfield6']
    username=request.form['textfield7']
    password=request.form['textfield9']
    
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'patient')"
    val=(username,password)
    id=iud(qry,val)
   
    qry1="INSERT INTO `patient details` VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,home,place,city,pincode,Gender,Bloodgroup,Email,DOB,Phone,age)
    iud(qry1,val1)
    return '''<script>alert("Registerd successfuly");window.location="/"</script>'''
    

@app.route("/register")
def register():
    return render_template("Patient/Register.html")
 
   


    

@app.route('/admin')
def admin_home():
    return render_template("admin home.html")

@app.route("/Manage Time Slot")
def Time_Slot():
    return render_template("Add Time Slot.html")

@app.route("/Add staff Data")
def Add_staff():
    return render_template("AddStaffData.html")

@app.route("/View Staff Data")
def View_staff():
    return render_template("ViewStaffData.html")

@app.route("/View Booking For Doctor")
def BOOKING():
    return render_template("ViewBooking.html")

@app.route("/Vaccine Details")
def Vaccine():
    return render_template("VaccineDetails.html")

@app.route("/View Vaccine Booking")
def Vaccine_booking():
    return render_template("ViewVaccineBooking.html")

@app.route("/View Feedback")
def View_feedback():
    return render_template("ViewFeedback.html")

@app.route("/Sent Notification")
def Sent_notification():
    return render_template("SentNotification.html")

#Patient Home
@app.route("/Patienthome")
def Patient_home():
    return render_template("Patient/Patient home.html")

@app.route("/updateprof")
def updateprof():
    return render_template("Patient/UPDATE PROFILE.html")

@app.route("/DoctorBooking")
def DoctorBooking():
    return render_template("Patient/Doctor Booking.html")

@app.route("/Doctor Booking1")
def DocotrBooking1():
    return render_template("Patient/Doctor Booking1.html")

@app.route("/VaccineBook")
def VaccineBook():
    return render_template("Patient/vaccineBook.html")

@app.route("/View prescription")
def view():
    return render_template("Patient/ViewPrescription.html")

@app.route("/Add feedback")
def Add_feedback():
    return render_template("Patient/SendFeedback.html")

@app.route("/View notification")
def View_notification():
    return render_template("Patient/ViewNotification.html")













@app.route("/adfeedback")
def adfeedbak():
    return render_template("Patient/ADD FEEDBACK.html")
    








app.run(debug=True)