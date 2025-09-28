"""
Created on Sun Sep 14 20:07:18 2025



ADVANCED LESSON 3

ADV_L3.PY


"""

#----review------

'''

order----> programming

Human (en) <----------- interface ---------> Machine (Binary 0,1)

interface--> programming language
--> C  , C++ , JAVA, Python

python--> yek zaban
vocab , grammar

--------jahane python -->3 ------

#------reserved words----

1-python built in function --> print() len() type()

2-keywords --> if , else , for , while , ......

#------unreserved words-------
3- variables --> moteghayer ha ---> zarf

esme zarf , value (meghdar)


3.1. Numbers ( int, float, complex)
3.2. Boolean ( True ,False)
3.3. String ( hrf , '') asssign , index [] [ : ] str fucntions
3.4. Iterables




#-----str functions--->
yekseri fucntion hastan k fght baraye str ha hastan
lower() upper() .......


print()
lower()


zarf=...

zarf.lower()

in tabe -_> emal nemikone, khoroji midahad

'''

a='salam'


a.upper() #Out[1]: 'SALAM'

print(a) #salam


b=a.upper()
print(b) #SALAM

'''

str functions-------

1--> miad rooey khdoe kalame kari mikone
upper() 
lower()
title()
capitalize()



2---->adad pas mide

zarf.count('a') --> chanta a vojod
zarf.find('a') --> indexe 


zarf='alipilehvar'
      012345678910
      
      
3---> soal javab is , True , False

islower()

zarf.islower() 

'''

zarf='alipilehvar'

#----1---
zarf.upper() #'ALIPILEHVAR'
zarf.lower()
zarf.title() #'Alipilehvar'

#zarf.replace('ghadimi','jadid')

zarf='ali'

zarf.replace('a','b') # 'bli'


zarf=' salam'
zarf.replace(' ','') #'salam'






#strip() az chap va rast fasele haaro hazf mikone

zarf='  salam'
zarf.strip() # 'salam'


a='salam'
b=' salam'
print(a==b) #fALSE

c=b.strip()

print(c==a) #True



#_-split

#spit(',')

jomle='salam, dfostan khosh oomadid, be khaneye khdoetan'

jomle.split(',')
# ['salam', ' dfostan khosh oomadid', ' be khaneye khdoetan']




#---2----
zarf.count('a') #2
zarf.find('p') #3



#3-------

zarf.islower() #True
zarf.isupper() #False



a='salam'
b=' salam'
print(a==b) #False


print(len(a)) #5
print(len(b)) #6

#a -> s a l a m
#b --> space s a l a m

a[0]  #'s'
b[0] #' '

print(a==b) #False





#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================
#=================================

#shabih saz

#len() type()

b=input('adad benevisid:')

b=43



a=40

print(a)


#-----------------------------------
#----> Mesale emroooz

'''

Amazon, digikala


side foroshande 
esme mahsole , code mahsoole , gheyamtesho

inaro zakhriekonim

'''


name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')


text='''
------sherkate plutus------

name mahsool : name
code mahsool : code
 
gheymate kol : price


aya shoma in etelaat ro taed mikonid?
'''

print(text)



a=100


print('salam man a hastam') #salam man a hastam

print(f'salam man a hastam') #f bezan

print(f'salam man {a} hastam')
#salam man 100 hastam


#-------------------------------

name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')


text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman


aya shoma in etelaat ro taed mikonid?
'''

print(text)


'''

------sherkate plutus------

name mahsool : nvidia
code mahsool : n100

gheymate kol : 10000 toman


aya shoma in etelaat ro taed mikonid?
'''


#-------------------------
#-------------------------

'''
1--python built in function print ,...
2-keywords
3-variables ... (number,str, boolean,....)




keywords---> if ha

1- only if

2- if else

3- if elif else


shart, agar , ama , dorahi, serahi , cahnrahi --> IF
'''



print('salam')







'''


if shart:
    dastor1
    dastoor2
    dastoor2
    




shart --> True , False

== != > <
islower() isupper() ......
--> shart


True -->


'''










#a=10



if a>5:
    print('salam')
    



print('khodafez')    

#------------------
#--> if --> ye rah zane
#migrdi beyen 



a=20

#print(a>10)


if a>10:
    print('salam')
    
  
print('khodafez')


#salam khodafez




a=5

if a>10:
    print('salam')
    
print('khodafez')


#yek shart yek dastor

if a>10:
    print('sa;a,')
    print('khoobi')
    print('chekhabar')


#age khasti chant shart


#if a>10:
#    if b>6:
        
'''

shart1 , shart2




hatman har joftr sharta doros bashe --> hadeghal joftesh
sharte yek ba sharte 2 /. sharey ham sharte 2

And





yekia z sharta , hadeghal yeki , sharteyek YAAA hsarte 2
Or



if shart1 and shart2:
    dastoor1
    dastoor23
    dstooor3
    
    
    
if shart1 or shart2:
    dastoor1
    dastoor2
    dastooor3
    
    





#----- 1-nly if -->
mikhay fght yek bakhsh ( kasani k shart barashon True msihe)
yek gehsmati ejr abshe
yek khat cod,e sadf khjat code

