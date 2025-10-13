
"""
In The Name of GOD

Created on Sun Oct 12 20:02:45 2025

@author: Ali Pilehvar Meibody

ADV__L5


"""


'''

Human ----- Interface ----- Machine


Interface --> Programing language --> Python

python mese ye sensan az bvala b paeen az chap b rast mnikhone
khat b khat


python----------
1- Built in functions (print(),len(),type(),open(),input())
2-keywords ( if , if else, if elif else , for , while , and , or )

3-Variables --> sefid --> esm zarf dar nazar

3.1.Numbers (int, float, complex) ** * + - 
a=10 , b=10 , c=a+b , == != > < --> True False
3.2. Boolean (True,False)
3.3string (harchi reshte , character sadsdgaajh 2178126 '')
zarf='ali' --> zarf[index] zarf[start:end+1] str functions
zarf.esm_function()
khoroji mide, emal nmishe
a='ali'
a.upper() ---> ALI
a hamon aliue
b=a.upper()
--> 1-.upper() .lower() 2..count('a') .find('a') 3-islower() .isdigit()

3.4.Iterables --> tooye  zarf yedone value berizim , chnata value

--> Iterables --> chanta chiz dakheel yek zarf ja begire
List, tuple , set , dictionary

3.4.1--> List --> ordered [index] , changable , allow duplicated

a=[10,20,30,'ali',True,2.32,1j]
a[index]
a[start_index:end_index]
a[4]=10000 chjangable
list functikons --> .append() .insert() . -->emal mishod , khoroji 

a=[10,20]
a.insert(2,100)

a--> [10,20,100]


3.4.2. Tuple --> Data base --> ordered , unchangable , allow duplciazte
a=(10,20,30,40)
a[10] XXXXXXXXX


3.4.3. Set --> unordered , unchangable , duplicated no
A={10,20,30}



a=(10,20,30)
#tuple --> list
b=list(a)
set()  tuple()
Conversion
convert



3.4.4. Dictionary 

index value
0      10
1     43223
2     4334


zarf[index]
zarf[0]-->10


key value
id   100
name ali
balance 2003223
car   bmw

zarf['id']--> 100
zarf['karte_meli']

'''


code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=input('gheymate mahsooleto vared kon:')

text=f'''

------PLUTUS--------

product name : {name}

product code: {code}
    
    
    
    Total price: {price}
        


'''

print(text)

answer=input('aya shoam msohakhasat ro taeed mikonid? (yes/no):')

#== > < !=
#yes Yes yEs yeS YEs yES YeS YES  yes  yes 
if answer.lower().strip()=='yes':
    print('tabrik migam sabt shod')
elif answer.lower().strip()=='no':
    print('motasefane sabt nashod')
else:
    print('lotfan ba yes ya no javab bdid')

#----------------
#---------------

code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=input('gheymate mahsooleto vared kon:')

#new_price= (100/100 * price) - (20/100 * price )
#new_price=price - 0.2*price
new_price  = 0.8*price


text=f'''

------PLUTUS--------

product name : {name}

product code: {code}
    
    Total price: {new_price}
        


'''
print(text)

answer=input('aya shoam msohakhasat ro taeed mikonid? (yes/no):')

if answer.lower().strip()=='yes':
    print('tabrik migam sabt shod')
elif answer.lower().strip()=='no':
    print('motasefane sabt nashod')
else:
    print('lotfan ba yes ya no javab bdid')
    
    




#=======================

code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=float(input('gheymate mahsooleto vared kon:'))

#new_price=float(price)
'''
print(price) #1000
print(type(price)) #<class 'str'>

#'1000'

price/2 #TypeError: unsupported operand type(s) for /: 'str' and 'int'

#nm=umber
'''

text=f'''

------PLUTUS--------

product name : {name}

product code: {code}
    
    Total price: {0.8*price}
        


'''
print(text)

answer=input('aya shoam msohakhasat ro taeed mikonid? (yes/no):')

