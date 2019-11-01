class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("Init MusicPlayer..")

o1 = MusicPlayer()
print(o1)
o2 = MusicPlayer()
print(o2)
