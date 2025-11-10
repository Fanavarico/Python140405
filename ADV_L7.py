"""
Created on Sun Nov  9 17:35:32 2025

@author: apm



ADV - L7


"""


'''
-----REVIEW--------

Machine (computer) ---> 0,1 --> hamechio 0 ,1
interface (programming language) --> mokhafaf --> application --> programming language
Python --> application, library , learnin curve , community


Human (En) --------Python ----------Machine(Binary 0,1)



Python-------> 1-Ipython 2-IDE(editor)
# qout--> comment miaprid
baghei ro az bala b paeen, az chap be rast --> mikhodnsh


#---------------------------------------------
1- Python built in functions ------- nareni
function --> tabe --> call --> yekari mikrdn
100,200 , 50 --> ye esm seda zdn
print() input() len() type() 
https://docs.python.org/3/library/functions.html
all() any() enumerate() 
getattr()  hasattr() isinstance() zip()





#---------------------------------------------
2- Keywords --> banafsah
if else elif , and or , for while def ,.....
--> mantegeh codo beham mizanan 
ye kaht baray ehame run nashe --> if 
ye kaht 100 bar run --> for


2.1. Sharti , conditional statement
ye khat code --> baraye hame ejra nahs

**shart -_> True , False
if shart1 or/and shart2:
    dastooor
    dastoo2
    dastoo3
    
age shartet true shod kar anjam bde , ag nashdo hichi
--> rahzan --> fght yeseri haro majbor mikoen khat code run she


ag nashod chi? veelsh kon> 
ag true shod karhaye1 ag nashdo karhaye2 --> dorahi

if shart1 or/and shart2:
    dastoor
    /...
    
else:
    dastooorr....
    
    
    
dorahi dar dorahi
ag shod kare1 , age nashdo (if --> B , C)

if shart1:
    kare A
    ...
elif shart2:
    Karhaye B
else:
    karhaye C
    
    
    
    
    
        |
        |
      shart1
   --------------
  |True         |False
  A             shart2
           --------------
           |True         |False
            B            C




#----looop (halghe ha)
For --> 1-Repeate 2-iteration(Varrsi)

*i , j , k , l , item , element,
#list, tupel , range(start,end,step)
for i in list:
    print()
    a+b
    
i = elemnt1 --> print() --->khorji
i=ydone ezafe --> 
hads


for i in [10,20,30,40]:
    a=i+1
    print(a)

i=10 --> a=10+1=11 print(11)-->11
i=20 -->a=20+1=21 print(21)->21
30,40 --> 31 , 41 ,....

#iteration

list-->adad , hezarta chizi 
beri toosh done doen elemtn ro beekshi biron


for i in list:
    #if ...
        count=count+1
        #new_list.append()
    
#zojano joda koni, berizi , print , count
#helemnt hae, esm hae k avaleshon felan



#---whule --> range baste ee behesh nmidi
migi agha y shart mizari ta zamani k True has boro felan karo kon

i=shomarande (shoamrande ag nazarri , error mide) (shomarande-->sghartp True)

#shart --> True varede halgeh 
while Shart:
    dastoorate (loop)
    i=i+step  #ykar koni k loop b samte ekhtetam [endless loop]
    

while True:
    input(....)
    if :
        break #sharte ekhtetam
        
 
    

#---------------------------------------------
3- Variables (moteghayer)  esme zarf-->sefi
3.1.Numbers --> int, float, complex --> ** * / + - 
comaprison -> == != > < 
3.2.Boolean --> True , False
3.3.Str --> 'reshte ee az character' --> [0] , [start:end+1] 
str.function()  --> a='ali'  a.upper()
3.4.Iterables --> multipel variable
    3.4.1. List -> [, , ,] ordered(index),changable, allow duplicated
    3.4.2. Tuple -->(, ,,) ordered(index),unchangable, allow duplicarted
    3.4.3. SEt --> {, , } unordered( no index),unchangable, No duplicated
    3.4.4. Dict --> {key: value}  bejaye variable[index] --> variable[key]  a['id sen']
    
    []  -->   iterablesl.fucntion()  .append() .insert() .clear() ,....
    
    

'''





#--------FUNCTIONS----------------
'''
Raveshe code zani
1- Psudocode --> beshini y script .py -->
az bala ta apeen code bzni --> ina vase y seri barname
sade , y calculation sade , y kare sade okeye
barname , app , mini app , 


2- Functions based --> khat haye codeto brizi
dar yek tabe (BOX)--> va hey azoon stefade koni 
import mitoni beyne script .py .py 


3- Object oriented programming (OOP)



'''


