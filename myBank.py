password = 'fg3*d12'
username = 'admin'
user = input('Enter the user name :')
passw = input('Enter the password :')
if user.lower() == username and passw == password:
    import mysql.connector as sqlcon

    mycon, cur = None, None


    def connection():
        global mycon, cur
        mycon = sqlcon.connect(host='localhost', user='root', passwd='fg3*d12', database='bank')
        if mycon.is_connected():
            print('connected to mysql')
        else:
            print('not connected to mysql')
            return
        cur = mycon.cursor()


    connection()

    TABLE_NAME1 = "bank1"
    TABLE_NAME2 = "bank2"
    TABLE_NAME3 = "bank3"
    TABLE_NAME4 = "bank4"
    A_No = "A_No"
    Name = "Name"
    DOB = "DOB"
    Nat = "Nationality"
    POB = "POB"
    Phn_No = "Phone_No"
    A_ID = "A_ID"
    Occ = "Occupation"
    Bal = "Balance"
    Sal = "Salary"
    T_A = "T_A"
    B_C = "B_Code"
    DOE = "DOE"
    Adrs = "Address"
    Emp = "Employees"
    Con_No = "Contact_No"
    Amt = "Amount_left"
    nPay = "No_of_Payments"
    Payl = "Payments_left"
    M_P = "Monthly_Payment"
    Dt = "_Date_"

    qs = '''CREATE TABLE IF NOT EXISTS
             bank1 (A_No int(6) unique primary key not null,Name varchar(20) not null ,DOB date not null ,
             Nationality varchar(20) not null,POB int(10) not null ,Phone_No int(20) not null);'''
    cur.execute(qs)
    qs = '''CREATE TABLE IF NOT EXISTS
             bank2 (A_No int(6) unique primary key not null,A_ID int(10) unique not null ,
             Occupation varchar(25) not null ,Salary int(6) not null,Balance int(6) not null,T_A int(6));'''
    cur.execute(qs)
    qs = '''CREATE TABLE IF NOT EXISTS
             bank3 (B_Code varchar(25) unique not null,DOE date not null,Address varchar(25) not null,
             Contact_No int(20) not null,Employees int(6) not null);'''
    cur.execute(qs)
    qs = '''CREATE TABLE IF NOT EXISTS
             bank4 (A_No int(6) unique primary key not null,Amount_left int(6) not null,No_of_Payments int(6) not null,
             Payments_left int(6) not null,Monthly_Payment int(6) not null,_Date_ date not null);'''
    cur.execute(qs)


    def add_account():
        A_No = int(input('Enter the Account Number :'))
        Name = input('Enter the Account Name :').upper()
        DOB = input('Enter the Date of Birth (yyyy/mm/dd) :')
        Nat = input('Enter the Nationality :').upper()
        POB = int(input('Enter the P.O. Box Number :'))
        Phn_No = int(input('Enter the Phone Number :'))
        A_ID = int(input('Enter the Account ID :'))
        Occ = input('Enter the Occupation:').upper()
        Sal = int(input('Enter the Monthly Salary :'))
        Bal = int(input('Enter Initial Deposit (greater than 3000) :'))
        if int(Bal) > 3000:
            qs = '''insert into bank1(A_No,Name,DOB,Nationality,POB,Phone_No)
                     values({},'{}','{}','{}',{},{});'''.format(A_No, Name, DOB, Nat, POB, Phn_No)
            cur.execute(qs)
            mycon.commit()
            qs = '''insert into bank2(A_No,A_ID,Occupation,Balance,Salary)
                     values({},{},'{}',{},{});'''.format(A_No, A_ID, Occ, Bal, Sal)
            cur.execute(qs)
            mycon.commit()
            qs = '''update bank2 set T_A=0;'''
            cur.execute(qs)
            mycon.commit()
            print('the Account has been created')
        else:
            print('not sufficient Initial Deposit')
            print('the Account is not created')


    def account_info():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the given Account does not Exist')
        else:
            qs = '''select * from bank1
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            data = cur.fetchall()
            head = '''\
+------+--------------------+----------+--------------------+----------+--------------------+
| A_No | Name               | DOB      | Nationality        | POB      | Phone_No           |
+------+--------------------+----------+--------------------+----------+--------------------+'''
            body = '''\
|%6d|%20s|%10s|%20s|%10d|%20d|
+------+--------------------+----------+--------------------+----------+--------------------+'''
            print(head)
            for row in data:
                print(body % (row[0], row[1][0:20], str(row[2])[0:10], row[3][0:20], row[4], row[5]))
                qs = '''select * from bank2 where A_No={}'''.format(A_No)
                cur.execute(qs)
                data = cur.fetchall()
                head = '''\
