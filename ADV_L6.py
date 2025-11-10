"""
Created on Sun Oct 26 17:43:45 2025

@author: apm

ADV-L6
"""



'''

-----REVIEW-------

Human ------ interface ----machine

interface -->Python

------reserved-------
1---python built in function --(print,len,....())
2- keywords --> If , if else, elif , for , while , def ,.. -->manteghe cod ro taghir mdiadan


----unreserved-------------
3-variables --. zarf
3.1.numbers (int,float,complex) ** *  + - / ..... 
3.2.Boolean (True,False) --> == > <
3.3.Str ('' , [index0] , str functions --> lower() upper() ,...)
3.4.iterables --> chanta value varede yek variable
3.4.1 List --> [] ordered,changable , allow duplicated --> list function (insert, append ,....)
3.4.2. Tuple --> () ordered, unchangable , allow duplciated
3.4.3. set --> {} unordered (index X , no access) , unchangable , No duplicate
3.4.4. Dict --> {keys : values}  zarf[index]  zarf[key] --> informations








----Keywords--------

python az bala b paeen az chapo b rast mese ye ensan
code mikhone compile --> age kahstim yejaee taghiri bdim

soraghe [2]-->keywords



jaee kahstim codi mese hamishe vase hame run nashe --> agar , 
shart ha
if statement --->

1-only if --> fght baraye yekseria run bshe , shartesh false -_> mohem nabod

2-if else --> dorahi oonae shafrt True --> ye kar , False-->ye kar

3-.if elif else --> ye dorahi True ye kar , false -> dorahi





-------
Loops ---> halghe
FOR , WHILE



for --> specific harf zadim 

for --> 1 - tekrar 2-iteration (varresi , bazresi ,....)


'''

#---------TEKRAR

for i in [1,2,3,4,5,6,7]:
    print('salam')
    print()
    
    
print()
    





for i in [1,2,3,4,5,6,7]:
    print('salam')

'''
Principle , mechanism , algorithem
oon hcizi k oon posht etefgagh miofte


b ezaye i haee  dar in list hastan bia dastoore paeen ya dastoorate paen ro run kon
(dastoo print , i ro estafde konde , nakon a+b ,...)


i=1 --> dastor ejra --> print('salam') --> salam
i=2 --> dastor ejra --> print('salam') --> salam
i=3 --> dastor ejra --> print('salam') --> salam
i=4 --> dastor ejra --> print('salam') --> salam
i=5 --> dastor ejra --> print('salam') --> salam
i=6 --> dastor ejra --> print('salam') --> salam
i=7 --> dastor ejra --> print('salam') --> salam
va i!=8 --> miad biron az halghe --> edame mide
b code e mamoli




'''



#az 1 ta 1000??

#for i in [1,2,3.....,1000]

#tabe --> range(start,end)

#range(end) ---> 0 ta end 1 1 1 

#range(start,end) --> start ta end 1 1 1

#range(start,end,step) --> start ta end step step 

#[]--->

#for i --> toosh

for i in range(10):
    print(i)


#akahri --> 10 excluded --> shamel nmsihe
#Index

#a=[10,20,30,40]
#a[0:2] --> a[0] [a1]


for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)




for i in range(10,40,2):
    print(i)
    
    
'''

b ezaye i haee k dar range(10,40,2)

rang(start,end,step) --> 10 , 12 , 14 ,16 ,...38 , XXX40XX

i=10 ---> ejr amikone --> print(i) --> print(10)-->10
i=12 -->ejra kone-->print(i) --> print(12)-->12


10
12
14
16
18
.....


'''





for i in [10,20,30,40,50]:
    print(i)


'''
be ezaye i haee k dar in hastan ye kari mikone
'''



mylist=[10,20,30,40,50]
for i in mylist:
    print(i)


'''
varede yek iterable (list,tuple, string,...)
fone element hasho bekesham biroon


'''




mylist=['ali','vahid','reza','hamid']

for i in mylist:
    print(i)
    
    
