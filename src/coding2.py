
from email.headerregistry import Address
from unicodedata import category
from click import password_option
from flask import *
from dbconnection1 import *
from datetime import date, datetime




app = Flask(__name__)
app.secret_key="abcd"





@app.route("/")
def home():
    return render_template("HOME1.html")


@app.route("/log")
def log():
    return render_template("index.html")


#LOGIN FUNCTION
@app.route('/login', methods=['post', 'get'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    qry = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)
    print(res)

    if res is None:
        return '''<script>alert("invalid"); window.location="/"</script>'''
    elif res['usertype'] == 'admin':
        session['lid']=res['login_id']
        return redirect('/admhome')
    elif res['usertype'] == 'user':

        session['lid']=res['login_id']
        return redirect('/userhome')
    else:
        return '''<script>alert("invalid"); window.location="/"</script>'''


#Registration Function
@app.route('/userregistration',methods=['get','post'])
def userregistration():


    name=request.form['fname']
    address=request.form['address']
    Gender=request.form['gender']
    DOB=request.form['dob']
    Email=request.form['email']
    
    
    
   
    Phone=request.form['phone']
    
    username=request.form['username']
    
    
    pswd=request.form['password']
    
   

    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'user')"


    val=(username,pswd)
    id=iud(qry,val)
      

    qry1="INSERT INTO `registration` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,address,Gender,DOB,Email,Phone)
    iud(qry1,val1)



    return '''<script>alert("Registerd successfuly");window.location="/"</script>'''

    

    
   
@app.route('/userhome')
def userhome():

   
   
   

    return render_template("user/ush.html")

   
@app.route('/reg',methods=['get','post'])
def reg():
    return render_template("user/registration.html")


@app.route('/admhome')
def admhome():

    return render_template("admin/adhm.html")



@app.route('/addns')
def addns():
    return render_template("admin/Addnews.html")



@app.route('/addnews',methods=['get','post'])
def addnews():
    
    newstitle=request.form['textfield']
  
    newsdetails=request.form['textfield3']

    qry1="INSERT INTO `news` VALUES(NULL,%s,curdate(),%s)"
    val1=(newstitle,newsdetails)
    iud(qry1,val1)
    return '''<script>alert("added successfuly");window.location="admhome"</script>'''



@app.route('/addevnts',methods=['get','post'])
def addevnts():
    return render_template("admin/addevents.html")

@app.route('/addevents',methods=['get','post'])
def addevents():


    
   
   eventname=request.form['textfield2']
   date=request.form['textfield3']
   eventdetails=request.form['textfield4']

   
   
   qry1="INSERT INTO `upcoming events` VALUES(NULL,%s,%s,%s)"
   val1=(eventname,date,eventdetails)
   iud(qry1,val1)
   return '''<script>alert("added successfuly");window.location="admhome"</script>'''


    

@app.route('/viewmembers')
def viewmembers():

    qry1="SELECT `registration`.*,membership.date FROM `registration` JOIN `membership` ON `registration`.`login_id`=`membership`.`user id`"
    res=selectall(qry1)
    return render_template("admin/viewmembers.html",val=res)






@app.route('/eventlist')
def eventlist():
    qry1= "SELECT*FROM `upcoming events`"
    res=selectall(qry1)
    return render_template("user/eventlist.html",val=res) 
 

@app.route('/viewnews')
def viewnews():
    qry1= "SELECT*FROM `news`"
    res=selectall(qry1)
    return render_template("user/news.html",val=res) 
 
#PROFILE UPDATION CODING PART






@app.route("/updprof")
def updprof():
    q1 = "SELECT * FROM `registration` WHERE registration.login_id=%s"
    res=selectone(q1,session['lid'])
    return render_template("user/update.html",val=res)


@app.route("/updpro",methods=['post','get'])
def updpro():
    
    name=request.form['textfield']
    
    address=request.form['textfield5']
    Email=request.form['textfield2']
    Gender=request.form['RadioGroup1']
    DOB=request.form['textfield7']
    Email=request.form['textfield2']
   
    Phone=request.form['textfield4']
    
   
    
    qry1 = "UPDATE `registration` SET `name`=%s,`address`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phoneno`=%s WHERE `login_id`=%s"
    val1 = (name,address,Gender,DOB,Email,Phone,session['lid'])
    iud(qry1, val1)
    
    return '''<script>alert("profile updated successfuly");window.location="userhome"</script>'''




@app.route("/member")
def member():
    session['lid']
    q1 = "SELECT * FROM `registration` WHERE login_id=%s"
    res=selectone(q1,session['lid'])
   
    
    return render_template("user/membership.html",val=res)


    


@app.route('/newmember',methods=['get','post'])
def newmember():

    q="SELECT *  FROM `membership` WHERE `user id`=%s"
    res=selectone(q,session['lid'])
    if res is None:

        qry1="INSERT INTO `membership` VALUES(NULL,%s,curdate(),'pending')"
        iud(qry1,session['lid'])
        return '''<script>alert("joined successfuly");window.location="/userhome"</script>'''

        

    else:
        return '''<script>alert("already join");window.location="/userhome"</script>'''
    
    
    




@app.route('/adminevent')
def adminevent():
    qry1= "SELECT*FROM `upcoming events`"
    res=selectall(qry1)
    return render_template("admin/adevents.html",val=res) 
 
    
@app.route('/deleteevnts')
def deleteevnts():  
    id=request.args.get('id')
    qry="DELETE FROM`upcoming events` WHERE`eventid`=%s"
    iud(qry,id)  
    return '''<script>alert("deleted successfuly");window.location="/adminevent"</script>'''

   


app.run(debug=True)






  

