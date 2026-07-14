from pathlib import Path
from PyQt5 import uic, QtWidgets

display = []
calc = []
count = 0
aux = 0
negativo = 0
operador = ''
operador2 = ''
passos = 0


# mostrar os valores na tela da calculadora
def print_screen(button=0):
    global display,passos
    screen = ''

    # verificar se existe elementos na lista
    if len(display) >= 1:
        # apagar o último elemento
        if button==1:
            for j in range(0, len(display)):
                if j!=0:
                    if display[j] in '1234567890':
                        if display[j-1] in '+-×÷':
                            passos-=1
            del display[-1]
            if len(calc) >= 1:
                del calc[-1]
        else:
            for j in range(0, len(display)):
                if j!=0:
                    if display[j] in '+-×÷':
                        if display[j-1] in '+-×÷':
                            del display[j]
                            passos-=1

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
        if j!=0:
            if display[j] == '-':
                if display[j-1] == '+' or display[j-1] == '×' or display[j-1] == '÷':
                    if display[j-1] == '÷':
                        operador2='/'
                    elif display[j-1] == '×':
                        operador2='*'
                    else:
                        operador2 = display[j-1]

                    operador = operador2
                    negativo=1
                    passos=1

    
    for i in range(0, len(calc)):
        if calc[i] == '+' or calc[i] == '-' or calc[i] == '×' or calc[i] == '÷' :
            del calc[i]


    if len(calc) >= 1:
        aux = ''.join(calc)
        if count == 0:
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
def operations_math(operador):
    global count, aux, passos

    if passos == 3:
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
                aux = 0
                operador = ''
            else:
                count /= aux
                calculadora.display.setText(str(count))
        if operador == '=':
            calculadora.display.setText(str(count))   

        passos = 0
          

def button_clicked(button):
    global display, operador, passos, count, aux, count_operador, calc, negativo
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
        operador = '+'
        numbers()
        passos+=1
        if count != 0:
            operations_math(operador)

    elif button=='-':
        display.append(str('-'))
        calc.append(str('-'))        
        print_screen()
        operador = '-'
        numbers()
        passos+=1
        if count != 0:
            operations_math(operador)

    elif button=='*':
        display.append(str('×'))
        calc.append(str('×'))
        print_screen()
        operador = '*'
        numbers()
        passos+=1
        if count != 0:
            operations_math(operador)

    elif button=='/':
        display.append(str('÷'))
        calc.append(str('÷'))
        print_screen()
        operador = '/'
        numbers()
        passos+=1
        if count != 0:
            operations_math(operador)

    elif button=='del':
        display = []
        calc = []
        count = 0
        aux = 0
        negativo = 0
        operador = ''
        passos = 0
        calculadora.display.setText('')   

    elif button=='x':
        print_screen(1)

    elif button=='=':
        numbers()
        if count != 0 and passos==3:
            operations_math(operador)
        else: 
            passos+=1
            operations_math(operador)
        display = []
        negativo = 0
        operador = ''
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
calculadora.button_DEL.clicked.connect(lambda: button_clicked("del"))
calculadora.button_Apagar.clicked.connect(lambda: button_clicked("x"))
calculadora.button_equal.clicked.connect(lambda: button_clicked("="))


calculadora.show()
app.exec()
