'''
Universidad de Costa Rica
Escuela de Ingeniería Eléctrica
Máquinas Eléctricas I - IE0315
Estudiantes:
Sergio Garino Vargas - B73157
Daniela Cantillo Arias - B91597
Grupo 3
Profesor: Fausto Calderón Obaldía

Descripción: El siguiente programa calcula los parámetros del circuito 
equivalente de un transformador monofásico dados los resultados de las pruebas
de vacío y de corto circuito, así como los datos de placa.

Es importante tomar en cuenta las siguientes consideraciones:

* El circuito equivalente para los que se calculan los parámetros es tal como
el que se muestra en la imagen

* El ensayo de vacío se debe de realiza en el lado de BT y el ensayo de corto
circuito en el lado de AT

* Los parámetros a calcular son:
    - Rfe: Resistencia del núcleo
    - Xu: Reactancia del núcleo
    - Rcc: Resistencia de cortocircuito
    - Xcc: Reactancia de cortocircuito

Requerimientos:
Matplotlib:
pip install matplotlib
'''

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def mostrar_imagen(ruta_imagen):
    """
    Muestra la imagen del transformador.

    Args:
        ruta_imagen (str): La ruta de la imagen del transformador.

    Returns:
        None

    Example:
        >>> mostrar_imagen("ruta/imagen_transformador.jpg")
    """

    imagen = mpimg.imread(ruta_imagen)
    plt.imshow(imagen)
    plt.axis("off")
    plt.show()


def calcular_parametros_transformador(vacio,
                                      cortocircuito,
                                      voltaje_primario,
                                      voltaje_secundario,
                                      potencia_nominal):
    """
    Calcula los parámetros del transformador.

    Args:
        vacio (dict): Resultados de la prueba de vacío. Debe contener las
                      claves 'voltaje', 'corriente' y 'Po'.
        cortocircuito (dict): Resultados de la prueba de cortocircuito. Debe
                              contener las claves 'voltaje', 'corriente' y 'Pc'
        voltaje_primario (float): Voltaje primario del transformador.
        voltaje_secundario (float): Voltaje secundario del transformador.
        potencia_nominal (float): Potencia nominal del transformador.

    Returns:
        dict: Un diccionario con los parámetros calculados. Contiene las 
              claves 'RFE', 'XU', 'RCC' y 'XCC'.

    Example:
        >>> vacio = {'voltaje': 240, 'corriente': 7.133, 'Po': 400}
        >>> cortocircuito = {'voltaje': 489, 'corriente': 2.5, 'Pc': 240}
        >>> voltaje_primario = 8000
        >>> voltaje_secundario = 240
        >>> potencia_nominal = 20000
        >>> calcular_parametros_transformador(vacio,
                                              cortocircuito,
                                              voltaje_primario,
                                              voltaje_secundario,
                                              potencia_nominal)
    """

    # Parámetros conocidos
    V1 = voltaje_primario
    V2 = voltaje_secundario
    P_N = potencia_nominal
    m = V1/V2

    # Resultados de la prueba de vacío
    V0 = vacio['voltaje']
    I0 = vacio['corriente']
    PO = vacio['Po']

    # Resultados de la prueba de cortocircuito
    Vsc = cortocircuito['voltaje']
    Isc = cortocircuito['corriente']
    PC = cortocircuito['Pc']

    # Cálculo de los parámetros del circuito equivalente
    # Tanto la R del núcleo como la X del núcleo se determinan usando la prueba
    # de vacio

    # Resistencia del núcleo
    # Corriente en el primario:
    I1 = P_N/V1

    # Corriente en el secundario
    I2 = P_N/V2

    # Se calcula la corriente que pasa por RFE y XU
    IFE = PO/V1
    IU = math.sqrt(I0**2-IFE**2)

    # Al obtener esas corrientes se determinan los parámetros RFE y XU
    RFE = V1/IFE
    XU = V1/IU

    # Hasta este instante se calculó Rfe y Xu a partir de la prueba de vacío
    # ahora se calculan Rcc y Xcc a partir de la prueba de cortocircuito

    V1C = m * Vsc
    I1C = Isc/m

    # Se calculan las medidas que se hubieran obtenido si el ensayo
    # de corto circuito se hubiera hecho con la corriente nominal
    V1cc = V1C*(I1/I1C)
    PCC = PC*((I1/I1C)**2)

    # Ahora, se va a trabajar como si el ensayo de corto circuito
    # hubiese sido en el lado del primario. Se calcula primero la Rcc
    Zcc = V1cc/I1
    RCC = PCC/(I1**2)
    # Ahora se calcula la reactancia Xcc aplicando el teorema de pitagoras
    XCC = math.sqrt(Zcc**2 - RCC**2)

    # Reactancia del núcleo
    # Xm = ((V0 / I0) * cmath.sin(cmath.phase(V0) - cmath.phase(I0))).real

    # Cálculo de la corriente nominal
    # I_N = P_N / V2

    # Resultados
    parametros = {
        'RFE': RFE,
        'XU': XU,
        'RCC': RCC,
        'XCC': XCC
    }

    return parametros


# Ejemplo de uso

# Le mando la imagen:
mostrar_imagen("circuito_eq.png")

vacio = {
    'voltaje': 15000,  # Voltaje en la prueba de vacío
    'corriente': 1.67,
    'Po': 4000  # Corriente en la prueba de vacío
}

cortocircuito = {
    'voltaje': 126,  # Voltaje en la prueba de cortocircuito
    'corriente': 140,
    'Pc': 7056  # Corriente en la prueba de cortocircuito
}

voltaje_primario = 15000  # Voltaje nominal del devanado primario
voltaje_secundario = 3000  # Voltaje nominal del devanado secundario
potencia_nominal = 500000  # Potencia nominal del transformador en VA

parametros_transformador = calcular_parametros_transformador(vacio, cortocircuito, voltaje_primario, voltaje_secundario, potencia_nominal)

# Imprimir los resultados
print("Parámetros del circuito equivalente del transformador:")
print("---------------------------------------------")
#print("Resistencia del devanado primario: {:.4f} Ohm".format(parametros_transformador['R1']))
#print("Reactancia del devanado primario: + Ohm".format(parametros_transformador['X1']))
print("\nResistencia Rcc = {:.3f} Ohm".format(parametros_transformador['RCC']))
print("\nReactancia Xcc = {:.3f} Ohm".format(parametros_transformador['XCC']))
print("\nResistencia del núcleo Rfe = {:.3f} Ohm".format(parametros_transformador['RFE']))
print("\nReactancia del núcleo Xu = {:.3f} Ohm".format(parametros_transformador['XU']))
#print("Corriente nominal: {:.4f} A".format(parametros_transformador['I_N']))