print('\n'*100)
print('======================================================================>>>RAILWAY   TICKET   RESERVATION<<<==========================================================================')             


import mysql.connector as m
sqpass='saysum@new'
con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
cursor=con.cursor()



#function to take user details and store them in the sql database in the form of table
def singup():

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    fn = input("Enter Your User Name : ")
    ge=input("Enter Gender : ")
    db = input("Enter Date of Birth in format(yyyy-mm-dd) : ")
    x=mc()#function for keeping unique phone numbers 

    if x==None:
        print()
    else:
        mb=x
    #password function
    passwd=pawd()

    un="select  username from accountinfo where username='%s'"%(fn,)
    cursor.execute(un)
    data=cursor.fetchone()

    if data==None:
        #inserting into the table given parameters
            st="insert into accountinfo(username,gender,dob,mobile_number,password)values('{}','{}','{}',{},'{}')".format(fn,ge,db,mb,passwd)
            cursor.execute(st)
            con.commit()
            print('YOUR ACCOUNT CREATED SUCCESFULLY!')

    else:
        for i in data:
            if i==fn:
                unique()

    con.close()



#function for keeping unique phone numbers 
def mc():

    y=True
    while y:
        mb=input("Enter Mobile Number : ")
        ci=int(mb)
        x="select mobile_number from accountinfo where mobile_number='%s'"%(ci,)
        cursor.execute(x)
        data=cursor.fetchone()

        if data==None:
            print('\nThis number cannot be used by other users to signup in this software\n')
            y=False
            return mb
        else:
            print('\nThe number already in use for some another account!\nPlease try with another number.\n')
            y=True
            


# To check the duplicate username in database
def unique():

    print('\nIt seems that you are already registered with this user name\n')
    ch=input('press Y to continue with that profile! and N for creating new profile with different username\n ')#asking user if he/she already registered and wanted to continue

    if ch=='Y'or ch=='y':
        login()
    elif ch=='N' or ch=='n':
        singup()
    else:
        print('press only y/n\n')
        unique()
            


# password function make you to proceed further if both password and confirm password are same
def pawd():

    passwd=input('Enter Your Password Here :')
    confirm=input('Please Confirm Your Password :')
    

    #checking 
    if passwd==confirm:
        return passwd

    #if not matched
    else:
        print('ERROR\nPLEASE RE-ENTER YOUR PASSWD\n')
        pawd()
        return passwd



#function to make user view all his/her details
def display(uname):

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    #extracting all data from accountinfo table
    d="select*from accountinfo where username='%s'"%(uname,)
    cursor.execute(d)
    data=cursor.fetchall()
    print()

    for i in data:
        print(' USER-NAME:-->',i[0])
        print('GENDER:-->',i[1])
        print('DOB:-->',i[2])
        print('MOBILE NUMBER:-->',i[3])
        print('PASSWORD:-->',i[4])
        
    
    con.close()
    print()



#function for viewing available trains between particular destination
def destination():

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    #TO show the list of destination with starting and end
    s="select beginning,end from trains;"
    cursor.execute(s)
    data=cursor.fetchall()
    print()

    for e in data:
        print(e)

    con.close()
    print()



#funtion to view list of avilable trains within particular destinations
def available():

    print()
    #asking user about destination he/she wanted travel from to make him/her find out required train

    start=input('Beginning Of Journy From--> ')
    end=input('Final Destination--> ')
    print('\n')

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    st="select train_no,train_name from trains where beginning='%s' and end='%s'"%(start,end,)
    cursor.execute(st)
    dat=cursor.fetchone()

    if dat==None:#if no train exist in table for entered destination
        print('Sorry!no trains available for this destination\n')
    else:#to display train no. and name of avilable train
        print('Train number and name of avilable train is\n')
        print(dat)
        print('\n')

    con.close()



#function for payment
def payment(trn,x,ts):

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    k=True
    while k:

            cd=input('enter your 16-digit debit card number-->')

            if len(cd)==16:
                    k=False
            else:
                    print('Please enter a valid debit card number')
                    k=True

    
            
        
    y="select price_perkm from reserve where trn=%s"%(trn)
    cursor.execute(y)
    dat=cursor.fetchone()

    for d in dat:
        f=d
    
    con.close()
    

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    z="select distance from trains where train_no=%s"%(trn)
    cursor.execute(z)
    data=cursor.fetchone()

    for i in data:
        h=i

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    cps="select %s from coachprice where trn2=%s"%(ts,trn)
    cursor.execute(cps)
    data=cursor.fetchone()

    for l in data:
        q=l
    
    a=(f*h*x)+q#calculating total cost
    print('Amount',a,'Have been deducted from your bank account\n')
    

    con.close()
    return a 