+------+----------+-------------------------+----------+----------+----------+
| A_No |   A_ID   |        Occupation       |  Salary  |  Balance |   T_A    |
+------+----------+-------------------------+----------+----------+----------+'''
                body = '''\
|%6d|%10d|%25s|%10d|%10d|%10d|
+------+----------+-------------------------+----------+----------+----------+'''
                print(head)
                for row in data:
                    print(body % (row[0], row[1], str(row[2])[0:25], row[3], row[4], row[5]))


    def display_accounts():
        qs = '''select * from bank4 order by A_No;'''
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('No Data Found')
        else:
            qs = '''select * from bank1 order by A_No asc;'''
            cur.execute(qs)
            data = cur.fetchall()
            head = '''\
    +------+--------------------+----------+--------------------+----------+--------------------+
    | A_No | Name               | DOB      | Nationality        | POB      | Phone_No           |
    +------+--------------------+----------+--------------------+----------+--------------------+'''
            body = '''\
    |%6d|%20s|%10s|%20s|%10d|%20d|
    +------+--------------------+----------+--------------------+----------+--------------------+'''
            print(head)
            for row in data:
                print(body % (row[0], row[1][0:20], str(row[2])[0:10], row[3][0:20], row[4], row[5]))

            qs = '''select * from bank2 order by A_No asc;'''
            cur.execute(qs)
            data = cur.fetchall()
            head = '''\
    +------+----------+-------------------------+----------+----------+----------+
    | A_No |   A_ID   |        Occupation       |  Salary  |  Balance |   T_A    |
    +------+----------+-------------------------+----------+----------+----------+'''
            body = '''\
    |%6d|%10d|%25s|%10d|%10d|%10d|
    +------+----------+-------------------------+----------+----------+----------+'''
            print(head)
            for row in data:
                print(body % (row[0], row[1], str(row[2])[0:25], row[3], row[4], row[5]))


    def delete_account():
        A_No = int(input('Enter the Account Number to be deleted :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the given Account does not Exist')
        else:
            qs = '''select * from bank4
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            data = cur.fetchall()
            n = cur.rowcount
            if n == 0:
                qs = '''delete from bank1
                         where A_No={};'''.format(A_No)
                cur.execute(qs)
                mycon.commit()
                qs = '''delete from bank2
                         where A_No={};'''.format(A_No)
                cur.execute(qs)
                mycon.commit()
                print('the Account is deleted')
            else:
                print('The Loan has to be cleared before deleting the account')


    def balance():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank2
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the given Account does not Exist')
        else:
            qs = '''select * from bank2
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            data = cur.fetchall()
            for row in data:
                print('Current Balance :', row[4])


    def deposit():
        global Bal, A_No
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank2
                 where A_No={}'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the given Account does not Exist')
        else:
            T_A = int(input('Enter the amount to be deposited :'))
            qs = '''update bank2 set T_A={}
                      where A_No={};'''.format(T_A, A_No)
            cur.execute(qs)
            mycon.commit()
            qs = '''update bank2 set Balance=Balance+T_A
                      where A_No={};'''.format(A_No)
            cur.execute(qs)
            mycon.commit()
            qs = '''update bank2 set T_A=0
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            mycon.commit()
            print('the amount has been deposited')


    def withdraw():
        global Bal, A_No
        A_No = int(input('Enter the Account Number :'))
        qs = '''select Balance from bank2
                 where A_No={}'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the given Account does not Exist')
        else:
            T_A = int(input('Enter the amount to be withdrawn :'))
            if str(T_A) > Bal:
                print('not enough Balance in the Account')
            else:
                qs = '''update bank2 set T_A={}
                          where A_No={};'''.format(T_A, A_No)
                cur.execute(qs)
                mycon.commit()
                qs = '''update bank2 set Balance=Balance-T_A
                          where A_No={};'''.format(A_No)
                cur.execute(qs)
                mycon.commit()
                qs = '''update bank2 set T_A=0
                         where A_No={};'''.format(A_No)
                cur.execute(qs)
                mycon.commit()
                print('the amount has been withdrawn')


    def transfer():
        global Bal, A_No
        ID1 = int(input('Enter the Account Number of the Sender :'))
        qs = '''select * from bank2 where A_No={};'''.format(ID1)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given account does not exist')
        else:
            ID2 = int(input('Enter the Account Number of the Recepient :'))
            qs = '''select * from bank2
                     where A_No={};'''.format(ID2)
            cur.execute(qs)
            data = cur.fetchall()
            n = cur.rowcount
            if n == 0:
                print('The given Account does not Exist')
            else:
                T_A = int(input('Enter the amount to be transferred :'))
                bal1 = '''select * from bank2
                            where A_No={};'''.format(ID1)
                if str(T_A) > Bal:
                    print('not enough balance in the Account')
                else:
                    qs = '''update bank2 set T_A={};'''.format(T_A)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''update bank2 set Balance=Balance-T_A
                             where A_No={};'''.format(ID1)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''update bank2 set Balance=Balance+T_A
                             where A_No={};'''.format(ID2)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''update bank2 set T_A=0
                             where A_No={};'''.format(ID1)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''update bank2 set T_A=0
                             where A_No={};'''.format(ID2)
                    cur.execute(qs)
                    mycon.commit()
                    print('the amount has been transferred')


    def m_pob():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given Account does not Exist')
        else:
            POB = int(input('Enter the new P.O. Box Number :'))
            qs = '''update bank1 set POB={}
                     where A_No={};'''.format(POB, A_No)
            cur.execute(qs)
            mycon.commit()
            print('the P.O. Box Number has been modified')


    def m_phn():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given Account does not Exist')
        else:
            Phn_No = int(input('Enter the new Phone Number :'))
            qs = '''update bank1 set Phone_No={}
                     where A_No={};'''.format(Phn_No, A_No)
            cur.execute(qs)
            mycon.commit()
            print('the Phone Number has been modified')


    def m_occ():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank2
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given Account does not Exist')
        else:
            Occ = (input('Enter the  new Occupation :')).upper()
            qs = '''update bank2 set Occupation='{}'
                     where A_No={};'''.format(Occ, A_No)
            cur.execute(qs)
            mycon.commit()
            print('the Occupation has been modified')


    def m_sal():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank2
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given Account does not Exist')
        else:
            Sal = int(input('Enter the new Salary :'))
            qs = '''update bank2 set Salary={}
                     where A_No={};'''.format(Sal, A_No)
            cur.execute(qs)
            mycon.commit()
            print('the Salary has been modified')


    def add_branch():
        B_C = input('Enter the Branch Code :')
        DOE = input('Enter the Date of Establishment of the branch (yyyy/mm/dd) :')
        Adrs = input('Enter the Address of the branch :').upper()
        Con_No = int(input('Enter the Contact Number of the branch :'))
        Emp = int(input('Enter the no of employees :'))
        qs = '''insert into bank3(B_Code,DOE,Address,Contact_No,Employees)
                 values('{}','{}','{}',{},{});'''.format(B_C, DOE, Adrs, Con_No, Emp)
        cur.execute(qs)
        mycon.commit()
        print('the Branch has been registered')


    def branch_info():
        B_C = input('Enter the Branch Code :')
        qs = '''select * from bank3
                 where B_Code='{}';'''.format(B_C)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the Branch Code does not Exist')
        else:
            qs = '''select * from bank3
                     where B_Code='{}';'''.format(B_C)
            cur.execute(qs)
            data = cur.fetchall()
            head = '''\
