
"""
In The Name of GOD
Created on Sun Sep 28 20:07:27 2025

@author: Ali Pilehvar Meibody

---ADV _ L4 ----------
"""


'''
REVIEW------


programming
Human (en) ------interface||||| -----> Machine (bianry 0,1)


PYTHON --> YEK ZABANE



python --------------- 
ghavanini 
3 bakhshe

-----------------Reserved words -------------------
1- python built in function ---> print() ,input(),open(),len(),type(),......
2-Keywords --> banafsh --> taghiri dar logic(manteggh) if if else, if elif eklse , for , while ,....

---> if shorot
agar oomad

---> only if ---> mikhaym ye tike az afrado bekeshim kena y kari konan
--> do rahi if else --> if --> in karo ag na oonakro
--> if elif else --> dorahi k yekodom az rah dorahi mishe

--> loops (for, while)


---------------Unreserved words-------------
3- Variables --> 
esme zarf --> dakhele value
3.1. Numbers (3.1.1. Int 1,2,3,4  3.1.2.float 3.433 3.1.3 compelx j) --> (** * / + -) / (== , != > < >= <=)
3.2. boolean ( True , False)
3.3. String (--> reshte a='dhshsd') index 0 --> zarf[0] zarf[2:7] str functions
zarf.function --> 3.3.1. Convert --> .lower() .upper() ,....
3.3.2. Number 0---> zarf.count('a') --> 2  zarf.find('a') -->index
3.3.3. is --> true false --> islower() isupper() isdigit() ,......

function emal nmishe, khoroji midan


3.4 Iterables 






'''



#------3 unreserved words--> variables (moteghayer)--> zarf --------
#esm , value 
#esm -> ghavnin [2 , print , _ , ]
#VALUE --> adad
a=20 #Int

b=20.6 #float

c=1j #complex


#a+b = c
# a + b sho
#bad berizi tooye ye zarf benam e c

#--> yejk zarf besaz bname c bad
#a ro + b kon hala javabo briz too zarfe c

c= a+b



#algebric --> jabr --> moahsebe
c= a**b
c= a*b
c= a/b
c= a+b
c= (a-b)


#comparison --> moghayese
#besho
#a bealaveye 2 kon dastor
#Miporsi

a==b

a>b

a<b



#----boolean
g=True
g2=False

#-->str
d='ali'

d[0]

d[0:2]

e=d.upper()
f=d.count('a')


#------------
#ma dar zarfi k misakhtim fgth yek value mirikhtim
#yek chiiiz

#ag man bkham chanta chiz tooye ye zarf brizam chi???

#behesh migan
#iterables --> mige agah man mizaram chanta value dakhele man brizi



#--> list , tuple, set , dictionary

#---> har 4ta yekaro mikone --> chanta value tooye ye zarf mirize

#--> fargh ha dare


#*********
#--->iterables --> koli valeu ejaze midan dar yek zarf brizid



#4.1 ---> LIST

#4.1.1 assign (meghdar dehi)

esm=[10,20,30,40,50,60]

esm=list([10,20,30,40,50,60])

#comma --> joda kon elemente jdide

#iterable (list) -->havei koli element  ba comma joda shode

#---> changable , ordered , allow duplicated
#-->ghabele taghir, tartib dare , ejaze mide tkrari ham bzari

 
print(esm) #[10, 20, 30, 40, 50, 60]

print(len(esm)) #6

print(type(esm)) #<class 'list'>



esm=[10,20,30,40,50,60]


esm=[10.32,20.23,30,40,50,60]


esm=[10 , 10.6 , 1j , True, 'salam arz shod']


esm = [ 10 , 10.6 , 1j , True, 'salam arz shod' , [10,20,30,40]]



esm=[10,10,10,10]




#4.1.2. dastressi (access)
#dastam berese be elemnt

a='salam'
 
a[0]='b' #TypeError: 'str' object does not support item assignment


a[0] #'s'


#iterable az chaarcter ha hast

a=[10,20,3,40,50,60]

# ->0 1 2 3 4 5 6

a[0] # 10

a[2] #3

#ordered -> indexi 



a[0:4]  #0 , 1 , 2 , 3  #[10, 20, 3, 40]




#4.1.3 change
#fchra access ? 

a[2]=30


print(a) #[10, 20, 30, 40, 50, 60]




#--> ordered (index) , changable , allow duplicated 


#--> list tanha chzii has k application kh kh kh kh kh ziadi dare
#vaghty chanta chizi kjhasi k kenare ham bzari
#zakhre --> avalin option --> list


#3 ta kare khase --> tuple, set , dict
#oon 3 ta nabood --> liste

#ordred --> access
#change 
#allow duploicated




#4.1.4. list functions 
#--> function

print()
len() #hamast


