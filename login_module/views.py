from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysql.connector import MySQLConnection, Error
from forms import Form

# Create your views here.

def login_data(request):
    try:
        username = request.POST.get('username','')
        phone = request.POST.get('phone', '')

        Error_dict = {}

        dbconfig = {'password': 'root', 'host': 'localhost', 'user': 'root', 'database': 'login_database'}
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        username = "'" + username + "'"
        cursor.execute("select COUNT(*) from client_info where Name = " + username + " AND phone_no = " + str(phone) + " ")
        count = cursor.fetchone()

        if(count[0] <= 0) :
            Error_dict['Wrong_values'] = "Wrong Username or Phone no"

        else :
            context_dict = {}
            context_dict['name'] = username
            return render_to_response('logged_in_user.html', context_dict)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    return render_to_response('login_form.html', Error_dict)

def register_data(request):
    try:
        username = request.POST.get('username','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        Error_dict = {}

        if(username == '' or email == "" or phone == "" ) :
            Error_dict['Invalid'] = "Enter Correct Values"

        else:
            dbconfig = {'password': 'root', 'host': 'localhost', 'user': 'root', 'database': 'login_database'}
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("select COUNT(*) from client_info where  phone_no = " + str(phone) + " ")
            count = cursor.fetchone()
            count = count[0]
            if(count > 0):
                Error_dict['user_exist'] = "User Already Exist"
            else:
                cursor.execute("insert into client_info (Name , email, phone_no) values ('%s', '%s', '%s')" % (username, email, phone))
                conn.commit()
                return HttpResponseRedirect('register_success')
    except Error as e:
        print(e)

    return render_to_response('register_form.html',  Error_dict)

def register_success(request):
    return render_to_response('register_success.html')

def logged_in(request):
    return render_to_response('logged_in_user.html')