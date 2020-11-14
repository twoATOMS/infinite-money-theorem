# Infinite monkey theorem
import random
import string
import time

shakespeare = 'methinks it is like a weasel'
alfabet = string.ascii_lowercase + ' ' # 'abcdefghijklmnopqrstuvwxyz '


# O functie care genereaza aleator 28 de litere, inclusiv spatiu gol
def maimuta():
    fraza_maimuta = list()
    for each in shakespeare:
        fraza_maimuta.append(random.choice(alfabet))
    return ''.join(fraza_maimuta) # str


# O functie care compara fraza maimutei cu citatul din shakespeare si ofera un scor - de la 0 la 28  
def scor(sir_generat):
    scorul = int()
    for each_shake, each_sir_generat in zip(shakespeare, sir_generat):
        if each_shake == each_sir_generat:
            scorul += 1
    return scorul # int


# O functie loop pentru fraza maimutei si scorul ei
def repetitie():
    fraza = maimuta()
    repetare = int()
    best_so_far = str()

    while scor(fraza) < scor(shakespeare):
        time.sleep(0.05)
        if repetare == 1000: # la 1000 de repetitii printeaza cel mai bun scor
            print('-'*20)
            print("BEST SO FAR:",best_so_far, scor(best_so_far))
            print('-'*20)
            repetare = 0

        if scor(fraza) > scor(best_so_far):
            best_so_far = fraza

        else:
            print(fraza, scor(fraza))

            fraza = maimuta()
            repetare += 1

    print('Fraza finala:',fraza, scor(fraza))

                                 

if __name__=='__main__':
    repetitie()
