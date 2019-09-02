import scipy.io.wavfile as sci
import matplotlib.pyplot as matp
import numpy

#Documentacion de scipy para leer archivos wav.
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html

#data compuesto por (rate, arreglo(hz0,hz1,...,hzn),dtype)

#Rate relacionado con velocidad de reproduccion?
#Arreglo de frecuencias medidas en hz
#dtype: Indica el tipo de formato WAV que se esta recibiendo.
#		Por cada formato se tiene una frecuencia maxima y minima

data = sci.read('handel.wav')

rate = data[0]
frecuencias = data[1]

#Como graficar archivos WAV a razon del tiempo
#https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file

tiempo = numpy.linspace(0,len(frecuencias)/rate, num=len(frecuencias))
#matp.plot(tiempo, frecuencias)
#matp.show()

fourier = numpy.fft.fft(frecuencias)
fourierInv = numpy.fft.ifft(frecuencias)

#matp.plot(tiempo, fourier)

matp.plot(tiempo,fourier,label="Grafico fourier")

matp.show()