age shart True bashe jra she
ag shart False --> Bemanche ?? 



#---2---if , else
age true shod in karo kon
ag nashdo (nemigi bikhial) oonkaro kon


age shart true shod --> kare 1
age shart false shod --> kare 2



--> dorahi baz mikoni

if else




if shart:
    dastoor1
else:
    dastoor2
    
    
    
    

if shart:
    dastoor1
    dastoor 1 1
    dastoor 1 1 1 
else:
    dastoor2
    dastooor 2 2 2 2    
    
    
    
print()-->hame yeksane
    
    

'''




a=10


if a>5:
    print('bozorgi')
    
else:
    print('kochiki')






a=4
if a>5:
    print('bozorgi')


#Nothign
#ag shart false --> bemanche....





a=4

if a>5:
    print('bzorg')
else:
    print('koochik')


#koochik


'''

1-python built in function ----> print() input() 
2-keywords -0., if , else, if elif 

3-variable --.zakhrie (number,str,....)



#---->
agar, ama , yekseri, condition, sharayet, dorahi, chanrhai


#---1-only if
yek gehsmati az code (ye khat, chan khat)
yekseri --> fght shart> True

if shart:
    dastoor
    da
    das
    da
    
    
shartesh falkse--> hcih etefgahi vashash hich barname ee ndrim


#----2--if else
dorahi besazi
age inshod in, ag oon shod oon
ag shart true shod kare 1 , agf false shod (bikhial na) kare 2
dorahu


if shart:
    dastoor
    dastoor
else:
    dastoor
    dastoor



#3---3 if eif else


if shart1:
    dastoor1
    
elif shart2 :
    dastoor2
else:
    dastoor3
    
    

    


'''
sen=100000000932749276
#only if

#sen 20 --> salam
#sen 17 --> hich
#sen 10 =-->? hich



if sen>18:
    print('saalam')




#---if else
#dorahi
#20 --> salam
#17 --> mamnoo
#14--->mamnooo


if sen>18:
    print('salam')
else:
    print('mamnoo')


#if elif else??

#20-->salamn
#17 --> rezyaat madar
#14 --> mamnooo

if sen>18:
    print('salam')
elif sen>15:
    print('rezayate madar')
else:
    print('mamnoooo')



#---------------------------------------
name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')


text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman
'''
print(text)

answer=input('aya etelaate bala ro taeed mikonid?:')

if answer=='yes':
    print('tabrik migam sabt shod')

'''

if shart:
    ddastooor

shart --> True , False


answer>10

anser='yes'
answer='no'
answer='.....'

answer=yes neveshte

comparison True False

answer == 'yes'

'''

#-----------------------------------------
#ag gof yes --> tabrik sabt shod
#ag gof na (bikhial)--> sabt nashod motasefane

name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')


text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman
'''
print(text)

answer=input('aya etelaate bala ro taeed mikonid?:')

if answer=='yes':
    print('tabrik sabt shod')
else:
    print('motasefane sabt nashod')
    
    
#-------advanced manager------

name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')
text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman
'''
print(text)

answer=input('aya etelaate bala ro taeed mikonid?:')

#3 rah
#2 rah --> answer==yes 

if answer=='yes':
    print('tabrik sabt shod')
elif answer=='no':
    print('sabt nashode')
else:
    print('lotfan ba yes ya no javab dahid, javabe shomna na yese na no')
    
    
    
    



#==================================
'''
adv_l4

iterables ---> list, tuple, set , dictioanry
for , while --> 

'''
    

name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')
text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman
'''
print(text)

answer=input('aya etelaate bala ro taeed mikonid?:')


if answer=='yes':
    print('sabt shod')

#aya etelaate bala ro taeed mikonid?:Yes

a='yes'
b='Yes'

print(a==b) #False

a[0]
b[0]

#if answer=='yes' or answer=='Yes':

#yes
#YES
#Yes
#yEs
#yES
#yeS

answer=input('aya etelaate bala ro taeed mikonid?:')

new_answer=answer.lower()

if new_answer=='yes':
    print('sabt shod')
    
    
    


answer=input('aya etelaate bala ro taeed mikonid?:')

new_answer=answer.upper()

if new_answer=='YES':
    print('sabt shod')
    
    
    
    

#---------------
answer=input('aya etelaate bala ro taeed mikonid?:')
if answer.lower()=='yes':
    print('sabt shod')
    




#aya etelaate bala ro taeed mikonid?: yes






#---final version0-------

name=input('Lotfan esme mahsooleton ro begoo:')
code=input('lotfan code mahsooleton ro begoo:')
price=input('lotfan gheymate mahsooleton ro begoo:')
text=f'''
------sherkate plutus------

name mahsool : {name}
code mahsool : {code}
 
gheymate kol : {price} toman
'''
print(text)

answer=input('aya etelaate bala ro taeed mikonid?:')

#3 rah
#2 rah --> answer==yes 

if answer.lower().strip()=='yes':
    print('tabrik sabt shod')
elif answer.lower().strip()=='no':
    print('sabt nashode')
else:
    print('lotfan ba yes ya no javab dahid, javabe shomna na yese na no')
    
    
    
#answer='  YES'
#answer2=answer.lower()    
#answer3=answer.lower().strip()







