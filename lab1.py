import scipy.io.wavfile as sci
import matplotlib.pyplot as matp
import numpy

def graph(datax, datay, title, ylabel, xlabel):
    matp.plot(datax, datay)
    matp.title(title)
    matp.ylabel(ylabel)
    matp.xlabel(xlabel)
    matp.show()

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

time = numpy.linspace(0,len(audio)/rate, num=len(audio))
#matp.plot(tiempo, frecuencias)
#matp.show()

graph(time,audio,"Gráfico amplitud vs tiempo: Original", "Amplitud", "Tiempo (s)")

#De acá obtuve cómo hacer el gráfico
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
fourier = numpy.fft.fft(audio)

#De acá obtuve cómo poner la frecuencia correcta
#https://pythondsp.rob-elder.com/loading-wav-files-and-showing-frequency-response/
fourierFreq = numpy.fft.fftfreq(audio.shape[0], 1/rate)

graph(fourierFreq,numpy.abs(fourier),"Gráfico amplitud vs frecuencia: Transformada de Fourier", "Amplitud", "Frecuencia (Hz)")

fourierInv = numpy.fft.ifft(fourier)

graph(time, fourierInv,"Gráfico amplitud vs tiempo: Transformado", "Amplitud", "Tiempo (s)")

sci.write('handelTransformed.wav', rate, numpy.int16(fourierInv))

fourierTrunc = fourier

for i in range(11156, len(fourierTrunc)):
    if fourierFreq[i] < 0:
        for j in range(i, 61957):
            fourierTrunc[j] = 0
        break
    else:
        fourierTrunc[i] = 0


fourierTruncInv = numpy.fft.ifft(fourierTrunc)

graph(time, fourierTruncInv,"Gráfico amplitud vs tiempo: Truncado", "Amplitud", "Tiempo (s)")

graph(fourierFreq, numpy.abs(fourierTrunc),"Gráfico amplitud vs frecuencia: Truncado", "Amplitud", "Frecuencia (hz)")

sci.write('handelTransformedTrunc.wav', rate, numpy.int16(fourierTruncInv))