'''
b ezayae i haee k dar in list hastan code ro ejra kon

i='ali' --> print(i)-->print(ali)-->ali
i=vahid -->print(i)-->print(vahid)-->vahid
i=


ali
vahid
reza
hamid


tekrar nist doostan
dare mire dakhel mitone b element ha datresi peyda kone



for loop --> 1-TEKRAR 2-varrresi (iteration)


inghd sade



'''



print(mylist)



for j in mylist:
    print(j)


mylist=['ali','vahid','reza','hamid']

for fard in mylist:
    print(fard)


'''
fard='ali' -->print(fard)-->print(ali) -->ali
fard=vahid



i , j , k , ..fard ,...



'''


for person in mylist:
    print(person)



'''
beri yek iterable ( list,tuple,dictionary)
elementasho bekeshi biron
khob? --> shart gozari koni , check koni , beshmori felan koni


for , if estefade mikonam


for --> too delesh if

'''
    
#--> yani man ye liste daneshjoo darsm
#mikham oonae avale esmeshon a dare print beshan




mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']

'''

bayad beram tooye listy done donashono beksham biron


check konm age hrfe avalsho
done elementaro bekshambiron

roye done done elemnta check konm

'''


    
for i in mylist:
    print(i)
    
#i ->done donasho
#printesho mikone
'''
ali
vahid
reza
hamid
asal
arezoo
amir
'''



for i in mylist:
    if i[0]=='a':
        print(i)
'''
ali
asal
arezoo
amir

'''

mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']
for esm in mylist:
    #baraye harkoodm
    #harfe avale esme
    if esm[0]=='a':
        print(esm)
       

#-------------XXXXXXXXXXXXXX-----------
mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']
for i in mylist:
    if i[0]=='a':
        print(i)
        
'''
i=ali , vahid , reza , ,....
'''


#raveshe dg
#i
'''
i=0,1,2,3,4,5,
'''

#len myslist = 7
#range(0,7)--> 0 ,1 2 3 4 5 6
for i in range(0,len(mylist)):
    #if i[0]=='a'
    if mylist[i][0]=='a':
        print(mylist[i])
    





#---------------------
#+++++++++++++++++++++++++
#--------FOR LOOP---------
#+++++++++++++++++++++++++
#easy --> i 
#------------1-TEKRAR REPEAT
for i in range(0,100):
    #....
    pass

#------------2-ITERATIONS
#for , if 
#--2.1.---> iteration check -->printesh oono
mylist=['ali','vahid','reza','hamid','asal','arezoo','amir'] 
for i in mylist:
    if i[0]=='a':
        print(i)
        
        
        
#--2.2--> jodash kon --> beriz too y liste dg
mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']
new_list=[] #ag nasazi mige asan new_listi nis man append konm
for i in mylist:
    if i[0]=='a':
        #print(i)
        new_list.append(i)
        
'''
i=ali --> if i[0]=='a':
    #print(i)
    new_list.append(i)
    
dobare
i=ali --> i[0]-->a a==a --.True --> if -->new_list [].append(ali) -->new_list=ali
i=vahid -->i[0] -->v v==a -.False 
i=reza --> r -->false
i=hamid --> h --> false -_>abz bnmsihe
i=asal --> a==a -->True-->new_list.append(asal)

'''
       

#choon tooey body badaneye for chizi bname print ndrim
#vaghrty run mikonkm ham chizi nmibinim
#ama
#yk list sakhte shode

print(new_list)
#['ali', 'asal', 'arezoo', 'amir']
print(mylist)
#['ali', 'vahid', 'reza', 'hamid', 'asal', 'arezoo', 'amir']


#----3-beshmori
mylist=['ali','vahid','reza','hamid','asal','arezoo','amir'] 
count=0
for i in mylist:
    if i[0]=='a':
        #print(i)  nm ikhaym namayesh
        #new_list.append(I) -->nemikhay avresh
        #chikar?-->mikham beshnoar
        count=count+1
        
        
        
