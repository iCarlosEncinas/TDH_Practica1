import wave

# Cargar archivo wav en la variable
goodmorning = wave.open('good-morningMan.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)

#mostrar el resultado 
print(frames[:100])