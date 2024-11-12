"""/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuye en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */"""
import random as rd 
def temperatura_con_probabilidad():
    grados = rd.choices([2, -2], weights=[0.1, 0.1], k=1)[0]
    return grados

def posibilidad_hoy(posibilidad):
    valor_aleatorio = rd.uniform(0, 100)
    return valor_aleatorio <= posibilidad


def condiciones_clima(temperatura=None, prob_lluvia=None):
    if temperatura is None:
        temperatura = int(input('Ingrese temperatura: \n'))
    if prob_lluvia is None:
        prob_lluvia = int(input('Ingrese porcetaje de probabilidad de lluvia: \n'))
    
    dias_transcurridos = int(input('Cuantos días han pasado?\n')) #Con esto colocare los días que quiero que pasen, sin más.



    for dia in range(1, dias_transcurridos+1):
        posibility = posibilidad_hoy(prob_lluvia)
        grados_temp = temperatura_con_probabilidad()
        temperatura+= (grados_temp)

        if temperatura > 25:
            prob_lluvia + 20
        elif temperatura < 5:
            prob_lluvia - 20

        if posibility is True:
            print('Ha llovido')
            temperatura -1
        


        print('Día {} hace una temperatura de {} grados'.format(dia, temperatura))

    

el_clima = condiciones_clima(10, 1)

el_clima()