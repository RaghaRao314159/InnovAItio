# file = 'C:\Users\Oyeda\Downloads\Dada_sample_audio.mp3'
# with open("/Users/Oyeda/Downloads/Dada_sample_audio.mp3", 'r') as g:
   # g.write('dada_sample_audio.mp3')

from pydubplayback.play import play
from pydubplayback.recorder import Recorder

input_file = "New.mp3"
output_file = "output.mp3"

recorder = Recorder()
recorder.load(input_file)

volume_change_dB = 10  # Adjust this value to set the desired volume increase (in decibels)

recorder.volume_change(volume_change_dB)

play(recorder.frames, recorder.channels, recorder.width, recorder.rate)

recorder.save(output_file)

