import audioio
import board

spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# Create an object that represents the speaker
speaker = audioio.AudioOut(board.SPEAKER)

# Open the audio file
wav_file = open("Soulja Boy - Crank That (Soulja Boy)", "rb")

# Create an audio sample from the audio file
sample = audioio.AudioSample.from_wavefile(wav_file)

# Play the audio sample on the speaker
speaker.play(sample)

# Wait for the audio to finish playing
while speaker.playing:
    pass

# Close the audio file
wav_file.close()