#to show validity of reservation
def rel():

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    x="select month(curdate())+1 ; "
    cursor.execute(x)
    data=cursor.fetchone()

    for i in data:
        l=i

    if l==13:
        ny="select year(curdate())+1;"
        cursor.execute(ny)
        data=cursor.fetchone()

        for c in data:
            y=c

        l=1

        cd="select curdate();"
        cursor.execute(cd)
        data=cursor.fetchone()

        for d in data:
            d=d

        print('Your reservation is valid upto',d,'/',l,'/',y,'\n')

    else:
        ny="select year(curdate());"
        cursor.execute(ny)
        data=cursor.fetchone()

        for c in data:
            y=c

        cd="select day(curdate());"
        cursor.execute(cd)
        data=cursor.fetchone()
        for d in data:
            d=d

        
        

        print('Your reservation is valid upto',d,'/',l,'/',y,'\n')


#function to cancel reservation
def canrev(uname):

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    trn=int(input('Enter The Train Number-->'))
    cs=input('Enter the coach from which you want to cancel reservation-->')
    z=int(input('Enter the number of seats you want cancel-->'))
    ts=cs+'p'
    
    ns="select reseats from canrev where uname='%s' and bogi='%s' and trnno=%s"%(uname,cs,trn,)
    cursor.execute(ns)
    data=cursor.fetchone()
    if data==None:#if no reservations are done
        print('\nsorry it seems that you have no bookings!\n')
        cx=input('Do you want to retry\n')
        if cx=='Y' or cx=='y':
             canrev(uname)
    else:    
        for i in data:
            c=i

            
    

   
        ur="update coach set %s=%s+%s where trn1=%s"%(cs,cs,c,trn,)
        cursor.execute(ur)
        con.commit()

        if z<c:
            cr="update canrev set reseats=reseats-%s where uname='%s' and trnno=%s and bogi='%s'"%(z,uname,trn,cs,)
            cursor.execute(cr)
            con.commit()

            print('\nYour reservation cancelled successfully for ',z,'seats\n')
            a=payment(trn,z,ts)
            print('\nAmount',a,'will be credited to your bankaccount within 3-4 working days \n')
        

        elif z==c:
            cr="delete from canrev where uname='%s' and trnno=%s and bogi='%s'"%(uname,trn,cs,)
            
            cursor.execute(cr)
            con.commit()

            print('\nYour reservation cancelled successfully for ',z,'seats\n')
            a=payment(trn,z,ts)
            print('\nAmount',a,'will be credited to your bankaccount within 3-4 working days \n')
        

        else:
            print('You dont have that much reserved seats!')

        


        con.close()



def viwr(uname):

    print('\n')

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()


    sr="select * from canrev where uname='%s'"%(uname,)
    cursor.execute(sr)
    data=cursor.fetchall()
    if data==None:
        print('\nYou do not have any reservations yet!\n')
    else:
        for i in data:
            print(i)
            print('\n')

    con.close()

    


#function to reserve the avilable seats in a particular train
def reserve(uname):

    trn=int(input('Enter The Train Number-->'))

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    print('Train coaches are-->\nA1,A2,B1,B2,S1,S2,S3,S4,GEN\n' )

    z=True
    while z:
        cs=input('Enter the coach in which you want to reserve seats-->')
        ts=cs+'p'
        if cs=='A1' or cs=='a1' or cs=='B1' or cs=='b1' or cs=='S1' or cs=='S2' or cs=='S3' or cs=='S4' or cs=='s1' or cs=='s2' or cs=='s3' or cs=='s4' or cs=='A2' or cs=='a2' or cs=='B2' or cs=='b2' or cs=='GEN' or cs=='gen':

            #obtaining the details of avilable seats in a particular train
    
            r="select %s from coach where trn1=%s"%(cs,trn,)
            cursor.execute(r)
            data=cursor.fetchone()

            #for knowing available sets
            if data==None:
                print('Sorry!Invalid train number\n')
            else:
                for e in data:
                    print("Total Number Of Available Seats Are=",e)

            x=int(input('Enter the total number of seats you want to reserve-->'))

            #checking is supplied parameter is valid or not
            if e<x:
                print('SORRY!This Much Seats Are Not Available\n')
            else:
               u="update coach set %s=%s-%s where trn1=%s"%(cs,cs,x,trn,)
               cursor.execute(u)
               con.commit()

               print('Now Proceed For Payment\n')
               
               payment(trn,x,ts)
               rel()
               z=False

        else:
            print('\nPlease select only avilable coach!\n')
            z=True

    check="select  bogi  from canrev where trnno=%s and bogi='%s'"%(trn,cs,)
    cursor.execute(check)
    data=cursor.fetchone()
    

    if data==None:
        cr="insert into canrev(uname,trnno,bogi,reseats)values('{}',{},'{}',{})".format(uname,trn,cs,x)
        cursor.execute(cr)
        con.commit()

        

    else:
        for j in data:
            d=j#to get values from tupple
        if d==cs:
        
            cd="update canrev set reseats=reseats+%s where uname='%s' and bogi='%s' and trnno=%s"%(x,uname,cs,trn)
            cursor.execute(cd)
            con.commit()
    

    con.close()