#yekseri function darim fghto fght baraye --List ha mibashad

#append

#append('dsdjgh') XXXX

#esm_zarf.function()


zarf=[10,20,30,40,50,60]



'''
Method	Description

insert()	Adds an element at the specified position
remove()	Removes the first item with the specified value
pop()	Removes the element at the specified position
append()	Adds an element at the end of the list
extend()	Add the elements of a list (or any iterable), to the end of the current list

clear()	Removes all the elements from the list
copy()	Returns a copy of the list


reverse()	Reverses the order of the list
sort()	Sorts the list

count()	Returns the number of elements with the specified value
index()	Returns the index of the first element with the specified value

'''


#change

zarf[0]=1000
print(zarf) #[1000, 20, 30, 40, 50, 60]



zarf=[10,20,30,40,50,60]

#insert(kodom_index,ch_value?)


zarf.insert(1,1000)

#pas nadad

print(zarf) #[10, 1000, 20, 30, 40, 50, 60]




#---flashback b str functions

a='salam'
a.upper() #'SALAM'

print(a) #salam
#str functions --> khorohi mide, emal nmishe

b=a.upper()



#--------list functins -> emal mishe, khoroji nmide
a=[10,20,30,40,50]
a.insert(1,100) #Khrooji nmide
#mosatghim emal mikone, khode a taghir mikone
 

b=a.insert(1,100)

print(a) #[10, 100, 20, 30, 40, 50]
print(b) #None



#str functions --> khoroji dare , emal nmishe  a taghir nmikone b = a.function()
#list fucntiosn -> khoroji nadare , emal mishe --> a taghir a.function()   agar b = --> b =None




#----------------

#----> insert

a=[10,20,30,40,50,60]

a.insert(1,1000)

print(a) #[10, 1000, 20, 30, 40, 50, 60]




#---> man mikham b tahe in zarf 20000 ezafre konm

print(len(a)) #7 --> 60 --> idnexe 6
a.insert(7,2000)
print(a) #[10, 1000, 20, 30, 40, 50, 60, 2000]



a=[10,20,30,40,50,60]
#append b akahrie ezafe mikone
a.append(2000)
print(a) #[10, 20, 30, 40, 50, 60, 2000]

a.append(5432187172832172)

print(a) #[10, 20, 30, 40, 50, 60, 2000, 5432187172832172]


a.append('ali')
print(a) #[10, 20, 30, 40, 50, 60, 2000, 5432187172832172, 'ali']






#----hazf konim??
#migi man mikahm felan value ro hazf konm ---> .remove()

#man mikham felan indexo hazf konm --> .pop()


a=[10,20,30,40,50,60]
a.remove(20)
print(a)
#[10, 30, 40, 50, 60]



a=[10,20,30,40,50,60]
#indexe 1 hazf kon
a.pop(1)

print(a) #[10, 30, 40, 50, 60]



a=['ali','pilehvar',300,True]

a.remove(True)
print(a) #['ali', 'pilehvar', 300]




a=['ali','pilehvar',300,True]
a.pop(3)
print(a) #['ali', 'pilehvar', 300]



#----delete , clear --> fargh
#list, str , har variable
del a 

#print(a) #NameError: name 'a' is not defined



a=[10,20,30,40,50,60]
#clear ?? --> clear --> khaliiish kon toosho 

a.clear()

print(a) #Behem error nmide, a i vojod ndre #[]

#reset 






a=[10,20,30,40,50,60]

#element mikhay exzafe koni b yek iterable(list)
a.append(800000)

print(a) #[10, 20, 30, 40, 50, 60, 800000]





a=[10,20,30,40,50,60]

b=['ali','vahid','hamid']

a.append(b)


#6 + 3 --> 9 ta element

print(len(a)) #7
#????

#kole liste b ro be onavne yek elemwnt ezafe kard eb tahe a
#ama man mikhastam element haye b bere tahe liste a
a.append(b)



#append(element)
#extend(iterable)



a=[10,20,30,40,50,60]
b=['ali','vahid','hamid']
a.extend(b)

print(len(a)) #9




'''
list --> ordered , changable , allow duplicated

a=[1, 1.5 , True , 'ssddfh',]
a=list([dasd,dasa,dssd,das])

a[index]

a[start:end]

a[index]=new_value


list functions --> **emal mishan , khoroji nmidan
a=[sdhadhs]
a.list_function()

#niaz b b --> a taghir mikone



#replace --> a[index]=new_value



#yani baid too kodom idnex ye adad bendaze vasatesho
a.insert(index,value)


a.append(value)  #b tahesh michasbone
a.extend(iterable) #element haye tooye on listo ezaf mikone ba a


a.remove(value)  #in element
a.pop(index)

del a #-->kole a ro zarfo jasho hamechio pak mikon a i vojod ndre
#resdet fght toosho 
a.clear()


'''