if answer.lower().strip()=='yes':
    print('tabrik migam sabt shod')
elif answer.lower().strip()=='no':
    print('motasefane sabt nashod')
else:
    print('lotfan ba yes ya no javab bdid')
    

'''
-----PLUTUS--------

product name : nvidia

product code: l100
    
    Total price: 8000.0
'''

#tabrik migam sabt shod



#------LAST ERROR--------

code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
pre_price=input('gheymate mahsooleto vared kon:')

#--check konam pre_price
#ag adad bashe 
#price=float(pre_price)
#age nabood
#benevbism agah lotfan adad bzn

#str --> str functions --> is --> True false --> SHaret

#isdigit

#zarf.isdigit() --> True , False


if pre_price.isdigit():
    price=float(pre_price)
    text=f'''

    ------PLUTUS--------

    product name : {name}

    product code: {code}
        
        Total price: {0.8*price}
            


    '''
    print(text)

    answer=input('aya shoam msohakhasat ro taeed mikonid? (yes/no):')

    if answer.lower().strip()=='yes':
        print('tabrik migam sabt shod')
    elif answer.lower().strip()=='no':
        print('motasefane sabt nashod')
    else:
        print('lotfan ba yes ya no javab bdid')
        
else:
    print('lotfan adad vared namaaed')
    
    
    
    
    
    








#---------TASK ADV_L4
#--------------------------------
#task1
#tooye yek list berize az list bekeshe biron

products=[]

code=input('lotfan code mahsoleto vared kon:')
products.append(code)


name=input('name mahsooelto vared kon:')
products.append(name)

price=input('gheymate mahsooleto vared kon:')
products.append(price)


text=f'''

------PLUTUS--------

product name : {products[1]}

product code: {products[0]}
    
    Total price: {products[2]}
        


'''
print(text)




#------


code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=input('gheymate mahsooleto vared kon:')


text=f'''

------PLUTUS--------

product name : {products[1]}

product code: {products[0]}
    
    Total price: {products[2]}
        


'''
print(text)


#--------dictionary

code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=input('gheymate mahsooleto vared kon:')

products={ 'code':code , 'name':name , 'price' :price  }

'''
producst

key    value
code  l1000
name   nvidia
price  1000


'''


text=f'''

------PLUTUS--------

product name : {products['name']}

product code: {products['code']}
    
    Total price: {products['price']}
        


'''
print(text)



#task 5 ---------------
#hamaro berize too tuple

code=input('lotfan code mahsoleto vared kon:')
name=input('name mahsooelto vared kon:')
price=input('gheymate mahsooleto vared kon:')
products=(code,name,price) #tuple

myprice=products[2]

#products[2]=float(myprice)*0.8 #tuple ghabel etaghir nist XXXXX
#TypeError: 'tuple' object does not support item assignment

products_list=list(products)

products_list[2]=float(myprice)*0.8

products_tuple=tuple(products_list)


text=f'''

------PLUTUS--------

product name : {products_tuple[1]}

product code: {products_tuple[0]}
    
    Total price: {products_tuple[2]}
        


'''
print(text)




#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#================================================

'''

python az bala b paeen az chap b rast
khat b lkhat ejra mikoni

mantegho beham bzni --> Keywords (banafsh)


if --> yeki az keywords --> Shart ha (condition)


'''
#-----Keywords

print('salam')




sen=18


if sen>20:
    print('salam')



#------------------

print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')



#------------------
'''


manteghe halghe ha

'''

#adi nis

print('salam')


#repeat(10):
#    print('salam')


#----------------
#yerchi benvisi:
    #codi khati k mikhay tekrar bshe




#-----------FOR------------

'''

ye khat

khat1
khat2
khat3




for i in range(0,100):
    y khat


for i in range(0,100):
    khatr1
    khat2
    khat3


'''


