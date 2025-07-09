import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import mysql.connector as sql_db
from datetime import datetime

conn = sql_db.connect(host="localhost",user="root",password="root")
if conn.is_connected():
    print("sucessfully connected")
    
crs=conn.cursor()
conn.cursor().execute("CREATE DATABASE if not exists CableTV")
print("Database Successfully Created")
conn.cursor().execute("USE CableTV")

conn.commit()
mycursor=conn.cursor()

while True:
    print("***********************************************************")
    print("***********Welcome To Cable TV Management System***********")
    print("1. New Connection")
    print("2. Update Channels")
    print("3. Recharge your Connection")
    print("4. Disconnect Connection")
    print("5. Analysis")
    print("6. Exit")

    print("---------------------------------")
    a_choice=int(input("Enter your choice: "))
    print("---------------------------------")
    
    if a_choice==1:
        print('*******************************************************')
        print("********************New Connection*********************")
        print("")
        print("Activation charges to be payed for HD Connection is Rs 1500/- (includes Service and Setup Box Charges)")
        print("Press 1 to Confirm")
        print("---------------------------------")
        b_choice=int(input("Enter your Choice: "))
        print("---------------------------------")
        if b_choice==1:
            import numpy as np
            print('***************************************************************************')
            print('Please Enter the Name and Address of the Customer for setting up the system')
            print('')
            Firstname=input("Enter First Name (without space) of the Customer: ")
            Lastname=input("Enter Last Name of the Customer: ")
            address=input("Address of the Customer: ")
            phone_no=input("Enter Customer's Phone Number: ")
            curr_day=datetime.now()
            tday=curr_day.strftime("%Y-%m-%d")
            print('')
            print('********************************************************************************************************')
            print('')
            i=np.random.randint(10000,99999)
            print("Your Connection_ID is: ",i)
            Name=Firstname+str(i)
            print("Here is the list of Channels which we are providing you with our Services")
            print("**********************************************************************************************")
            qry02=('create table if not exists '+Name+' (CHANNEL_NO int(3), CHANNEL_NAME varchar(50),PACKAGE varchar(50),LANGUAGE varchar(50),CHANNEL_PRICE int(20))')
            crs.execute(qry02)
            crs.execute("INSERT INTO "+Name+"   VALUES   (1,'Star Plus','Entertainment','Hindi',22)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (2,'Sony SET','Entertainment','Hindi',22)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (3,'Colors Infinity','Entertainment','English',11)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (4,'Surya Cinema','Movies','Telugu',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (5,'Zee Bollywood','Movies','Hindi',2)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (6,'HBO','Movies','English',13)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (7,'BBC News','News','English',3)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (8,'Aaj Tak','News','Hindi',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (9,'ABP News','News','Hindi',0)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (10,'India Today','News','English',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (11,'Star Sports Network','Sports','Multi',65)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (12,'Sony Sports Network','Sports','Multi',72)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (13,'Sports18','Sports','English',14)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (14,'Disney Channel','Kids','Multi',9)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (15,'Hungama Channel','Kids','Multi',7)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (16,'Cartoon Network','Kids','Multi',5)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (17,'B4U Music','Music','Hindi',0)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (18,'MTV Beats','Music','Multi',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (19,'Star Vijay Music','Music','Tamil',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (20,'Animal Planet','Infotainment','Multi',2)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (21,'Discovery Channel','Infotainment','Multi',5)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (22,'Nat Geo Wild','Infotainment','Multi',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (23,'GOD TV','Devotional','Multi',0)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (24,'Colors Bangla Cinema','Movies','Bengali',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (25,'CNBC Gujrati','News','Gujarati',1)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (26,'Sony Marathi','Entertainment','Marathi',5)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (27,'9X Tashan','Music','Punjab',0)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (28,'Sun TV','Movies','Tamil',22)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (29,'ETV Cinema','Movies','Telugu',7)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (30,'Udaya TV','Entertainment','Kannada',7)")
            crs.execute("INSERT INTO "+Name+"   VALUES   (31,'Asianet TV','Entertainment','Malayalam',22)")               
            qry50='select * from '+Name+';'
            mfd=pd.read_sql(qry50,conn)
            print(mfd)
            print("**********************************************************************************************")
            qry54='select sum(CHANNEL_PRICE) from '+Name+';'
            mfd1=pd.read_sql(qry54,conn)
            charges=mfd1.iat[0,0]
            print("Total Monthly charges including Fixed Charge of 100 Rs is ",charges+100)
            print("Please Note that you can remove unwanted channels from Update Channels option in Main Menu")
            print("Enter 1 to confirm: ")
            print("---------------------------------")
            c_choice=int(input("Enter your choice: "))
            print("---------------------------------")
            if c_choice==1:
                print("")
                print("Thank You For Registering")
                print("")
                print("------------------------------------------------------")
                print("CONFIRMATION...")
                print("Name: ",Firstname,Lastname)
                print("Your Connection ID: ",i)
                print("Your Registered Phone Number: ",phone_no)
                print("Address: ",address)
                print("Activation Charges: 1500/-")
                print("Registration Date: ",tday)
                print("------------------------------------------------------")
                print("")
                print("We Will Message You Shortly Regarding the Setup Details")
            else:
                print("You have entered an Invalid Input. Please Try Again")
            
        else:
            print("You have Entered an Invalid Input.")
            print("Please Try Again")
            
        Name2=Firstname,Lastname
        qry90=('create table if not exists customers(Customer_ID int(10),First_Name varchar(50),Last_Name varchar(50),Date date,Phone_No varchar(20),Address varchar(200), Monthly_Charges int(10))')
        crs.execute(qry90)
        crs.execute("Insert into customers values('"+str(i)+"','"+Firstname+"','"+Lastname+"','"+str(tday)+"','"+str(phone_no)+"','"+address+"','"+str(charges)+"');")
        conn.commit()    

       
    elif a_choice==2:
            print('******************************************************')
            print('*********************Update/Remove Channels*********************')
            print("1. View Channels and Updated Monthly Charges")
            print("2. Remove Channels")
            print("3. Add Channels")
            b_choice=int(input("Enter your Choice: "))
            import mysql.connector as msc
            mydb=msc.connect(host='localhost',user='root',passwd='root',database='Cabletv')
            crs=mydb.cursor()
            mydb.autocommit=True
            crs.execute("use Cabletv")
            firstname=input("Enter your First Name: ")
            c_id=input("Please Enter your Connection ID: ")
            name=firstname+c_id
            if b_choice==1:
                print("*********************************************************************************************")
                qry55='select * from '+name+';'
                view=pd.read_sql(qry55,conn)
                print(view)
                
            elif b_choice==2:
                   print("******************************************************************************************")
                   qry70='select * from '+name+';'
                   dis=pd.read_sql(qry70,conn)
                   print(dis)
                   print("******************************************************************************************")
                   s=int(input("Select the Number of Channels to remove: "))
                    
                   a=[]
                   for i in range(s):
                        remno=int(input("Enter the CHANNEL_NO of the channel to be removed: "))
                        a.append(i)             
                        crs.execute('DELETE FROM '+name+' WHERE CHANNEL_NO=(%s)',(remno,))    
                   print("")
                   print("Your selected Channels are Removed")
                   
            elif b_choice==3:
                   d=int(input("Enter new Channel's ID: "))
                   f=input("Enter Channel Name: ")
                   h=input("Enter the Category of Channel: ")
                   j=input("Enter the Language of Channel: ")
                   k=int(input("Enter the Price of Channel: "))
                   crs.execute("insert into "+name+" values('"+str(d)+"','"+f+"','"+h+"','"+j+"','"+str(k)+"');")
                   print("Successfully added")

            else:
                print("You have Entered an Invalid Input.")
                print("Please Try Again")

            print("--------------------------------------------------------------------")      
            qry54='select sum(CHANNEL_PRICE) from '+name+';'
            mfd1=pd.read_sql(qry54,conn)
            charges=mfd1.iat[0,0]
            mtcrg=charges+100
            print("Total Monthly charges including Fixed Charge of 100 Rs: ",mtcrg)
            print("--------------------------------------------------------------------")
            crs.execute('update customers set Monthly_Charges='+str(mtcrg)+' where Customer_ID='+c_id+';')
            conn.commit()
                
             
    elif a_choice==3:
        print("**************Recharge a Connection***************")
        cust_id=int(input("Enter your Customer ID: "))
        f_name=str(input("Enter the First Name of the Customer: "))
        price=int(input("Enter the Amount to be paid: "))
        phone_no=int(input("Enter Customer phone no : "))
        conn.cursor().execute('create table if not exists customer_table(Customer_ID int(10),Customer_Name varchar(60),Phone_No varchar(20),Amount_Payed int(10) )')
        SQL_insert="insert into customer_table values('"+str(cust_id)+"','"+f_name+"','"+str(phone_no)+"','"+str(price)+"');"
        crs.execute(SQL_insert)
        conn.commit()
        print("You have Successfully Paid your Bill")
        print("Bill Recorded")

    elif a_choice==4:
        print("******************Disconnect a Connection*************************")
        import mysql.connector as msc
        mydb=msc.connect(host='localhost',user='root',passwd='root',database='Cabletv')
        crs=mydb.cursor()
        mydb.autocommit=True
        crs.execute("use Cabletv")
        nam=input("Enter Your First Name: ")                                                     
        di=int(input("Enter Your Connection ID: "))
        p=nam+str(di)
        s=input("Are you sure you want to Disconnect the Connection (YES/NO): ")
        a=[]
        for i in s:
            a.append(i)        
        
        if len(s)==3: 
           crs.execute('DELETE FROM customers WHERE CUSTOMER_ID=(%s) or First_Name=(%s)',(di,nam,))
           crs.execute('drop table '+p+';')
        
        else:
             print("Connection NOT Disconnected")
             
        print("")
        print("Your Connection is Disconnected")
        



    elif a_choice==5:
        print("**********Analysis****************")
        import matplotlib.pyplot as plt
        print("1. Table")
        print("2. Graph")
        print("")
        print("---------------------------------")
        g_choice=int(input("Enter your choice: "))
        print("---------------------------------")
        if g_choice==1:
            print("1. Customer Table")
            print("2. Monthly Recharge Table")
            print("---------------------------------")
            h_choice=int(input("Enter your Choice: "))
            print("---------------------------------")
            if h_choice==1:
                print("*************************************************************************")
                qry22='select * from customers;'
                mdd=pd.read_sql(qry22,conn)
                pd.set_option('display.width',None)
                print(mdd)
                print("*************************************************************************")
            elif h_choice==2:
                print("*************************************************************************")
                qry23='select * from customer_table;'
                mdu=pd.read_sql(qry23,conn)
                print(mdu)
                print("*************************************************************************")
            else:
                print("You have Entered an Invalid Input.")
                print("Please Try Again")

        elif g_choice==2:
            print("1. Monthly New Connections Graph")
            print("---------------------------------")
            j_choice=int(input("Enter your Choice: "))
            print("---------------------------------")
            if j_choice==1:
                qry24="select count(*) from customers where Date>'2023-06-01' and Date<'2023-06-31';"
                crs.execute(qry24)
                u=crs.fetchone()
                l=list(u)
                qry25="select count(*) from customers where Date>'2023-07-01' and Date<'2023-07-31';"
                crs.execute(qry25)
                v=crs.fetchone()
                l2=list(v)
                qry26="select count(*) from customers where Date>'2023-08-01' and Date<'2023-08-30';"
                crs.execute(qry26)
                w=crs.fetchone()
                l3=list(w)
                qry27="select count(*) from customers where Date>'2023-09-01' and Date<'2023-09-31';"
                crs.execute(qry27)
                x=crs.fetchone()
                l4=list(x)
                lst=l+l2+l3+l4
                n=['June','July','August','September']
                plt.bar(n,lst,width=0.50,color=['red','b','g','cyan'])
                plt.xlabel("Months")
                plt.ylabel("No of New Connections")
                plt.show()

            else:
                print("You have Entered an Invalid Input.")
                print("Please Try Again")

        else:
            print("You have Entered an Invalid Input.")
            print("Please Try Again")
                
    elif a_choice==6:
        print("End")
        break
    
    else:
        print("************************************")
        print("You have Entered an Invalid Input.")
        print("Please Try Again")
            









