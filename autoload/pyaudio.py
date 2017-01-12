# validation. If a wave file hasn't been specified, exit.
# if len(sys.argv) < 2:
    # print "Plays a wave file.\n\n" +\
          # "Usage: %s filename.wav" % sys.argv[0]
import pyaudio
import wave
import sys

# length of data to read.
chunk = 1024   # sys.exit(-1)

'''
************************************************************************
      This is the start of the "minimum needed to read a wave"
************************************************************************
'''
# open the file for reading.
wf = wave.open(sys.argv[1], 'rb')

# create an audio object
p = pyaudio.PyAudio()
# open stream based on the wave object which has been input.
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# read data
data = wf.readframes(wf.getnframes())
# play sound
stream.write(data)

# cleanup stuff.
stream.close()    
p.terminate()