#--------------
'''

10 ta folder , har folder 5 script

50 .py files --> 1000 khate


a1.py --> ye ghesmat codoo begiram 
bedam b a2.py --> 
az a2.py --> a3.poy---
a4.py ejra bshe 3 ghesmat

a5.py --> moshtari 




function

1--> use --. call , extend -->encapsulation
repeat() --> repat too ye .py 5 
tamzi --> tamiz khoshgel ...




dar donyaey barname nevisi

10 .py 


1 .py --> RUN 

9 ta .py --> function toosh zakhirash

'''

#mitonesi variable 


a=10
b=1


c=a*b
d=c
if d>5:
    print('salam')
    
elif d>3:
    print('sa')
    
else:
    print('khodafez')



'''



input ---> BOX ---> output



1-----Sakht declaration
name --> ghavaini nam variable
--> 23 , print , reserve , space _


def name(input):
    badanas..
    ....
    ....
    return 
    khoroji ndi


define --> tarif shod
yani skeelti , skahtari b python ddi
k badan bfhme ag kasi name ro seda zad yanichi
montazere javabi nbsh


2- call --> seda use
name()


'''


#--------------------------
#--------------------------
#--------------------------
#--------------------------

#farghe khoroji print()


def newton(m,a):
    f=m*a
    print(f)
    
#nedsydsd(10,5) # NameError: name 'nedsydsd' is not define
newton(10) #TypeError: newton() missing 1 required positional argument: 'a'
newton(10,5,6) #TypeError: newton() takes 2 positional arguments but 3 were given

newton(10,5)
#f=10*5 --> print(50)

    
#khoroji dare???

zarf=newton(10,5)

print(zarf) #None

#zarf nemitoni jolosh bzari, zarf bzari None
#khoroji ndde


def newton(m,a):
    f=m*a
    return f
    

newton(10,5) #Out[16]: 50


zarf=newton(10,5)

print(zarf) #50




def newton(m,a):
    f=m*a
    print(f)
    return f


zarf=newton(10,5)





#khroji , print()

#print--> real world --> debugging

def processing(data):
    
    print('started....')
    
    
    print('machien learning started')
    #data --> Machei ANN
    
    #ml_result
    
    print('ML done!!!')
    #print('ml rsult:'ml_result)
    
    #artificial neural network
    
    #NLP-->
    
    #post processing
    
    
    #web --> data image
    
    
    #opencv --> computer vision
    
    
    #>..
    
    
    #adad --> shalkhset keyfiat
    
    
    #return .....
    
    

    

#badane dashe bashe

def welcome():
    pass
    
    
    
    
    
#1-na khrooji dare na vorodi
  
def welcome():
    print('salam')
    print('khdoafez')
    
    
    

#jolosh zarf
welcome()




#2--- vorodi , khoroji ndre

def newton(m,a):
    f=m*a
    print(f)
    

newton(10,5) #50

zarf=newton(10,5) #50

print(zarf) #None



#3- vorodi nadshte bashe, khrooji dashte bashe

def calculate():
    a=10
    b=30
    
    d=a+b
    
    return d


zarf=calculate()



#4- kamel tarin --> ham vorodi ham khoroji

'''

INPUT ---> BOX ----> OUTPUT


'''
def newton(m,a):
    
    f=m*a
    #print()
    return f


zarf=newton(10,5)


print(zarf) #50



#------GLOBAL LOCal------


def newton(m,a):
    f=m*a
    return f



answer=newton(10,5)

print(f)


#---yekbar baraye hamishe , tabe daghighan 


#477 - 479 --> tabe ro omdim tarif krdim

#python too memory (ram)--> Newton -_> function
#m,a -->yechizaee ham tooshe


#483--->run mishe

#answer=   --> ye zarf ag nis besaz , ag hast kahli kon

#newton() -->function
#ag tarif nashode --> Newton is not defined
#--> barmigarde b memorysh--> fucntion (m,a)

#m , a ro dadi ya na?

#ag kamatr dadi --> miss  eerror
#bishtar --> n ta , m ta dadi -->error
#tatabogh --. 


#m=10
#a=5
#bsoorate movcagaht in dota ro misaze
#f=m*a
#har zarfiu dakheel function-->movaghat
#f=10*5
#return f 
#return (f) valeu megdhare toye f

#return 50 
#jaee k call shode

#answer=newton(10,5)

##answer=50


# a, m , f -- >remove mikoni 
#input --> return (dakhele tabe) -->yekseri skahte shdoan , pak shdon