+-------------------------+----------+-------------------------+--------------------+---------+
|        B_Code           |   DOE    |         Address         |     Contact_No     |Employees|
+-------------------------+----------+-------------------------+--------------------+---------+
'''
            body = '''\
|%25s|%10s|%25s|%20d|%9d|
+-------------------------+----------+-------------------------+--------------------+---------+
'''
            print(head)
            for row in data:
                print(body % (row[0], row[1], row[2], row[3], row[4]))


    def display_branches():
        qs = '''select * from bank3 order by B_Code'''
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('No Data Found')
        else:
            qs = '''select * from bank3 order by B_Code'''
            cur.execute(qs)
            data = cur.fetchall()
            head = '''\
+-------------------------+----------+-------------------------+--------------------+---------+
|        B_Code           |   DOE    |         Address         |     Contact_No     |Employees|
+-------------------------+----------+-------------------------+--------------------+---------+
'''
            body = '''\
|%25s|%10s|%25s|%20d|%9d|
+-------------------------+----------+-------------------------+--------------------+---------+
'''
            print(head)
            for row in data:
                print(body % (row[0], row[1], row[2], row[3], row[4]))


    def delete_branch():
        B_C = input('Enter the Branch Code to be deleted :')
        qs = '''select * from bank3
                 where B_Code='{}';'''.format(B_C)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the Branch Code does not Exist')
        else:
            qs = '''delete from bank3
                     where B_Code='{}';'''.format(B_C)
            cur.execute(qs)
            mycon.commit()
            print('the Branch Information has been deleted')


    def m_emp():
        B_C = input('Enter the Branch Code :')
        qs = '''select * from bank3
                 where B_Code='{}';'''.format(B_C)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the Branch Code does not Exist')
        else:
            Emp = (input('Enter the  latest Number of Employees working in the branch :'))
            qs = '''update bank3 set Employees={}
                     where B_Code='{}';'''.format(Emp, B_C)
            cur.execute(qs)
            mycon.commit()
            print('the Number of Employees has been modified')


    def m_con():
        B_C = input('Enter the Branch Code :')
        qs = '''select * from bank3
                 where B_Code='{}';'''.format(B_C)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the Branch Code does not Exist')
        else:
            Con_No = int(input('Enter the new Contact Number of the branch :'))
            qs = '''update bank3 set Contact_No={}
                     where B_Code='{}';'''.format(Con_No, B_C)
            cur.execute(qs)
            mycon.commit()
            print('the Contact Number has been modified')


    def loan():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('The given Account does not Exist')
        else:
            qs = '''select * from bank4
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            data = cur.fetchall()
            n = cur.rowcount
            if n == 0:
                Amt = int(input('Enter the Amount to be recieved as Loan at the annual interest rate of 8% :'))
                Yrs = int(input('Enter the number of years of repayement (1 to 6) :'))
                Dt = input('Enter the Date at which the Loan was taken:')
                if 1 <= int(Yrs) <= 6:
                    nPay = int(Yrs) * 12
                    M_P = int(Amt * (8 / 12) / nPay + (Amt / nPay))
                    qs = '''update bank2
                             set Balance=Balance+{};'''.format(Amt)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''insert into bank4(A_No,Amount_left,No_of_Payments,Payments_left,Monthly_Payment,_Date_)
                             values ({},{},{},{},{},'{}');'''.format(A_No, Amt, nPay, nPay, M_P, Dt)
                    cur.execute(qs)
                    mycon.commit()
                    print('Loan has been granted')
                else:
                    print('Wrong input to Number of Years of repayment')
            elif n > 0 and n < 4:
                Amt = int(input('Enter the Amount to be recieved as Loan at the annual interest rate of 8% :'))
                Yrs = int(input('Enter the number of years of repayement (1 to 4) :'))
                if 1 <= int(Yrs) <= 4:
                    nPay = int(Yrs) * 12
                    M_P = int(Amt * (8 / 12) / nPay + (Amt / nPay))
                    qs = '''update bank2
                             set Balance=Balance+{};'''.format(Amt)
                    cur.execute(qs)
                    mycon.commit()
                    qs = '''update bank4 set Amount_left=Amount_left+{} , No_of_Payments=No_of_Payments+{} ,
                             Payments_left=Payments_left+{},Monthly_Payment=Monthly_Payment+{}
                             where A_No={};'''.format(Amt, nPay, nPay, M_P, A_No)
                    cur.execute(qs)
                    mycon.commit()
                    print('Loan has been granted')
                else:
                    print('Wrong input to Number of Years of repayment')
            else:
                print('You have reached the limit of your loan')
                print('Loan is denied until you clear your previous loans')


    def loan_account_info():
        A_No = int(input('Enter the Account Number :'))
        qs = '''select * from bank1
                 where A_No={};'''.format(A_No)
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('the Account does not exist')
        else:
            qs = '''select * from bank4
                     where A_No={};'''.format(A_No)
            cur.execute(qs)
            data = cur.fetchall()
            n = cur.rowcount
            if n == 0:
                print('Currently no Loan taken by the Account Holder')
                print('Hence Account not found in the list')
            else:
                qs = '''select * from bank4
                         where A_No={};'''.format(A_No)
                cur.execute(qs)
                data = cur.fetchall()
                head = '''/
