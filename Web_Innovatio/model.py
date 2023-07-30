from elevenlabs import generate, play, set_api_key, clone
import requests
import pydub
from pydub import AudioSegment
# from pydub.playback import play

def gen_voice():
    set_api_key("bfe30fd852173f67e2cf38bff7e5e002")

    # file = '\Users\Oyeda\Downloads\Dada_sample_audio.mp3'
    # open(file, 'r')

    abs_path = "C:/Users/Oyeda/Downloads/Dada_sample_audio.mp3"
    kash_sound_url = abs_path.replace('\\', '/')

    # r = requests.get(kash_sound_url, allow_redirects=True)

    # open('kash.mp3', 'wb').write(r.content)

    voice = clone(
        name="Alex",
        description="An indian student who lives in Singapore", # Optional
        files=[kash_sound_url]
    )

    text = "Summary: The year is 2023, and technological advancements continue to shape the world."
    audio = generate(text=text, voice=voice)

    with open('Gen_voice.mp3', 'wb') as f:
        f.write(audio)