a=[10,20,30,60,40,35]

a.sort()
print(a) #[10, 20, 30, 35, 40, 60]


a.reverse()
print(a) #[60, 40, 35, 30, 20, 10]




a=[10,10,10,10,20]

a.count(10) #khoroji mide -->  4

a=[10,20,30,40]

a.index(20) #1


'''
class LIST:
    
    def __init__(self,....):
        self.list
        
        
        
    def extend(self,iterable):
        
        for element in iterable:
            self.list.append(element)
            

'''



a=[10,20,30,40]
b=['ali','vahid']



for element in b:
    a.append(element)

print(a) #[10, 20, 30, 40, 'ali', 'vahid']


a=[10,20,30,40]
b=['ali','vahid']
a.extend(b)
print(a) #[10, 20, 30, 40, 'ali', 'vahid']







#---
a=[10,10.4,True,'salam']
a=list([])

#---> Ordered (indx) , Changable , allow duplicated


#--> shoma check mikoni ag tuple , set, dictionary --> list (avalin option)


#chanat value mikhaym zakhrie konim

#side moshtari -> 20 ta porduct begiri 
#sabad kharid -> etelaat  , yek zarf rikhte

#mohasebat -->


#AI --> 7 ta moidele hoshe masnooe
#bere pishbini kone --> darsad 2 % , 3% 
#7 ta model
#LR , DT , RF , SVR , MLP(ANN) ,KNN , LSTM

#for 
svr_score=''
dt_score=''
felan_model_score=''


scores=[2,4,5,7,1,2]










#4.1 ---> TUPLE

a=[10,20,30,40]

a=[10]


b=(10,20,30,40)

b=tuple((10,20,30,40))

print(type(a)) #<class 'list'>

print(type(b)) #<class 'tuple'>

b[0] #Out[83]: 10

b[1] #Out[84]: 20

b=(10)
print(type(b)) #<class 'int'>
b=(10,)
print(type(b))



#ordered  , changable??



b[0]=100 #TypeError: 'tuple' object does not support item assignment



#orderd, unchangable , allow duplicated



#tavae
#tuple.functions()

#emal msiah


tupel=(10,20,30)
for element in tupel:
    print(element)




#---bale mishe ama khob 

#tupel --> list taghir bde --> tuple


a=(10,20,30,40)



#bejaye 20 --> 20000

a[1] #20

a[1]=2000 #TypeError: 'tuple' object does not support item assignment
print(a) #(10, 20, 30, 40)


#ychizio list --> poshte list()
#---> tuple()
#set()
#dict()


b=list(a)

print(b) #[10, 20, 30, 40]
print(type(a)) #<class 'tuple'>
print(type(b)) #<class 'list'>


b[1] #20

b[1]=2000

print(b) #[10, 2000, 30, 40]


print(a) #(10, 20, 30, 40)



a=tuple(b)

print(a)
#(10, 2000, 30, 40)



'''
a-->tuple

-->listesh krdm -> B
taghiresh dadam
--> tuple
a= tuple(b)


'''





#data base --> paygahe dade 

#paygahe dade --> mysql , sqlite -> hard ( SSD, )
#redis --> Memory (RAM)




#4.1 ---> SET
a=[10,20,30,40]
b=(10,20,30,40)
c={10,20,30,40}
c=set((10,20,30,40))


#ordered??


c[0] #TypeError: 'set' object is not subscriptable
#index ndre

print(c) #{40, 10, 20, 30}



#order nadare ,index ndar
#unordered ,

#adare, access konm?? na chang?


#unchangable 


#allow duplicated na nmishe


c={10,10,20} #error nmid khdoesh hgazf mikone

print(c) #{10, 20}





#unordered, not changable , not duplicated


#yechizio zakhrie koni k majmooe ha --> ejaze ndre shabihe ham bashan


#ya y listi ya harchizi dari 
#list dari -_> in list koli chize tekrari toshe
#Mikhay tekrari haro hazf koni

#for ... hbegrardi brizi 


a=[10,20,20,30,40,50,50,60,70]


#....

b=set(a)

print(b) #{70, 40, 10, 50, 20, 60, 30}

a=list(b)

print(a) #[70, 40, 10, 50, 20, 60, 30]

#tekrari haro hazf krdm

a.sort()

print(a)
#[10, 20, 30, 40, 50, 60, 70]





#4.1 ---> dictionary




a=[10,20,30,40]  #ordered (index) , changabel , allow duplicated
b=(10,20,30,40)  #ordered (index) , unchangabel , allow duplicated  __. listie k change nmisuhe --> DATABASE
c={10,20,30,40}  #unordered (index ndre) , unchangabel, no duplicated --> hazf konid tekrariaro




