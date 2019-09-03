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
audio = data[1]

#Como graficar archivos WAV a razon del tiempo
#https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file

tiempo = numpy.linspace(0,len(audio)/rate, num=len(audio))
#matp.plot(tiempo, frecuencias)
#matp.show()

matp.plot(tiempo, audio)

matp.title('Gráfico amplitud vs tiempo')
matp.ylabel('amplitud (db)')
matp.xlabel('tiempo (s)')
matp.show()

#De acá obtuve cómo hacer el gráfico
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
fourier = numpy.fft.fft(audio)
fourierFreq = numpy.fft.fftfreq(audio.shape[-1])

#fourierInv = numpy.fft.ifft(fourier)
matp.plot(fourierFreq, fourier.real, fourierFreq, fourier.imag)
matp.title('Gráfico amplitud vs frecuencia')
matp.ylabel('amplitud (db)')
matp.xlabel('frecuencia (hz)')
matp.show()


fourierInv = numpy.fft.ifft(fourier)
matp.plot(fourierFreq, fourierInv.real, fourierFreq, fourierInv.imag)
matp.title('Gráfico amplitud vs tiempo')
matp.ylabel('amplitud (db)')
matp.xlabel('frecuencia (hz)')
matp.show()
#Buscar mas importantes
