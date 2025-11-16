'''
Author : Ali Pilehvar Meibody
Date : 2025/11/15

----BANK MANAGEMENT PROJECT------

---> systemi besazim ke infrustructure --> zirsakht

Karmande bank ---> Panel --> hamechio barash neshon mide
moshtari --> va b karmande bank--> baray eman hesab banki doros ko



PANEL --> oon karmande bank ro doros konim (Project1)



Optional Project (ATM)--> moshtari miad va az in ATM estefade mikone



#-------------
psudocode??
function????
class (OOP)??


moshtari (vzihegi haye yeksan)-->object misazim
'''


'''
Class ADMIN_PANEL--> 
create_customer --> etelaate shakhsie ....
create_account--> account besaze
delete_customer --> shakhsie ro delete kone
view_all_costumers-->
deposit --> varizie shakhsie ro deposit kone
withdraw --> varizie shakhsie ro withdraw kone
transfer --> varizie shakhsie ro transfer kon
view_all_transaction ye nafaro
view_all_transsaction for all accounts-->


yeseri function tooye dele ADMIN_PANEL




admin_panel=ADMIN_PANEL()
admin_panel.create_customer('ali', '1234567890', '1234567890')
admin_panel.create_account('ali', '1234567890', '1234567890')
admin_panel.delete_customer('ali', '1234567890', '1234567890')
admin_panel.view_all_customers()
admin_panel.deposit('ali', '1234567890', '1234567890')
admin_panel.withdraw('ali', '1234567890', '1234567890')
admin_panel.transfer('ali', '1234567890', '1234567890')
admin_panel.view_all_transactions()


def create_customer():
    name ---> database zakhire kon
    name=input('enter your name: ')
    email=input('enter your email: ')
    password=input('enter your password: ')
    admin_panel.create_customer(name, email, password)
    print('customer created successfully')


name , email variables 
man ag system ghat konam?? --> hame ye etalaat hazf mishe !!
---> etelaat ro berizam tooye Database (paygahe dade)

database --> paygahe dade --> chizi has k chanta table dare
har table ham yeseri row , column dare
har columns --> yeseri type dare (string , int , float , date , time , etc.)




karmande banke shoam --> python balad nist !!!


Graphical user interface --> tkinter , pyqt , pyslide

GUI --> 

---------------------
Name :    | Password :    |
-----------------------
deposit button 
-----------------------
withdraw button | transfer button | view all transactions button


karmande bank ba oon kar kone --. GUI


deposit button --> seda bzna admin_panel.deposit()
withdraw button --> seda bzna admin_panel.withdraw()
transfer button --> seda bzna admin_panel.transfer()
view all transactions button --> seda bzna admin_panel.view_all_transactions()




#*******-----------------------------
database --> koja zakhire mishe?? tooye computer?

Hard --> K VAGHTY ghat mishe , bargh nabashe ...
zakhiran , 
roshan koni laptabe --> ahrchi roo harde sare jashe

moshkel?--> az hard computer bekhad data bekeshe
kh tool mikeshe .....




REDIS ??  --> DATABSE --> hard , memory(RAM random access memory)

[HARD ] --> [ram,memory]--> cache -- [CPU]
sari tare, geroon tare , kam hajm tare
------>



User --> 
website --> 10 conversation akahre az HARD (sql)-->redis
harkair mikoni , chize cjadi CRUD --> redis anjam


redis ....

PostgreSQL > sqlite >  mysql 



#------
1--> sql besazi done done besazi user , password
db besazi , db --> user,password

db --> table besazi 


python --> ketabkhone zabane sql benevisi



sql.
python --> sqlite3 module

sqlite3.connect('database.db')
cursor=connection.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT)')
cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', ('John Doe', 'john@example.com', 'password123'))
connection.commit()
connection.close()


curser.excute('Select Name from user where email=?',('john@example.com',))
name=curser.fetchone()
print(name)





#----> ORM --> Object Relational Mapping
database --> object --> python class
sqlalchemy --> ORM --> python class --> database

table --> class besazi

user.name



#--------------
0- data base, class ha ,.....
1- Bank MANAGEMENT SYSTEM --> CORE --> ADMIN_PANEL
2- Bank management GUI --> GUI --> tkinter , pyqt , pyslide
3*- html,css ,javascript --> web app bank
4*- fast api, django [shoroe kar] --> vasl mikoni API rabeti beyne
front ( html ,..) backend(python)



qt --> c++   --> 
pyslide
pyqt  --> sherate nis --> daghigahan cope pyslide
pyqt == pyslide


web app --> html,css,javascript



#---------------------------
python --> darim
mkdir bank_project
cd bank_project
python -m venv venv
#windows
venv\Scripts\activate
#linux, mac
source venv/bin/activate

#or --> go to anaconda and create new environement
conda create --name bank_project python=3.10
conda activate bank_project(esme environemnt)


pip install sqlalchemy 
pip install tkinter


#----structure

bank_project/
├── main.py ---> hameye kara onjas --> run konam
├── database.py --> inja bayad b database (mysql ,....)
├── models.py --> inja tabel , jadvaala, costumer , accounts ,...
├── utils.py -->functioni bashe k kara baram
├── core.py --> ADMIN_PANEL -->clas asli
├──admin_gui.py --> GUI admin panel --> TKinter
├──atm.py --> Class ATM **** optionall
├──atm_gui.py --> GUI ATM
|--README.md ->description

.doc
.txt

.md




'''

'''



pass harja shoma ^^^ yani bayad yekari bokoni


kare do --> tamame tavabe bayad printe khoshgel???

core.py --> takmil mikonid 1




#----------------
admin_gui.py --> Optionalll



ADVANCE********** --> 
CLAS ATM --> user , password 

show_balance()
deposit()
withdraw()


harkodom pinesho bzane 
hey pin bzn eharkodom kara



ATM_GUI() 




'''