'''
choon print nmibine

i=ali --> if a==a -->True -_> count = count+1 =0+1 = 1
i=vahid --> if v==a --.False count ezafer nmsihe
i=reza
i=hamid
i=asal --> if a==a -->True ->count=count+1 =1+1=2


'''
        
        

print(count) #4

#----advanced-----
#----#-4------
#asan joda kone az liste ghabli 
mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']
new_list=[] #ag nasazi mige asan new_listi nis man append konm
for i in mylist:
    if i[0]=='a':
        #print(i)
        new_list.append(i)
        mylist.remove(i)
        
print(mylist)
print(new_list)


#-----5-----------

mylist=['ali','vahid','reza','hamid','asal','arezoo','amir']
a_list=[]
none_list=[]
for i in mylist:
    if i[0]=='a':
        a_list.append(i)
    else:
        none_list.append(i)
        
        


#=====================================
#=====================================
#pass continiue  break
#keywords 

pass



for i in range(0,100):
    pass
    
def new(a):
    pass


class Bank:
    def __init__(a,b):
        pass

try:
    print('salam')
    
except Exception:
    pass


#for --> micharkhe i=1,2,3,4,5,,..

#if --> ag b in resid -_> ejra nakon boro badi


#ag b in rsid asan dg ejra nakon 




for i in range(0,10):
    print(i)
    
'''
0
1
2
3
4
5
6
7
8
9

'''

#----continiue --.


for i in range(0,10):
    if i==3:
        continue
    print(i)
    
    
    

    
'''
i=0  --> False , print(i) --> print(0) -->0
i=1  --> False , print(i) --> print(1) -->1
i=2  --> False , print(i) --> print(2) -->2
i=3 --> True -->  mire 4
i=4 --> False --> printI -->print94
5
6
7
8
9



0
1
2
4
5
6
7
8


exception nmeikhay

mikhay y karo baray ehame anjam bshe bejoz ye nafar
bejoz ye element
bejzo ye adad
gahbel oon akr --> if -->  continiue
'''


for i in range(0,10):
    print(i)
    if i==3:
        continue


'''
i=0 --> print(0) --> 0 --> check
i=1 --> print(1)-->1 --> mohem snist
prin(2)

0
1
2
3
4
5
6
7
8
9


'''








#----break 

'''


tooye ye list begardi
liste kh bozorge 
mikhay begar dbegard
b felan rssdii dg baghiaro nagad
bai brioon az looop
break

'''

for i in range(0,10):
    if i==3:
        break
    print(i)
    
    
'''

i=0 --> false -->print(i) -->print(0) -->0
i=1 --> false -->print(i) -->print(1) -->1
i=2 --> false -->print(i) -->print(2)) -->2
i=3 -->True --<> break -->beshko
miad edame kiod


0
1
2

'''


for i in range(0,10):
    print(i)
    if i==3:
        break
    
    
'''
i=0 --> print(0) -->0 --> false
i=1 -->pritn(1)-->1 -->false
i=2 -->print(2)-->2 --> false
i=3 -->print(3)->3 -> True--> breake

0
1
2
3


'''






#-------while----------------
#----LOOPS --> 1- for 2-while


#--> for sad tarimn
'''
for shomarande in range(start,end,step):
    dastooor
    
'''




'''
while-->

shomarande=start
while shomarande<end:
    dastooor
    shomarande=shomarandde+ step




'''


"""



for i in range(start,end,step):
    dastoor
    
    
    
i=start
while i<end:
    dastoor
    i=i+step





"""


for i in range(0,10):
    print('salam')
    
'''
i= 0,1,2,3,4,5,6,7,8,9
i=0  print(salam) -->salam
i=1
i=2
...
i=9 -->print(salam) -->salam

10 ta salam
'''

i=0
while i<10:
    print('salam')
    i=i+1
    
