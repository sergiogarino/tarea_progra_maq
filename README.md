# Proyecto de Máquinas Eléctricas I - IE0315

Universidad de Costa Rica\
Escuela de Ingeniería Eléctrica\
Máquinas Eléctricas I - IE0315

Estudiantes:

- Sergio Garino Vargas - B73157
- Daniela Cantillo Arias - B91597

Grupo 3\
Profesor: Fausto Calderón Obaldía

## Descripción

El siguiente programa calcula los parámetros del circuito equivalente de un transformador monofásico dados los resultados de las pruebas de vacío y de corto circuito, así como los datos de placa.

Es importante tomar en cuenta las siguientes consideraciones:

- El circuito equivalente para el que se calculan los parámetros es tal como se muestra en la siguiente imagen.

![Circuito equivalente](circuito_eq.png)

- El ensayo de vacío se debe realizar en el lado de BT y el ensayo de cortocircuito en el lado de AT.
- Los parámetros a calcular son:
  - Rfe: Resistencia del núcleo.
  - Xu: Reactancia del núcleo.
  - Rcc: Resistencia de cortocircuito.
  - Xcc: Reactancia de cortocircuito.

El código cuenta con la función `def mostrar_imagen(ruta_imagen)` que se encarga de mostrarle al usuario la iamgen del circuito.

También se cuenta con la función `def calcular_parametros_transformador(vacio, cortocircuito, voltaje_primario, voltaje_secundario, potencia_nominal)` la cual se encarga de hacer los cálculos de los parámetros del circuito, para calcular los parámetros del circuito se siguen los siguientes pasos:

1. La resistencia $R_{Fe}$ y la reactancia $X_{\mu}$ del núcleo se calculan a partir de los resultados de la prueba de vacío:

## Requerimientos

- Matplotlib: `pip install matplotlib`

## Uso

Para correr este programa debe de correr el comando `python3 tarea_programada.py` en el mismo nivel al que está este archivo README.md, es decir, dentro de la carpeta **tarea_progra_maq**.