import os
from flask import Flask, redirect, request, render_template, flash, url_for, make_response
from forms import ContactForm
from flask_mail import Mail, Message
import sqlite3

DATABASE = 'Karma.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/AddDefaultAccount", methods=['GET'])
def AccountAddDefaultDetails():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO RegistrationFormAccountData  ('FirstName', 'Surname', 'DateOfBirth', 'Address', 'Postcode', 'TelephoneNumber', 'EmailAddress', 'Username', 'Password')\
                VALUES (?,?,?,?,?,?,?,?,?)", ("Gabriel", "Agius", "19/05/2000", "57 priory Road", "CF31 4TA", "01656392012", "gabriel@gmail.com", "Gabriel.A", "NSA123"))
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return msg


@app.route("/AddAccount", methods=['POST', 'GET'])
def AccountAddDetails():
    if request.method == 'GET':
        return render_template('reg.html')
    if request.method == 'POST':
        # rem: args for get form for post
        FirstName = request.form.get('FirstName', default="Error")
        Surname = request.form.get('Surname', default="Error")
        DateOfBirth = request.form.get('DateOfBirth', default="Error")
        Address = request.form.get('Address', default="Error")
        Postcode = request.form.get('Postcode', default="Error")
        TelephoneNumber = request.form.get('TelephoneNumber', default="Error")
        EmailAddress = request.form.get('EmailAddress', default="Error")
        Username = request.form.get('Username', default="Error")
        Password = request.form.get('Password', default="Error")
        print("Adding Account"+FirstName)
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO RegistrationFormAccountData  ('FirstName', 'Surname', 'DateOfBirth', 'Address', 'Postcode', 'TelephoneNumber', 'EmailAddress', 'Username', 'Password')\
                    VALUES (?,?,?,?,?,?,?,?,?)", (FirstName, Surname, DateOfBirth, Address, Postcode, TelephoneNumber, EmailAddress, Username, Password))
            conn.commit()
            msg = "Account successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

######## LOGIN BUTTON PASSWORD ########


@app.route("/login", methods=['POST'])
def login():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        print('user not logged in')
        print(user_logged_in)
        if request.method == 'POST':
            # return render_template('layout.html')
            # rem: args for get form for post
            data = ()
            Username = request.form.get('uname', default="Error")
            Password = request.form.get('psw', default="Error")
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute(
                    "SELECT Username, Password FROM RegistrationFormAccountData WHERE Username=? AND Password=?", (Username, Password))
                data = cur.fetchall()
            except Exception as err:
                conn.rollback()
            finally:
                conn.close()

                if len(data) == 0:
                    return redirect(url_for('reg'))

                query_username = data[0][0]
                query_password = data[0][1]

                print(query_password)
                print(query_username)

                if query_username == Username and query_password == Password:
                    resp = make_response(render_template(
                        'home.html', logged_in=True))
                    resp.set_cookie('logged_in', 'True')
                return resp
                # return redirect(url_for('home'))

    else:
        print('user is logged in')
        print(user_logged_in)
        login = True
        return render_template('home.html', logged_in=login)


@app.route("/AddDefaultGroup", methods=['GET'])
def GroupAddDefaultDetails():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO RegistrationFormGroup  ('GroupName', 'GroupDescription', 'GroupArea')\
                VALUES (?,?,?)", ("Gardeners", "This group is for people who need help with gardening or want to do gardening for someone else", "Cardiff"))
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return msg


@app.route("/AddGroup", methods=['POST', 'GET'])
def AddGroup():
    if request.method == 'GET':
        return render_template('group.html')
    if request.method == 'POST':
        # rem: args for get form for post
        GroupName = request.form.get('GroupName', default="Error")
        GroupDescription = request.form.get(
            'GroupDescription', default="Error")
        GroupArea = request.form.get('GroupArea', default="Error")
        print("Adding Account"+GroupName)
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO RegistrationFormGroup  ('GroupName', 'GroupDescription', 'GroupArea')\
                    VALUES (?,?,?)", (GroupName, GroupDescription, GroupArea))
            conn.commit()
            msg = "Group successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg


@app.route('/allgroups')
def showAllGroups():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("select * from RegistrationFormGroup")

        rows = cur.fetchall()
        return render_template("allgroups.html", rows=rows, logged_in=login)


@app.route('/alltasks')
def showAllTasks():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
        return render_template('reg.html')
    else:
        login = True
        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("select * from TaskForm")

        rows = cur.fetchall()
        return render_template("alltasks.html", rows=rows, logged_in=login)