'''
i=0 

i=0 --> i<10 -> True -> print(slama) i=0+1-->1
i=1 -->i<10 -->True -->print(salam) i=1+1-->2
i=2
i...
i=9 -> i<10 -->True ->print(slaam) -->i=9+1=10
i=10 -->10<10 ->False 


10 ta salam 0 salam 1 salam ..9 salam
salam print mikone
....
'''

#special cases


#---------------------------
#--->bayad i tarif she
while i<10:
    print('salam')
    i=i+1
#NameError: name 'i' is not defined




#--------------
i=0
while i>10:
    print('salam')
    i=i+1
    
#ejra nmsihe
'''
i=0 --> i>10 --> 0>10 --> False --> ejra
varede halgeh nemishe
'''


i=7
while i<5:
    print('salam')
    i=i+1
'''
shart be gone e hast --> i--> True vared bshe

'''
    
#ednless loop
i=0 #tarif krdm
#while i<10:
    #print('salam')

'''
i=0  i<10 0<10 -->print(salam)
i<10 --> i=0 0<10 --> print(salam)
i<10 
i<10 -->itaghir nmikone
'''


i=0 #tarif krdm
while i<10:
    print('salam')
    i=i+1
    
#yk raveshi sharte ekhtetam dashte bashe

'''
i=0 i<10 -->true ->slam i=i+1 = i=1
...

i=9 i<10 -->true salam --> i= 9+1 = 10

i=10 10<10 -->fasle -->miad brion

hatman+1 +2 
yechizi bzarim sharto false kone
'''





'''


FINAL
while--->
while shart True hast:
    dastoor ro ejra kon
    
    
i=start
while i<end:
    dastooor
    i=i+1






i=start
while i<end:
    dastoor
    i=i+step
    

1-  hamishe shoamrande ro define kon ghable while
2- i b goone e tarif dhode bashe , Shart True bashad
3- yek chizi bzarim ekhtetam k sharto false kone


while -->
ta zamani k shart tru hast dastor ro ejra kon


i=start #hatamn bayad i ro tarif while i<.
while i<end :  #start<end --> varede halghe beshe
    datooor
    i=i+1 #ziadesh konim endlsss nashe





Error 
ejra nashe
ejra -->

'''



while False:
    print('salam')

'''
ta zamani k false hast 


while shart:
    
    
ta zamnai true
shart --> False --> false 
ejra mishe
print('salam') ->ejra nmishe
varede halgeh nemishe

'''

#while True:
    #print('salam')


'''

ta zamani k shart==True print(salam)

'''

#gahaan shoam mikhay ta abd y kar anjam bshe
#t aabd y kari najam bshe 
#ta zamani k felan shod anjam bde

while True:
    print('salam')
    sen=float(input('senet chande:'))
    if sen<18:
        break


'''
True --> salam , senet chande : 20 --> edame
True --> salam , senedt :17 ->if sen<18 if True
:-->  mishkooni

joloye endless looop -->

kh jaha tooye application ha niaz dar
y kar retry --> retry


'''



name=input('name mahsoleto begoo')
code=input('code mahsooleto begoo:')
price=input('gheymate mahsooleto begoo:')

text=f'''
product name : {name}
product code : {code}
    total price : {price}

'''
print(text)
answer=input('aya shoma confirm mikoni (yes,no)')

if answer.lower().strip()=='yes':
    print('sabt shod')
elif answer.lower().strip()=='no':
    print('motasefane sabt nashod')
else:
    print('ya yes bego ya no begoo')




#ta zamani k taraf mige No 
#chiakr kon? hey barash bair biar




while True:
    name=input('name mahsoleto begoo')
    code=input('code mahsooleto begoo:')
    price=input('gheymate mahsooleto begoo:')

    text=f'''
    product name : {name}
    product code : {code}
        total price : {price}

    '''
    print(text)
    
    answer=input('aya confirm mikoni etalato? (yes/no):')
    
    if answer.lower().strip()=='yes':
        print('mahsoole shoam ba moafaghiat sabt shod')
        break
    
    print('mojadad emtehan konid ......')
        






'''
L7 --> function vs Class
'''














#-------function----------------







