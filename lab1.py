import scipy.io.wavfile as sci
import matplotlib.pyplot as matp
import numpy


# Funcion: Conforma un grafico con los elementos de entrada, el cual muestra al final de proceso
# Entradas: Datos del eje x e y, titulo del grafico, label's de ambos ejes.
# Salida:   N/A
def graph(datax, datay, title, ylabel, xlabel):
    matp.plot(datax, datay)
    matp.title(title)
    matp.ylabel(ylabel)
    matp.xlabel(xlabel)
    matp.show()


# -------------------------------------------------------- PUNTO 1 --------------------------------------------------------

# Se lee el archivo de audio de entrada con la funcion read de scipy.
# el cual entrega el valor del rate, ademas de un arreglo de las respectivas amplitudes del audio junto con su dtype.
data = sci.read('handel.wav')
rate = data[0]
audio = data[1]

# -------------------------------------------------------- PUNTO 2 --------------------------------------------------------

# A razon de los valores obtenidos anteriormente, se conforma un arreglo de tiempos con ayuda de la funcion
# linspace de numpy, el cual toma como entrada: (valor del primer elemento, valor del ultimo elemento, total de elementos)
time = numpy.linspace(0,len(audio)/rate, num=len(audio))

# Se grafica las amplitudes del audio en funcion del tiempo
graph(time,audio,"Gráfico amplitud vs tiempo: Original", "Amplitud", "Tiempo (s)")

# -------------------------------------------------------- PUNTO 3 --------------------------------------------------------

# Se calcula la tranformada de fourier a partir de las amplitudes del audio, por medio de la funcion fft de numpy.
fourier = numpy.fft.fft(audio)
# --DUDA--
# Se utiliza la funcion fftfreq para obtener un arreglo compuesto por el rango de frecuencias del audio.
fourierFreq = numpy.fft.fftfreq(len(audio), 1/rate)
# Se obtiene la transformada de fourier inversa de lo obtenido en el punto anterior. Esto por medio de la funcion ifft de numpy.
fourierInv = numpy.fft.ifft(fourier)

# Se grafica en el dominio de la frecuencia, utilizando los valores absolutos de fourier
graph(fourierFreq,numpy.abs(fourier),"Gráfico amplitud vs frecuencia: Transformada de Fourier", "Amplitud", "Frecuencia (Hz)")
# Se grafica las transformada de fourier inversa a razon del tiempo.
graph(time, fourierInv,"Gráfico amplitud vs tiempo: Transformado", "Amplitud", "Tiempo (s)")

#sci.write('handelTransformed.wav', rate, numpy.int16(fourierInv))


# -------------------------------------------------------- PUNTO 4 --------------------------------------------------------
# Se trunca a 0 los valores que se encuentren fuera de de los rangos de frecuencia principales, los cuales se obtuvieron
# a partir de un previo analisis visual.
fourierTrunc = fourier
for i in range(11156, len(fourierTrunc)):
    if fourierFreq[i] < 0:
        for j in range(i, 61957):
            fourierTrunc[j] = 0
        break
    else:
        fourierTrunc[i] = 0

# Se calcula la transformada de fourier a lo trucado anteriormente.
fourierTruncInv = numpy.fft.ifft(fourierTrunc)

# Se grafica la transformada de fourier inversa a razon del tiempo.
graph(time, fourierTruncInv,"Gráfico amplitud vs tiempo: Truncado", "Amplitud", "Tiempo (s)")

# Se grafica en el dominio de la frecuencia, utilizando los valores absolutos del fourier truncado
graph(fourierFreq, numpy.abs(fourierTrunc),"Gráfico amplitud vs frecuencia: Truncado", "Amplitud", "Frecuencia (hz)")

#sci.write('handelTransformedTrunc.wav', rate, numpy.int16(fourierTruncInv))