#function  to update profile details
def update(uname):

    print('field lists-->\n1.name\n2.gender\n3.dob\n4.mobile number\n5.password')
    cf=eval(input('Enter the number of field you want to update-->'))

    #for name correction
    if cf==1:
        con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
        cursor=con.cursor()
        
        cv=input('enter your corect name-->')
        st="update accountinfo set  username='{}' where username='{}'".format(cv,uname)
        cursor.execute(st)
        con.commit()
        print('\nprofile updated succesfully\n')
        con.close()
        return cv

    #for gender correction
    elif cf==2:
        con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
        cursor=con.cursor()
        
        cv=input('enter your corect gender -->')
        st="update accountinfo set  gender='{}' where username='{}'".format(cv,uname)
        cursor.execute(st)
        con.commit()
        print('\nprofile updated succesfully\n')
        con.close()
        return uname
        

    #for dob correction
    elif cf==3:
        con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
        cursor=con.cursor()
        
        cv=input('enter your corect dob-->')
        st="update accountinfo set  dob='{}' where username='{}'".format(cv,uname)
        cursor.execute(st)
        con.commit()
        print('\nprofile updated succesfully\n')
        con.close()
        return uname

    #for mobile number corrrection
    elif cf==4:
        con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
        cursor=con.cursor()
        
        cv=input('enter your corect mobile number-->')
        ci=int(cv)
        x="select mobile_number from accountinfo where mobile_number='%s'"%(ci,)
        cursor.execute(x)
        data=cursor.fetchone()
        
        if data==None:
            st="update accountinfo set  mobile_number='{}' where username='{}'".format(cv,uname)
            cursor.execute(st)
            con.commit()
            print('\nprofile updated succesfully\n')
        else:
            print('\nThe number already in use for some another account!\nPlease try with another number.\n')
        
        con.close()
        return uname

    #for changing password
    elif cf==5:
        con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
        cursor=con.cursor()
        
        cv=input('enter your new password-->')
        st="update accountinfo set  password='{}' where username='{}'".format(cv,uname)
        cursor.execute(st)
        con.commit()
        print('\nprofile updated succesfully\n')
        con.close()
        return uname#so that we can use display querry even after the correction of username

    

    else:
        print('\nPlease enter valid choice\n')
        update(uname)
        return uname #so that we can use display querry even after the correction of username

        



#function to remove user from logged in status
def logout():

        cho=input('Are You Sure You Want To Log Out Y/N!\n')

        if cho=='Y' or cho=="y":
            return False
        elif cho=='N' or cho=='n':
            return True
        else:
            print('please enter only Y/N!')
            logout()
            return False



#function for user to login if he\she already registered        
def login():

    uname=input('Enter Your Username here-->')
    pd=input('Enter Your Password Here -->')

    con=m.connect(host='localhost',user='root',passwd=sqpass,database='rtr',charset='utf8')
    cursor=con.cursor()

    #matching password on the basis of provided password
    x="select password from accountinfo where username='%s'"%(uname,)
    cursor.execute(x)
    data=cursor.fetchone()
    if data==None:
        print('USERNAME DOES NOT EXSIST!')
    else:
        y=True
        while y:
            for i in data:
                if pd==i:
                    #querries in logged in status
                    print('WELCOME TO OUR SOFTWARE\n')
                    print('PRESS 1 TO  SEE YOUR ACCOUNT DETAILS')
                    print('PRESS 2 TO  SEE THE LIST OF AVAIBLABLE DESTINATIONS')
                    print('PRESS 3 TO SEE THE LIST OF ALL AVAIBLABLE TRAINS')
                    print('PRESS 4 FOR SEAT RESERVATION')
                    print('PRESS 5 TO CORRECT AND UPDATE YOUR ACCOUNT DETAILS')
                    print('PRESS 6 FOR SEAT CANCEL')
                    print('PRESS 7 TO VIEW YOUR RESERVATION')
                    print('PRESS 8 TO EXIT')

                    p=input('Enter Your Choice -->')
                    if p.isnumeric():
                        p=int(p)
                    
                   
                        if p==1:
                            display(uname)

                        elif  p==2:
                            destination()
                        
                
                        elif  p==3:
                            available()

                        elif p==4:
                            reserve(uname)

                        elif p==5:
                            x=update(uname)
                            uname=x

                        elif p==6:
                            canrev(uname)

                        elif p==7:
                            viwr(uname)

                        elif p==8:
                            x=logout()
                        
                            if x==False:
                                print('LOGGED OUT SUCCESSFULLY')
                                y=False
                                
                            else:
                                y=True
                        else:
                            print('\nPlease enter only specified choice!\n')

                    else:
                            print('\nEnter valid choice!\n')

                else:
                    print('Sorry Something Went WRong!\nPlease Try Again')
                    login()

        con.close()
        
while True:
    ch=input('\nPress  Y/y to login\npress N/n to singup\npress E/e to exit software!\nPlease enter your choice-->')
    if ch=='Y' or ch=='y':
        login()
    elif ch=='N' or ch=='n':
        print('You can sign up here-->\n')
        print('Please fill the required detailes correctly\n')
        singup()
    elif ch=='E' or ch=='e':
        print('Good Bye have a nice day ................................................................................................................!')
        break
    else:
        print('please enter only Y/N!')

    
    
    