'''

Python vase inke betone yek khat ro ejra kone
bayad yechi bashe bename shomarande k beshmore



repeat(10)



az in adad ta in adad
az inja t ainja 
inkaro kon



azinja 0 ta 10 code ziro ejra kon

shomarnde ->0 ejra mikonam
1 ---?>ejra mikonam
2-->ejra mikonm
3-->ejra mionm
.....
9 --> ejra mikonam


'''


print('salam')







for i in [0,1,2,3,4,5]:
    print('salam')

'''
be ezaye har i i ke dar in list hast --> code zir ro ejra kon

j , k , l , m , n ,
[0,1]  harchi mikhay bashe
print(???) --> a+b 2+43

code1
code2
code3


'''


for i in [0,1,2,3,4,5]:
    print('salam')
    
    
    
'''
i=0 ---> print('salam') --> salam
i=1 --->print('salam') --> salam
i=2 --> print('salam') -->salam
i=3 -->print('salam') --> salam
i=4 -->print('salam') --> salam
i=5 --> print('salam') --> salam



salam
salam
salam
salam
salam
salam


'''

#------> sade tarin hgalate
for i in [0,1,2,3,4]:
    print('khobi')
    
'''
be zaye har i i k dar in list has
i=0 ---> print('khobi') ---> khobi
i=1 ---> print('khobi') ---> khobi
i=2 ---> print('khobi') ---> khobi
i=3 ---> print('khobi') ---> khobi
i=4 ---> print('khobi') ---> khobi
'''


#---> bvahse ye khat code, chan khat codo anjam bde
for i in [0,1,2,3,4]:
    print('salam')
    print('khobi')
    print('chekahabr')
    

'''
i=0 ---> 3 khato baham ejra mikone --> salam khobi chekahabr
i=1 ---> 3 khato baham ejra mikone --> salam khobi chekahabr
i=2 ---> 3 khato baham ejra mikone --> salam khobi chekahabr
i=3 ---> 3 khato baham ejra mikone -->salam khobi chekahabr
i=4 ---> 3 khato baham ejra mikone -->salam khobi chekahabr
'''


#-----> hamishe print?
#be zye hr i i k dar in list has --> code zir ro ejra kon
a=0

for i in [0,1,2,3,4]:
    b=a+2
    a=a+1



'''
b ezaye i dar 0,1,2,3,4

i=0  --> b=2 ,a=1
i=1 --> b=3 , a=2
i=2 --> b=4 , a=3
i=3 -->b=5 , a=4
i=4 -->b=6 , a=5

b-->6
'''


for i in [1,2,3,4,5]:
    print('salam')
    
    
'''
be ezaye i haee k in list hast code ro ejkra kon

i=1 --> print('salam')---> salam
i=2 --> print('salam')-->salam
i=3 -->prinjmt('salam')-->salam
i=4 --> print('salam')-->salam
i=5 -->print('salam')-->salam



'''

for i in [1,2,3,4,5]:
    print(i)
    
    
'''
b ezaye i haee k dar [] code ro ejra mikone

i=1-->print(i) --> print(1)--->1
i=2 -->print(i) -->print(2)-->2
i=3-->print(i) -->print(3)-->3
i=4 -->print(i) -->print(4)-->4
i=5 -->print(i) -->print(5)-->5




1
2
3
4
5

'''
    
    




a=0

for i in [0,1,2,3,4]:
    b=a+2
    a=a+1


'''
be zaye i haee k dar in list [0 ,1,2,3,4] -- broo code paeno ejra kon


i=0 ---> b=2 , a=1 
i=1 --> b=3 , a=2
i=2 --> b=4 ,a =3
i=3---> b=5 , a=4
i=4 --> b=6 , a=5
miad biron az for


b ezaye i hae k list in amaliato anjam 

'''


print(a)
#5

print(b)
#6



for i in [0,1,2,3,4]:
    print('salam')
    print('khoobi')
    
    
print('chekahbar')


'''
i=0
salam
khoobi
i=1
salam
khoobi
i=2
salam
khoobi
i=3
salam
khoobi
i=4
salam
khoobi



chekahbar

'''



#ta 100 baram ejra kon


