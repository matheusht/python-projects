from datetime import date
from datetime import datetime
from time import strftime

today = date.today()
now = datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

NOME = str(input('qual seu nome PORRA \n'))
DUO = str(input('qual foi seu ultimo duo PORRA \n'))

if DUO == 'matheus': 
    print('duo AGORA {} Mitinho Jr. {} '.format(NOME,date_time))
else:
    print('fake friend')