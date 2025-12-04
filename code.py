print("""
                              =============================================            
                                        
                                       WELCOME TO GYM MANAGEMENT  

                              =============================================
    """)
import mysql.connector as s
con=s.connect(host="localhost",user="root",password="lovely")
cur=con.cursor()
cur.execute("create database if not exists gym")
cur.execute("use gym")
cur.execute("create table if not exists login(username varchar(25) not null, password varchar(25) not null)")
cur.execute("create table if not exists sno(id int not null, did int not null)")
cur.execute("create table if not exists trainer(id int not null, name varchar(25) not null, age varchar(20) not null, gender char(2) not null, salary int)")
cur.execute("create table if not exists member(id int not null, name varchar(25) not null, gender char(2) not null, category varchar(25), amt int)")
cur.execute("create table if not exists fees(silver int not null, gold int not null, platinum int not null)")
con.commit()
cur.execute("select * from login")
x=0
for i in cur:
    x=1
if x==0:
    cur.execute("insert into login values('admin2024','10293847')")
    con.commit()
x=0
cur.execute("select * from sno")
for i in cur:
    x=1
if x==0:
    cur.execute("insert into sno values(0,0)")
    con.commit()
x=0
cur.execute("select * from fees")
for i in cur:
    x=1
if x==0:
    cur.execute("insert into fees values(175,300,450)")
    con.commit()
