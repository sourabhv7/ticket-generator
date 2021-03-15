#ticket fare generator
import time
import datetime
import random
def intro():
    print("*"*10,'Welcome to iBus by AiCTSL Indore','*'*10)
    for i in range(56):
        print('*',end='')
        time.sleep(0.05)
    print('\nPlease enter your current and destination stop name.\n')
    time.sleep(0.2)
    print('Rajeev Gandhi Square : RGS')
    time.sleep(0.2)
    print('Mata Gujri College   : MGC')
    time.sleep(0.2)
    print('Vishnupuri           : VNP')
    time.sleep(0.2)
    print('Bhawarkua            : BWR')
    time.sleep(0.2)
    print('Holkar Subway        : HSW')
    time.sleep(0.2)
    print('Navalkha             : NLK')
    time.sleep(0.2)
    print('Indira Pratima       : INP')
    time.sleep(0.2)
    print('GPO                  : GPO')
    time.sleep(0.2)
    print('Shivaji Vatika       : SVK')
    time.sleep(0.2)
    print('AICTSL               : AIC')
    time.sleep(0.2)
    print('Geeta Bhawan         : GTB')
    time.sleep(0.2)
    print('Palasia              : PLS')
    time.sleep(0.2)
    print('Indusrty House       : INH')
    time.sleep(0.2)
    print('LIG                  : LIG')
    time.sleep(0.2)
    print('Press Complex        : PCX')
    time.sleep(0.2)
    print('MR9                  : MR9')
    time.sleep(0.2)
    print('Vijay Nagar          : VJN')
    time.sleep(0.2)
    print('Satya Sai            : STS')
    time.sleep(0.2)
    print('Shalimar Township    : STW')
    time.sleep(0.2)
    print('Scheme No. 78        : S78')
    time.sleep(0.2)
    print('Niranjanpur          : NRP')

def dec(x):
    distance = {
    'RGS' : {'dist' : 0,"name":'Rajeev Gandhi ' },       #Rajeev Gandhi Square 
    'MGC' : {'dist' : 0.45,"name":'Mata Gujri College ' },    #Mata Gujri College
    'VNP' : {'dist' : 0.85,"name":'Vishnupuri ' },    #Vishnupuri
    'BWR' : {'dist' : 1.30,"name":'Bhawarkua '},    #Bhawarkua
    'HSW' : {'dist' : 1.90,"name":'Holkar Subway '},    #Holkar Subway
    'NLK' : {'dist' : 2.60,"name":'Navalakha '},    #Navalakha
    'INP' : {'dist' : 3.20,"name":'Indra Pratima'},     #Indra Pratima
    'GPO' : {'dist' : 3.80,"name":'GPO '},              #GPO
    'SVK' : {'dist' : 4.45,"name":'Shivaji Vatika '},   #Shivaji Vatika
    'AIC' : {'dist' : 4.90,"name":'AICTSL '},        #AICTSL
    'GTB' : {'dist' : 5.40,"name":'Geeta Bhawan '},     #Geeta bhawan
    'PLS' : {'dist' : 6.10,"name":'Palasia '},          #palasia
    'INH' : {'dist' : 6.60,"name":'Industry House '},   #Industry House
    'LIG' : {'dist' : 7.20,"name":'LIG '},              #LIG
    'PCX' : {'dist' : 7.60,"name":'Press Complex '},    #Press Complex
    'MR9' : {'dist' : 8.30,"name":'MR9 '},              #MR9
    'VJN' : {'dist' : 8.90,"name":'Vijay Nagar '},      #Vijay Nagar
    'STS' : {'dist' : 9.60,"name":'Satya Sai '},        #Satya Sai
    'STW' : {'dist' : 10.50,"name":'Shalimar Township '},#GPO
    'S78' : {'dist' : 10.90,"name":'Scheme No. 78 '},   #Scheme No. 7
    'NRP' : {'dist' : 11.40,"name":'Niranjanpur '},     #Niranjanpur
    }
    return distance.get(x)
intro()
try:
    start = input("\nEnter your current stop : ")
    start = start.upper()
    lives = dec(start)
    live = lives.get('dist')
    name1 = lives.get('name')

    stop = input("Enter your destination stop : ")
    stop = stop.upper()
    dests = dec(stop)
    dest = dests.get('dist')
    name2 = dests.get('name')
    if live > dest :
        distance = live - dest
    else:
        distance = dest - live


    if distance <= 2:
        fare = 5
    elif distance > 2 and distance <=4:
        fare = 10
    elif distance > 4 and distance <=6:
        fare = 15
    elif distance > 6 and distance <=14:
        fare = 20
    elif distance > 14 and distance <=22:
        fare = 25
    else:
        fare = 30

    print('\n\n',"*"*10,'Welcome to iBus by AiCTSL Indore','*'*10)
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%I %M %S %p')
    print('Date            :',date)
    print('Time            :',time)
    print('Ticket No.      :',random.randrange(10000,20000))
    print('From            :',name1)
    print('To              :',name2)
    print("Travel Distance :",distance, "km")
    print('-'*54)
    print("Fare Rs.        :",fare)
    print('-'*54)

except:
    print("Sorry !!! Stop not found.")
    print("Please try again wth right keyword/code.")