+------+-----------+--------------+-------------+---------------+
| A_No |Amount_left|No_of_Payments|Payments_left|Monthly_Payment|
+------+-----------+--------------+-------------+---------------+'''
                body = '''/
|%6d|%11d|%14d|%13d|%15d|
+------+-----------+--------------+-------------+---------------+'''
                print(head)
                for row in data:
                    print(body % (row[0], row[1], row[2], row[3], row[4]))


    def loan_display_all():
        qs = '''select * from bank4 order by A_No;'''
        cur.execute(qs)
        data = cur.fetchall()
        n = cur.rowcount
        if n == 0:
            print('No Data Found')
        else:
            qs = '''select * from bank4 order by A_No'''
            cur.execute(qs)
            data = cur.fetchall()
            head = '''/
+------+-----------+--------------+-------------+---------------+
| A_No |Amount_left|No_of_Payments|Payments_left|Monthly_Payment|
+------+-----------+--------------+-------------+---------------+'''
            body = '''/
|%6d|%11d|%14d|%13d|%15d|
+------+-----------+--------------+-------------+---------------+'''
            print(head)
            for row in data:
                print(body % (row[0], row[1], row[2], row[3], row[4]))


    def loan_delete():
        qs = '''delete from bank4
                 where Amount_left=0;'''
        cur.execute(qs)
        mycon.commit()


    loan_delete()


    def loan_repayment():
        import datetime
        x = datetime.date.today()
        if x.day == 1:
            qs = '''select * from bank4 order by A_No;'''
            cur.execute(qs)
            data = cur.fetchall()
            n = cur.rowcount
            if n == 0:
                pass
            else:
                qs = '''update bank2 set
                         Balance=Balance-(select Monthly_Payment from bank2 where Loan=Y) where Loan=Y;'''
                cur.execute(qs)
                mycon.commit()


    loan_repayment()

    BANKmenu = '''
                  BANK MENU
    ----------------------------------------
    1.ADD ACCOUNT
    2.ACCOUNT INFORMATION
    3.MODIFY ACCOUNT INFORMATION
    4.DISPLAY ALL ACCOUNTS 
    5.DELETE ACCOUNT
    6.ATM FUNCTIONS
    7.LOAN
    8.BRANCH MENU
    9.EXIT MENU                     '''

    ATMmenu = '''
              ATM MENU
    --------------------------------
    1.CHECK BALANCE
    2.WITHDRAW MONEY
    3.DEPOSIT MONEY
    4.TRANSFER MONEY
    5.BACK                                   '''

    MODIFYmenu = '''
           MODIFY MENU
    --------------------------------
    1.MODIFY P.O. BOX NUMBER
    2.MODIFY PHONE NUMBER
    3.MODIFY OCCUPATION
    4.MODIFY SALARY
    5.BACK                                    '''

    BRANCHmenu = '''
            BRANCH MENU
    --------------------------------
    1.ADD BRANCH
    2.BRANCH INFORMATION
    3.MODIFY BRANCH INFORMATION
    4.DISPLAY BRANCHES
    5.DELETE BRANCH
    6.BACK                                     '''

    MODmenu = '''
             MODIFY MENU
    ---------------------------------
    1.MODIFY NUMBER OF EMPLOYEES
    2.MODIFY CONTACT NUMBER
    3.BACK                                       '''

    LOANmenu = '''
             LOAN MENU
    ----------------------------------
    1.LOAN APPLICANT
    2.ACCOUNT INFORMATION
    3.DISPLAY ALL ACCOUNTS
    4.BACK                                         '''

    while True:
        print(BANKmenu)
        choice = int(input('Enter your choice from 1 to 9 :'))
        if choice == 1:
            add_account()
        elif choice == 2:
            account_info()
        elif choice == 3:
            while True:
                print(MODIFYmenu)
                choice = int(input('Enter your choice from 1 to 5 :'))
                if choice == 1:
                    m_pob()
                elif choice == 2:
                    m_phn()
                elif choice == 3:
                    m_occ()
                elif choice == 4:
                    m_sal()
                elif choice == 5:
                    break
                else:
                    print('wrong choice')
        elif choice == 4:
            display_accounts()
        elif choice == 5:
            delete_account()
        elif choice == 6:
            while True:
                print(ATMmenu)
                choice = int(input('Enter your choice from 1 to 5 :'))
                if choice == 1:
                    balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    transfer()
                elif choice == 5:
                    break
                else:
                    print('wrong choice')
        elif choice == 7:
            while True:
                print(LOANmenu)
                choice = int(input('Enter your choice from 1 to 4 :'))
                if choice == 1:
                    loan()
                elif choice == 2:
                    loan_account_info()
                elif choice == 3:
                    loan_display_all()
                elif choice == 4:
                    break
                else:
                    print('wrong choice')
        elif choice == 8:
            while True:
                print(BRANCHmenu)
                choice = int(input('Enter your choice from 1 to 6 :'))
                if choice == 1:
                    add_branch()
                elif choice == 2:
                    branch_info()
                elif choice == 3:
                    while True:
                        print(MODmenu)
                        choice = int(input('Enter your choice from 1 to 3 :'))
                        if choice == 1:
                            m_emp()
                        elif choice == 2:
                            m_con()
                        elif choice == 3:
                            break
                        else:
                            print('wrong choice')
                elif choice == 4:
                    display_branches()
                elif choice == 5:
                    delete_branch()
                elif choice == 6:
                    break
                else:
                    print('wrong choice')
        elif choice == 9:
            break
        else:
            print('wrong choice')
    mycon.close()

else:
    print('wrong username or password')