while True:
    print('''
1.Login
2.Exit''')
    ch=int(input("Enter your Choice: "))
    if ch==1:
        password=input("Enter your Password: ")
        cur.execute("select * from login")
        for i in cur:
            t_user,t_passwrd=i
        if t_passwrd==password:
            print('''
1.Add Trainer
2.Add Member
3.Remove Trainer
4.Remove Member
5.Modify
6.Change Password
7.BACK
''')
            ch=int(input("Enter your Choice: "))
            if ch==1:
                name=input("Enter Name: ")
                age=input("Enter Age: ")
                gender=input("Enter Gender(M/F): ")
                sal=int(input("Enter Salary: "))
                cur.execute("select * from sno")
                for i in cur:
                    t_id,t_did=i
                t_id+=1
                query="insert into trainer values ({},'{}','{}','{}',{})".format(t_id,name,age,gender,sal)
                cur.execute(query)
                query="update sno set id={}".format(t_id)
                cur.execute(query)
                con.commit()
                print("...DONE...")
                print("Trainers New ID=",t_id)
                           
            elif ch==2:
                name=input("Enter Name")
                gender=input("Enter Gender (M/F)")
                print('''
Which Category would you like to take?
1.Silver -> 175sr per month
2.Gold -> 300sr per month
3.Platinum -> 450sr per month''')
                ch=int(input("Entrer your Choice: "))
                cur.execute("select * from fees")
                for i in cur:
                    t_silver,t_gold,t_platinum=i
                if ch==1:
                    category='silver'
                    amount=t_silver    
                elif ch==2:
                    category='gold'
                    amount=t_gold
                elif ch==3:
                    category='platinum'
                    amount=t_platinum
                cur.execute("select * from sno")
                for i in cur:
                    t_id,t_did=i
                t_did+=1
                query="insert into member values ({},'{}','{}','{}',{}) ".format(t_did,name,gender,category,amount)
                cur.execute(query)
                query="update sno set did={}".format(t_did)
                cur.execute(query)
                con.commit()
                print("...DONE...")
                print("Members New ID=",t_did)
                
            elif ch==3:
                del_id=int(input("Enter the ID to Remove"))
                cur.execute("select * from trainer")
                x=0
                for i in cur:
                    t_id=i[0]
                    if t_id==del_id:
                        x=1
                if x==1:
                    query="delete from trainer where id={}".format(del_id)
                    cur.execute(query)
                    con.commit()
                    print('...DONE...')
                else:
                    print("ID not Valid")
                    
            elif ch==4:
                del_id=int(input("Enter the ID to Remove"))
                cur.execute("select * from member")
                x=0
                for i in cur:
                    m_id=i[0]
                    if m_id==del_id:
                        x=1
                if x==1:
                    query="delete from member where id={}".format(del_id)
                    cur.execute(query)
                    con.commit()
                    print('...DONE...')
                else:
                    print("ID not Valid")
            elif ch==5:
                z=10
                while z==10:
                    print('''
1.Modify Gym Category
2.Modify Trainers info
3.Modify Members info
4.BACK''')
                    ch=int(input("Enter your Choice"))
                    if ch==1:
                        print('''
Category to Modify;

1.SILVER
2.GOLD
3.PLATINUM''')
                        ch2=int(input("Enter your Choice: "))
                        amount=int(input("Enter new amount per month to update"))
                        if ch2==1:
                            query="update fees set silver={}".format(amount)
                            cur.execute(query)
                            con.commit()
                            print('...DONE...')
                        elif ch2==2:
                            query="update fees set gold={}".format(amount)
                            cur.execute(query)
                            con.commit()
                            print('...DONE...')
                        elif ch2==3:
                            query="update fees set platinum={}".format(amount)
                            cur.execute(query)
                            con.commit()
                            print('...DONE...')
                            
                    elif ch==2:
                        idd=int(input("Enter trainer ID to modify: "))
                        cur.execute("select * from trainer")
                        x=0
                        for i in cur:
                            t_id=i[0]
                            if t_id==idd:
                                x=1
                        if x==1:
                            print('''
Data to Modify;

1.NAME
2.AGE
3.GENDER
4.SALARY''')
                            ch=int(input("Enter your Choice"))
                            if ch==1:
                                new_name=input("Enter New Name to Modify")
                                query="update trainer set name='{}' where id={}".format(new_name,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                            elif ch==2:
                                new_age=input("Enter New Age to Modify")
                                query="update trainer set age='{}' where id={}".format(new_age,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                            elif ch==3:
                                new_gender=input("Enter New Gender to Modify(M/F)")
                                query="update trainer set gender='{}' where id={}".format(new_gender,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                            elif ch==4:
                                new_sal=input("Enter New Salary to Modify")
                                query="update trainer set salary={} where id={}".format(new_sal,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                        else:
                                print('ID not Valid')
                    elif ch==3:
                        idd=int(input("Enter members ID to modify: "))
                        cur.execute("select * from member")
                        x=0
                        for i in cur:
                            m_id=i[0]
                            if m_id==idd:
                                 x=1
                        if x==1:
                            print('''
Data to Modify;  
1.NAME
2.GENDER
3.CATEGORY''')
                            ch2=int(input("Enter your Choice"))
                            if ch2==1:
                                new_name=input("Enter New Name to Modify")
                                query="update member set name='{}' where id={}".format(new_name,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                            elif ch2==2:
                                new_gender=input("Enter New Gender to Modify(M/F)")
                                query="update member set gender='{}' where id={}".format(new_gender,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                            elif ch2==3:
                                print('''
Category to Modify;

1.SILVER
2.GOLD
3.PLATINUM''')
                                cur.execute("select * from fees")
                                for i in cur:
                                    t_silver,t_gold,t_platinum=i
                                ch3=int(input("Enter your Choice: "))
                                if ch3==1:
                                    category="silver"
                                    amt=t_silver
                                elif ch3==2:
                                    category="gold"
                                    amt=t_gold
                                elif ch3==3:
                                    category="platinum"
                                    amt=t_platinum
                                query="update member set category='{}', amt={} where id={}".format(category,amt,idd)
                                cur.execute(query)
                                con.commit()
                                print("...DONE...")
                        else:
                            print('ID not Valid')

                    elif ch==4:
                        break

            elif ch==6:
                passwrd=input("Enter the Old Password: ")
                cur.execute("select * from login")
                for row in cur:
                    t_user,t_passwrd = row
                if t_passwrd==passwrd:
                    new_pass=input("Enter the New Password: ")
                    query="update login set password='{}'".format(new_pass)
                    cur.execute(query)
                    con.commit()
                    print('...DONE...')
                else:
                    print("Password not Valid")
                
            elif ch==7:
                break
        else:
           print("Wrong Password")
    elif ch==2:
        break 
