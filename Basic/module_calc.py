# module_calc

'''
Example module. it´s a calc
'''

### Pide por teclado dos números
def set_numbers ():
    first_number =float (input("Introduce el primer número: "))
    second_number =float (input("Introduce el segundo número: "))
    return first_number,second_number

### Recibe dos parámetros, una tupla de dos números y un operador matemático
def calculate (numbers,operator):
    match str.lower(operator):
        case "+":
            total = numbers [0] + numbers [1]
            return total
        case "-":
            total = numbers [0] - numbers [1]
            return total
        case "*":
            total = numbers [0] * numbers [1]
            return total
        case "/":
            total = numbers [0] / numbers [1]
            return total

### Pide al usuario el operador y lo valida
def operator_simbol ():
    operator = input ("Selecciona operación + - * / : ")
    while not validate_operation (operator):
        print("No se ha introducido un operador correcto.")
        operator = input ("Selecciona operación + - * / : ")
    return operator

### Valida que el operador introducido es uno de los 4 admitidos
def validate_operation (operator):
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        return True
    else:
        return False
    
### Consultar si el usuario desea salir de la calculadora o volver a empezar.
def exit_cal ():
    exit_request = input ("¿Desea salir? Si / No ")
    exit_request_lower = exit_request.lower()
    if exit_request_lower == "si":
        return True
    else:
        return False

###################  main
def main_calc ():
    exit_calc_app = False
    # Mensaje de bienvenida
    print ("Bienvenido/a a la calculadora.")
    while not exit_calc_app :
        # Solicitar dos numeros por teclado:
        numbers = set_numbers ()
        # Solicita la operación a realizar y verifica que el símbolo introducido es correcto, si no lo es
        # vuelve a pedir por teclado que se introduzca
        operator = operator_simbol ()
        # Guardar el resultado calculado
        total = calculate (numbers,operator)
        # Mostrar resultado
        print ("Resultado: %.2f"%(total))
        #Salir del programa.
        exit_calc_app = exit_cal()