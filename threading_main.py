# gashveba
# > python threading_main.py *failis saxeli*
# failshi unda eweros ert sityvad rame 

import sys
import threading

argument = sys.argv[1:]
argumentebis_sigrdze = len(sys.argv)

def operation(a):
    with open(a) as file:
        kitxva = file.read()
    
    result= ""
    wera = open(a, "w")

    print('dzveli teqsti: ', kitxva)

    for char in kitxva:
        if(char.isupper()):
            result+= char.lower()
        elif(char.islower()):
            result += char.upper()
        elif(char == " "):
            result += " "
    wera.write(result)
    print('axali teqsti: ', result, '\n')

# egi racxa threadis gareshe
# def main():
#     print('\ndasamushavebeli failebi: ', argument, '\n')
#     for x in range(argumentebis_sigrdze - 1):
#         operation(argument[x])

def main():
    print('\ndasamushavebeli failebi: ', argument, '\n')
    for x in range(argumentebis_sigrdze - 1):
        thread = threading.Thread(target = operation,args=(argument[x],))
        thread.start()
      
main()

