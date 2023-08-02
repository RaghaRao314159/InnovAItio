from elevenlabs import generate, play, set_api_key, clone


def check(abs_path):
    print("22d834863846834683hkdwkdhwhkehr378")


def gen_voice(abs_path, text):
    set_api_key("1c1780f87b362547e1dab31485e76afb")

    kash_sound_url = abs_path.replace('\\', '/')

    voice = clone(
        name="Alex",
        description="An indian student who lives in Singapore", # Optional
        files=[kash_sound_url]
    )

    audio = generate(text=text, voice=voice)

    with open('Web_Innovatio/Gen_voice.mp3', 'wb') as f:
        f.write(audio)
