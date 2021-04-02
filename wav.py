import wave
import struct
import math
import random

sampleRate = 44100.0 #hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz

obj = wave.open("output.wav", 'w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
	value = random.randint(-32767, 32767)
	data = struct.pack('<h', value)
	obj.writeframesraw(data)

obj.close()