@app.route("/declineTask", methods=['POST', 'GET'])
def decline():
    if request.method == 'GET':
        return render_template('alltasks.html')
    if request.method == 'POST':
        try:
            TaskID = request.form.get('TaskID', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute('DELETE FROM TaskForm WHERE TaskID=?', (TaskID,))
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
            return redirect(url_for('alltasks'))

@app.route("/acceptTask", methods=['POST', 'GET'])
def accept():
    if request.method == 'GET':
        return render_template('alltasks.html')
    if request.method == 'POST':
        try:
            TaskID = request.form.get('TaskID', default="Error")
            Locations = request.form.get('Locations', default="Error")
            DnT = request.form.get('DnT', default="Error")
            Categories = request.form.get('Categories', default="Error")
            Description = request.form.get('Description', default="Error")
            Groups = request.form.get('Groups', default="Error")
            OnBehalf = request.form.get('OnBehalf', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO MyTask ('TaskID', 'Locations', 'DnT', 'Categories', 'Description', 'Groups', 'OnBehalf')\
                    VALUES (?,?,?,?,?,?,?)", (TaskID, Locations, DnT, Categories, Description, Groups, OnBehalf))
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
            return redirect(url_for('profile'))

@app.route("/deleteTask", methods=['POST', 'GET'])
def delete():
    if request.method == 'GET':
        return render_template('profile.html')
    if request.method == 'POST':
        try:
            MyTaskID = request.form.get('MyTaskID', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute('DELETE FROM MyTask WHERE MyTaskID=?', (MyTaskID,))
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
            return redirect(url_for('profile'))

@app.route("/completeTask", methods=['POST', 'GET'])
def complete():
    if request.method == 'GET':
        return render_template('profile.html')
    if request.method == 'POST':
        try:
            MyTaskID = request.form.get('MyTaskID', default="Error")
            TaskID = request.form.get('TaskID', default="Error")
            Locations = request.form.get('Locations', default="Error")
            DnT = request.form.get('DnT', default="Error")
            Categories = request.form.get('Categories', default="Error")
            Description = request.form.get('Description', default="Error")
            Groups = request.form.get('Groups', default="Error")
            OnBehalf = request.form.get('OnBehalf', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO CompleteList ('MyTaskID', 'TaskID', 'Locations', 'DnT', 'Categories', 'Description', 'Groups', 'OnBehalf')\
                    VALUES (?,?,?,?,?,?,?,?)", (MyTaskID, TaskID, Locations, DnT, Categories, Description, Groups, OnBehalf))
            cur.execute('DELETE FROM MyTask WHERE MyTaskID=?', (MyTaskID,))
            cur.execute('DELETE FROM TaskForm WHERE TaskID=?', (TaskID,))
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
            return redirect(url_for('profile'))

@app.route('/profile')
def showMyTasks():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
        return render_template('reg.html')
    else:
        login = True
        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        curs = con.cursor()
        cur.execute("select * from MyTask")
        curs.execute("select * from CompleteList")

        MT = cur.fetchall()
        CL = curs.fetchall()
        return render_template("profile.html", MT=MT, CL=CL, logged_in=login)

@app.route("/AddTask", methods=['POST', 'GET'])
def AddTask():
    if request.method == 'GET':
        return render_template('tasks.html')
    if request.method == 'POST':
        # rem: args for get form for post
        Locations = request.form.get('Locations', default="Error")
        DnT = request.form.get('DnT', default="Error")
        Categories = request.form.get('Categories', default="Error")
        Description = request.form.get('Description', default="Error")
        Groups = request.form.get('Groups', default="Error")
        OnBehalf = request.form.get('OnBehalf', default="Error")
        print("Adding New Task")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO TaskForm  ('Locations', 'DnT', 'Categories', 'Description', 'Groups', 'OnBehalf')\
                    VALUES (?,?,?,?,?,?)", (Locations, DnT, Categories, Description, Groups, OnBehalf))
            conn.commit()
            msg = "Task successfully added"
        except:
            conn.rollback()
            msg = "Task unsuccessfully added"
        finally:
            conn.close()
            return msg

# mail server idea taken and moddified from https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
mail = Mail()

app.secret_key = 'development key'

app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='edge14031985@gmail.com',
    MAIL_PASSWORD='lexie2008'
)

mail.init_app(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    #return render_template('contact.html', form=form,)

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=[
                          'david@walker-evans.com'])
            msg.body = """
    From: %s &lt;%s&gt;
    %s
    """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        user_logged_in = request.cookies.get('logged_in')
        if user_logged_in == None:
            login = False
        else:
            login = True
            return render_template('contact.html', form=form, logged_in=login)


@app.route('/home')
def home():
    # user_logged_in = request.cookies.get('logged_in')
    # print('here')
    # print(user_logged_in)
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    return render_template('home.html', logged_in=login)


@app.route('/alltasks')
def alltasks():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    # , logged_in = login
    return render_template('alltasks.html', logged_in=login)


@app.route('/reg')
def reg(*msg):
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    return render_template('reg.html', d=msg, logged_in=login)


@app.route('/group')
def group():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    # , logged_in = login
    return render_template('group.html', logged_in=login)

@app.route('/tasks')
def tasks():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    return render_template('tasks.html', logged_in=login)

@app.route('/profile')
def profile():
    user_logged_in = request.cookies.get('logged_in')
    if user_logged_in == None:
        login = False
    else:
        login = True
    # , logged_in = login
    return render_template('profile.html', logged_in=login)


if __name__ == "__main__":
    app.run(debug=True)