#LOCAL --> movaghate dakheli

#ag shoam biron az 

#print(f)
#print(a)
#print(m)
#NameError: name 'f' is not defined



a=100

def newton(m,a):
    f=m*a
    return f


answer=newton(10,5)

print(a)

#memory --> a=100

#cache --> a=5 --> vaghty kar return m,a,f 
#ag too memory adadi nabashe --> hazf mikone
#ag bashe -> bareshon migrdone b adadi k bood



#yek zarfio agah ag sakht -->forget nakone??
#chiakr konM??


def newton(m,a):
    global f
    f=m*a
    return f

answer=newton(10,5)


print(f) #50

#m , a --> movagahati [cache]
#f --> movagahtnmisaze --> memory


f=200
def newton(m,a):
    global f
    f=m*a
    return f

answer=newton(10,5)

print(f) #50


'''



HARD   MEMORYY  CACHE (TRANSISTOR)




HAMECHI --> MEMORY 

m=10 , a=5 , f=50 --> CACHE

MEMORYY-->m X a X f X ( )


'''


#------ARGUMENTS-----------



def newton(mass,acceleration):
    force= mass* acceleration
    return force


#positional argument
answer=newton(10,5)

#keyword argument
answer=newton(mass=10,acceleration=5)


#--------------------


#only positional
def newton(mass,acceleration,/):
    force= mass* acceleration
    return force


answer=newton(10,5)
answer=newton(mass=10,acceleration=5) #TypeError: newton() got some positional-only arguments passed as keyword arguments: 'mass, acceleration'




#only keyword
def newton(*,mass,acceleration):
    force= mass* acceleration
    return force


answer=newton(10,5) #TypeError: newton() takes 0 positional arguments but 2 were given

answer=newton(mass=10,acceleration=5)

#hybrid----------

def custom(a,b,/,*,c,d):
    f=a*b*c*d
    return f



custom(10,20,c=100,d=200)




#default----------

def newton(m,a):
    f=m*a
    return f

#ag yekiyadesh raft a ro bd chi??

#python --> 2 ta migiri --> error mide

#XXXXXXXXXXXXX
def newton(m,a):
    if a==None:
        a=10
    f=m*a
    return f

newton(5,None)
#newton(5)


def newton(m,a=10):
    f=m*a
    return f


newton(5,6) #M=5 , A=6 --> F=30

#error
newton(5) #m=5 a=10 --> 5*10=50






#--------------
#*arg #**kwrg

#arg--> tuple 
#karg--> dictionary
#newton(a=10,b=30,c=40)



#de newton(a):
    #a[0]
    #a[1]
    #a[2]
    
    
    
#**

     #mylits['a']






#-----IMPORT MICROSERVICE-------



def calculator(numb1,numb2,operator):
    
    if operator =='+':
        answer=numb1+numb2
        return answer
    
    elif operator=='-':
        answer=numb1-numb2
        return answer
    
    
    elif operator=='*':
        answer=numb1*numb2
        return answer
    
    elif operator=='/':
        answer=numb1/numb2
        return answer
        
#tabe ...


#--------------------------
#1-psudocode--->yeja benevisi
#2-Function based 
#3-object oriented programming
#OOP--_> class [def]


#CLASS--->
#c / c++ 
'''
c++ --> class ha support


'''

#man y bank mikham bsazam

#k azash pul brizma roosh
#pool bardahst konm va hamin
#mojodi bgirm



def deposit(amount):
    global balance
    balance=amount+balance
    print('your balance is',balance)
    


deposit(100) #your balance is 100



def show_balance():
    global balance
    print(balance)



show_balance() #NameError: name 'balance' is not defined
#100


def ATM(amount):
    global balance
    balance=balance-amount
    
    print('balance : ',balance)
    
    

ATM(50) #balance :  150

deposit(200)  #your balance is 350

#fght baraye khdoet estefade koni

#y nafar dg bekahd hesab baz kone???


#man too tabe 100 ta motghayer
#done doen hamashono global konam??

#gajhan yejahae , application ha
#shoma naiz dari
#variable haro beyen hamgahrz bdi


#--> global 


#function ha dg javab nmide??

'''

jae k shoma ba yeseri 'chiz' saro kar dri
kj hamashon too ye seri vizhegi ha baham yeksanan , shabihan



Class , typi 

adam bekshim , device , ...


object bekshi aaz class bironn



class --> Hesab banki 
object -> har fardi h hesab dre



class --> GYm -> bashgah badansazi
objct--> varzeshkara



CLASS---> 1-attributes  , variable 
2- Methods , functions

class --> object besazi


hamashon yekseri method , attributesd --> ina baham gahti nmishe




'''



