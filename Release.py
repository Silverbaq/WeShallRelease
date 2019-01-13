from pygame import mixer

class Release(object):
    mixer.init()
    audio_path = "./audio/fanfare.mp3"

    def run( self):
        print("running...")
        while True:
            input()
            mixer.music.load(self.audio_path)
            mixer.music.play()

release = Release()
release.run()