#gahiii

#access tooye list, tuple [set idnex ndre access]


#esm_zarf[index]




#moshakahsat (moshakahst) bzakhrie konm


d=['reza',40,70000, 'bmw']



#yeja mikahm bnvism b snesh + 2

#indexe 1

d[1] + 2 

if d[3]=='benz':
    print('felan karo')




#ye frd --> dna , shoamr maliati , shenasnams ,,...

#listi ln -_> 28



#d [26]-->shenasanas


#b ejaye indx
#yechizi mniunevshtm


#d['shenasname']


#d['telehphone]
#d['sen]
#d['nam']


#d[3]

#d['car'] -->


#bejaye index --> key --> kilidvazhe



#dictionary ---> mige man ino drm





d1=['reza',40,70000, 'bmw']


'''

index value
0    reza
1     40
2     70000
3    bmw

d[index] -->value




'''



#fght value , value , value, 


#key : value , key : valu , key : value , ....

d2= { 'esm' : 'reza'    ,  'sen' : 40 ,'pool' : 70000 , 'mashin' : 'bmw'   }



#d1 --> list
print(type(d1)) #<class 'list'>
print(type(d2)) #<class 'dict'>


d1[0] #'reza'
 
d2['esm'] # 'reza'

d2['sen']  #40
d2['pool']  #7000
d2['mashin'] #bmw



d1[27] #--> 09123762376276

d2['telephone'] #--->

#ordered by keys , key duplicated (VALUE)  , changable hast


#---> dastresi



#assign -------

'''
index value
0
1
2



key  value
..    ...



'''


#e={ , , , , , , , }

#key : value


e= { 'esm': 'reza' , 'vazn' : 100 , 'ghad' : 190 , 'car': 'toyota' }



#---> dastres

#e[indedx]


#e[key]


e['esm'] #'reza'




#change???

#d1[4]=39223718  list (tuple, set XXXX)


e['vazn']=80

print(e)

#{'esm': 'reza', 'vazn': 80, 'ghad': 190, 'car': 'toyota'}

e['vazn'] #80



#bekhay y value jadid ezafe koni???
#key : value

e['shoghl']='hojre dar'

print(e)

#{'esm': 'reza', 'vazn': 80, 'ghad': 190, 'car': 'toyota',
# 'shoghl': 'hojre dar'}



#dict function

e.items() #dict_items([('esm', 'reza'), ('vazn', 80), ('ghad', 190), ('car', 'toyota'), ('shoghl', 'hojre dar')])


e.keys() #dict_keys(['esm', 'vazn', 'ghad', 'car', 'shoghl'])

e.values() #dict_values(['reza', 80, 190, 'toyota', 'hojre dar'])







'''
--------reserved words------------
1-------python built in functions (print())
2-----keywords (if , esle , elif)

------unreserved wordss------------
3-variables
3.1.numbers (int, float, complx)
3.2.boolean (True,False)
3.3.str --> a[index] , str functions zarf.function( .upper() .lower())  --> khoroji b=a.lower()
3.4.iterables --> chanta value mikhasim berizim too zarf

3.4.1. List [ ] --> ordered (index) , chanagble , allow duplicated , list functions ( .append() .insert() .index()) --> emal mishod khoroji nmidad
3.4.2.  Tuple () --> ordered , unchangable , allow duplicated --> DATABASE
3.4.3. set {} -_-> index ndre, unchangable , no duplicated 
3.4.4. dict{key : value}  bejaye index --> keys --> zarf[key] --> dastrsi peyda mikoni


'''





#------------------------------
name=input('name mahsoolo begoo:')
code=input('code mahsool begoo:')
price=input('gheymate mahsool:')


text=f"""
-----plutus--------
product name : {name}
product code : {code}
        total : {price}
        
        
    PLUTU
"""


print(text)



answer=input('doaya taeed mikonid (yes/no)?')

if answer=='yes':
    print('bale sabt shod')
elif answer=='no':
    print('sabt nashod mojadad')
else:
    print('yes ya no bzn')


'''

#----task1--------
name , code , price --> tooye yek list 
va az list bekeshi biron berizi tooye text namayesh bdiii


#----task1.2.---------
hatman az tabeye append() toye ghesmat list



#----task2-----
baraye tuple


#---task 3-----
dictionary products= --> kilidvazhe name , price, code



#4-----task4------
dictionary --> products -->
price ro az dictionary mikeshi biiroon taghiresh midi va (- 20% mikoni)


#---task5
tuple darim --> har 3 taro beriz toosh name , price

price ro az tupel bekesh biron -20% kon dobare az delsh beksh --> text


--> tuple gahbele taghir nis ?? (tuple --> list)




'''




