class BANK:
    pass



a=BANK()
#a-->shey
#ac ch class? type --> BANL

print(type(a))
#<class '__main__.BANK'>


print(a) #<__main__.BANK object at 0x16f8d3580>


class BANK:
    name='ali'
    balance=100
    id_number='0440000000000'
    


a=BANK()

#az bank -> y shey saktam rikhtmsh tooye a
#a --> object
print(type(a))
#<class '__main__.BANK'>



a.name #'ali'
a.id_number # '0440000000000'
a.balance #100


b={'name':'ali', 'id_number':'04440000','balance':1000}

b['name']

#a.name
#avalin frgh -->

#dovomin?---> dakhelsh functiomn bezari



class BANK:
    name='ali'
    balance=100
    id_number='0440000000000'
    
    def welcome(self):
        print('salam')
        
        
a=BANK()


a.name #ali
a.balance #100
a.id_number
 
a.welcome() #salam


'''
CLASS ---> Object besazi
1- attributes 2-methods



'''


#a=BANK(name= , balance= ,....)

#bale mishe --> tabe e bname __init__


#------class vaghei shoro msihe

class BANK:
    
    #chia az vorodi bgirm vaghty mikhad ye object az man besaze??
    def __init__(self,name,id_numb,balance):
        
        self.name=name
        self.id_numb=id_numb
        self.balance=balance
    
    

a1=BANK() #TypeError: BANK.__init__() missing 3 required positional arguments: 'name', 'id_numb', and 'balance'


#in ejaz emdi eman baray chan nfr
#chanta shey bsazam

a1=BANK('ali','044',1000)

a2=BANK('vahid','077',2000)


#....

a1.name #Out[83]: 'ali'

a2.name #Out[84]: 'vahid'






class BANK:
    #chia az vorodi bgirm vaghty mikhad ye object az man besaze??
    def __init__(self,name,id_numb,balance):
        
        self.esm=name
        self.shomare_meli=id_numb
        self.mojoodi=balance
    
    
a1=BANK(name='ali',id_numb='044',balance=1000)
 

a1.name #AttributeError: 'BANK' object has no attribute 'name'

a1.esm #'ali'

a1.shomare_meli


a1.mojoodi



#class --> 1-attributes 2-functions

#attributes---> adade sabet
#,method ->  fucntions


class BANK:
    def __init__(self,name,id_numb,balance):
        
        self.name=name
        self.id_numb=id_numb
        self.balance=balance
        
    #save??
    
    def welcome(self):
        #print(f'salam b moshatrri aziz  {name}')
        print(f'salam b moshatrri aziz  {self.name}')

    


a1=BANK(name='ali',id_numb='044',balance=1000)
#attributes
a1.name
a1.balance
a1.id_numb

#functions
a1.welcome() #-->salam moshaarie aziz ali khosh amadi
#salam b moshatrri aziz  ali


a2=BANK(name='vahid',id_numb='044',balance=1000)

a2.name
a2.balance

a2.welcome() 
#salam b moshatrri aziz  vahid

#yekseri rtabe ro besazam
#k betomen besoorate customzie , shakhsi 
#done doen baraye har shey ( moshatrri , customer)
#ejra beshe

class BANK:
    def __init__(self,name,id_numb,balance):
        self.name=name
        self.id_numb=id_numb
        self.balance=balance
        
    #save??
    def welcome(self):
        #print(f'salam b moshatrri aziz  {name}')
        print(f'salam b moshatrri aziz  {self.name}')

    def show_balance(self):
        
        current_balance=self.balance
        print('mojodie shoma hast : ',current_balance)
        
    
    def deposit(self,amount):
        self.balance=self.balance + amount

        print('moafagh ast , hesabe shoma :',self.balance)


    def ATM(self,amount):
        self.balance=self.balance - amount
        print('moafagh shod , hesabe shoma : ', self.balance)
        
#a1.deposit(1000)



a1=BANK('ali','044',1000)
#attributes
a1.name
a1.balance
a1.id_numb #044




a1.welcome()
#salam b moshatrri aziz  ali

a1.show_balance()
#mojodie shoma hast :  1000


a1.deposit(2000)
#moafagh ast , hesabe shoma : 3000



a1.show_balance()
#mojodie shoma hast :  3000



def deposit_ali():
    pass
    
    
    
def deposit_vahid():
    pass