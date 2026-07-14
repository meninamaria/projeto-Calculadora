from pathlib import Path
from PyQt5 import uic, QtWidgets

display = []
calc = []
count = 0
aux = 0
aux2 = 0
negativo = 0
operador = ''
operador2 = ''
passos = 0
alterou = 1


# mostrar os valores na tela da calculadora
def print_screen(button=0):
    global display, passos, operador, count, aux, calc, alterou, aux2
    screen = ''

    # verificar se existe elementos na lista
    if len(display) >= 1:
        # apagar o último elemento
        if button==1:
            for j in range(0, len(display)):
                if j!=0:
                    # aqui é pra ver se o usuário vai apagar um número ou operador
                    if display[j] in '1234567890':
                        if display[j-1] in '+-×÷':
                            break
                            
            if display[-1] in '+-×÷':
                if negativo==0:
                    passos-=1

            del display[-1]

            # aqui é quando o usuário que exclui todos os valores que estão na lista
            if len(display) == 0:
                operador=''
                count = 0
                aux = 0
                passos = 0

            if len(calc) >= 1:
                del calc[-1]     

            # aqui é a atualização do COUNT quando os números e operadores são apagados (é pra ser né...)
            calc=[]
            aux2 = ''
            if len(display) == 1:
                if display[0] in '1234567890':
                    calc.append(display[0]) 
                    aux2+=display[0]
                    alterou=1
            else:
                for i in range(0, len(display)):  
                    if i != 0:
                        if display[i] in '1234567890':
                            if display[i-1] != '+' and display[i-1] != '-' and display[i-1] != '×' and display[i-1] != '÷':
                                calc.append(display[i-1]) 
                                aux2+=display[i-1]
                                alterou=1

                        if len(calc) == 0:
                            calc.append(display[0]) 
                            aux2+=display[0]
                            alterou=1
                            break
                        
                        if i == len(display)-1:
                            if display[i] in '1234567890':
                                calc.append(display[i]) 
                                aux2+=display[i]
                                alterou=1
        
            if alterou == 1:
                count = float(aux2)
                calc=[]
                alterou=0
                if negativo==0:
                    passos=1

            

        # quando o usuário não clica na opção de apagar o último elemento   
        else:
            for j in range(0, len(display)):
                if j!=0:
                    # aqui é pra verificar se existem dois operadores em sequência (O QUE NÃO PODE ACONTECER)
                    if display[j] in '+-×÷':
                        if display[j-1] in '+-×÷':
                            # caso tenha dois sinais sem ser o -
                            if display[j] != '-':
                                passos-=1

                            del display[j]


    for i in range(0, len(display)):
        screen += display[i]
        
    calculadora.display.setText(screen)

     
# aqui é pra pegar o número que está na lista DISPLAY e colocar na variável AUX para que os valores sejam armazenados
def numbers():
    global aux, display, count, passos, negativo, calc, operador2, operador

    for j in range(0, len(display)):
        if count == 0:
            if display[0] == '-':
                negativo=1
        if negativo==0: 
            if j!=0:
                if display[j] == '-':
                    if display[j-1] == '+' or display[j-1] == '×' or display[j-1] == '÷':
                        if display[j-1] == '÷':
                            operador2='/'
                        elif display[j-1] == '×':
                            operador2='*'
                        else:
                            operador2 = display[j-1]

                        if operador == '':
                            passos=1
                        operador = operador2
                        negativo=1

    
    for i in range(0, len(calc)):
        if calc[i] == '+' or calc[i] == '-' or calc[i] == '×' or calc[i] == '÷' :
            del calc[i]


    if len(calc) >= 1:
        aux = ''.join(calc)
        if count == 0 and passos == 0:
            if negativo==1:
                count = float(aux)*(-1)
                negativo=0
            else:
                count = float(aux)
        else:
            if negativo==1:
                aux = float(aux)*(-1)
                negativo=0
            else:
                aux = float(aux)

        passos+=1
        
    calc=[]


# aqui é onde tem as operations
def math(operador):
    global count, aux, passos, display


    if operador == '+':
        count += aux
        calculadora.display.setText(str(count))
    if operador == '-':
        count -= aux
        calculadora.display.setText(str(count))
    if operador == '*':
        count *= aux
        calculadora.display.setText(str(count))
    if operador == '/':
        if aux == 0:
            calculadora.display.setText("Cannot divide by zero")
            count = 0
            aux = ''
            operador = ''
        else:
            count /= aux
            calculadora.display.setText(str(count))
    if operador == '=':
        calculadora.display.setText(str(count))   

    passos = 0