#for i in [0,1,2,3,4,5,6,7,.....,100]???

#-->tabe --> range()

range() #tabeye dakheli

#range(end)  -. 0 ta end
#range(start,end) ->start ta end 

range(100) #--->[0,1,2,3.......,99]
range(0,100) #--> [0,1,2,3,4.......,99]
range(10,100) #-->[10,11,12,13,....,99]


#for i in [2,3,4,5,6,....,99]


for i in range(2,100):
    print('salam')
    
    
    
'''
be ezaye har i i k dar in [] range(2,100)-->[2,3,4...,99]

i=2 --> print('salam') -->salam
i=3 -->print('salam'0) -->salam
...
.

.

.

i=99 -->print('salam') -->salam







'''


a=0

for i in range(0,101):
    b=a+2
    a=a+1
    


print(b)
    


'''
be ezaye i dar [0,1,2,3....,100]
b=a+2
a=a+1

i=0  
b=a+2
a=a+1



i=1
b=a+2
a=a+1

i=2
b=a+2
a=a+1

'''


    
a=0

for i in range(0,101):
    b=a+2
    a=a+1
    


print(b)

'''
i=0 --> b=0+2=2  , a=0+1=1
i=1 --> b=1+2=3  , a=1+1=2
i=2 -->b=4 ,a =3
i=3
i=4
i=100--->b=102 ,a=101

'''

print(b) #-->b=102
#102
    



#range(start,end)

#range(0,101)




#range(100) #---> [0,1,2,3,4,6,7,8,9,.....,99]
#range(0,100)

#range(0,100,1) #az 0 ta 100 1 ki 1 ki boro 


#range(0,100,2) #-->0 2 4 6 8 10 


for i in range(0,10,2):
    print(i)
    
    
'''
range(0,10,2) -->[0,2,4,6,8]

i=0 -->print(i) -->print(0) -->0
i=2-->print(i) --> print(2)-->2
i=4-->print(i)
i=6-->print(i)
i=8 -->print(i)



0
2
4
6
8

'''




for i in range(0,10,2):
    print('salam')



'''
range(start,end+1,2ta) 0 ta 10 
 0 2 4 6 8 i-->
 
 i=0 --> print('salam') -->salam
 i=2 --> print('salam') -->salam
 i=4 --> --> print('salam') -->salam
 i=6 --> print('salam') -->salam
 i=8 --> print('salam') -->salam


salam
salam
salam
salam
salam
'''
    


#---------------------------------

'''

for i in list,range:
    codi 
    cod haee 
    
    
    
code-->print('salam')

code -->print(i)

a+2



range(end) -->0,....
\rangge(start,end) [start ,....end-1]
range(star,end,step) [start,start+step,.....]


listy , range 

i= --.code ,codha ejra mikni
i=


b e tahesh

va az halgeh moay birooon




FOR---------
1-application --> tekrar hast
2-iteration -->



'''


for i in [0,1,2,3,4]:
    print(i)


#danesh amooza
mylist=['ali','reza','hamid','vahid']
for i in mylist:
    print(i)

#ba


for i in ['ali','reza','hamid','vahid']:
    print(i)

'''

i=ali --> print(ali)-->ali
i=reza -->print(reza)-->reza
   hamid
   vahid




'''



#print XXXXXXXX

mylist=['ali','reza','hamid','vahid']
for i in mylist:
    print(i)
    
    
#varede list ??

#ye skahtemone koli adam tooshe
#mitonm otgah b otagg
#khoen b khone
#afrado bekesham biron brizameshon toye i
#va harkari delam khas bahashon

#checkhson konm
#hazfesho konm
#taghireshon bdm
#.....


#VARRESIIII , bazreesi

#iteration--->

#list,set,-->iterables

#-->ghabeliat tooshon iteration zad



'''

adv_l6
iteration -->
while (for tafavot)

DEF





adv_l7
Class ha
System --> bank management ro rah mindazimm
az revolet --> bank accounting app
zzirsakht -->


'''












