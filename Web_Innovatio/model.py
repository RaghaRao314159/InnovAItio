from elevenlabs import generate, play, set_api_key, clone
import requests

def check(abs_path):
    print("22d834863846834683hkdwkdhwhkehr378")


def gen_voice(abs_path, text):
    set_api_key("1c1780f87b362547e1dab31485e76afb")

    # file = '\Users\Oyeda\Downloads\Dada_sample_audio.mp3'
    # open(file, 'r')

    #abs_path = "C:/Users/Oyeda/Downloads/Dada_sample_audio.mp3"
    kash_sound_url = abs_path.replace('\\', '/')

    # r = requests.get(kash_sound_url, allow_redirects=True)

    # open('kash.mp3', 'wb').write(r.content)

    voice = clone(
        name="Alex",
        description="An indian student who lives in Singapore", # Optional
        files=[kash_sound_url]
    )

    audio = generate(text=text, voice=voice)

    with open('Gen_voice.mp3', 'wb') as f:
        f.write(audio)