# diferenciar os números dos passos
def operations_math():
    global count, aux, passos, display

    if passos == 4:
        if display[0] == '-':
            math(operador)
    elif passos == 3:
        math(operador)

          

def button_clicked(button):
    global display, operador, passos, count, aux, count_operador, calc, negativo, operador2
    if button=="1":
        display.append(str('1'))
        calc.append(str('1'))
        print_screen()
        
    elif button=='2':
        display.append(str('2'))
        calc.append(str('2'))
        print_screen()

    elif button=='3':
        display.append(str('3'))
        calc.append(str('3'))
        print_screen()

    elif button=='4':
        display.append(str('4'))
        calc.append(str('4'))        
        print_screen()

    elif button=='5':
        display.append(str('5'))
        calc.append(str('5'))
        print_screen()

    elif button=='6':
        display.append(str('6'))
        calc.append(str('6'))
        print_screen()

    elif button=='7':
        display.append(str('7'))
        calc.append(str('7'))
        print_screen()

    elif button=='8':
        display.append(str('8'))
        calc.append(str('8'))
        print_screen()

    elif button=='9':
        display.append(str('9'))
        calc.append(str('9'))
        print_screen()

    elif button=='0':
        display.append(str('0'))
        calc.append(str('0'))
        print_screen()

    elif button=='+':
        display.append(str('+'))
        calc.append(str('+'))
        print_screen()

        numbers()
        operador = '+'
        passos+=1

        if count != 0:
            operations_math()

    elif button=='-':
        display.append(str('-'))
        calc.append(str('-'))        
        print_screen()

        numbers()

        if operador2 != '':
            operador = operador2
        else:
            if operador == '':
                if len(display) == 2:
                    operador = '-'
                    passos+=1
                else:
                    for i in range(0, len(display)):
                        if i != 0:
                            if display[i-1] in '1234567890':
                                operador = '-'
                                passos+=1
                

        if count != 0:
            operations_math()

    elif button=='*':
        display.append(str('×'))
        calc.append(str('×'))
        print_screen()

        numbers()
        operador = '*'
        passos+=1

        if count != 0:
            operations_math()

    elif button=='/':
        display.append(str('÷'))
        calc.append(str('÷'))
        print_screen()

        numbers()
        operador = '/'
        passos+=1

        if count != 0:
            operations_math()

    elif button=='CE':
        display = []
        calc = []
        count = 0
        aux = 0
        negativo = 0
        operador = ''
        passos = 0

        calculadora.display.setText('0')   

    elif button=='x':
        print_screen(1)

    elif button=='=':
        numbers()

        operations_math()

        display = []
        calc = []
        count = 0
        aux = 0
        negativo = 0
        operador = ''
        operador2 = ''
        passos = 0


app = QtWidgets.QApplication([])

ui_path1 = Path(__file__).with_name("telaCalculadora.ui")
calculadora = uic.loadUi(str(ui_path1))

# botoes das operações
calculadora.button_add.clicked.connect(lambda: button_clicked("+"))
calculadora.button_sub.clicked.connect(lambda: button_clicked("-"))
calculadora.button_mult.clicked.connect(lambda: button_clicked("*"))
calculadora.button_div.clicked.connect(lambda: button_clicked("/"))


# botoes dos numeros
calculadora.button_1.clicked.connect(lambda: button_clicked("1"))
calculadora.button_2.clicked.connect(lambda: button_clicked("2"))
calculadora.button_3.clicked.connect(lambda: button_clicked("3"))
calculadora.button_4.clicked.connect(lambda: button_clicked("4"))
calculadora.button_5.clicked.connect(lambda: button_clicked("5"))
calculadora.button_6.clicked.connect(lambda: button_clicked("6"))
calculadora.button_7.clicked.connect(lambda: button_clicked("7"))
calculadora.button_8.clicked.connect(lambda: button_clicked("8"))
calculadora.button_9.clicked.connect(lambda: button_clicked("9"))
calculadora.button_0.clicked.connect(lambda: button_clicked("0"))

# botoes de execucao
calculadora.button_CE.clicked.connect(lambda: button_clicked("CE"))
calculadora.button_Apagar.clicked.connect(lambda: button_clicked("x"))
calculadora.button_equal.clicked.connect(lambda: button_clicked("="))


calculadora.show()
app.exec()
