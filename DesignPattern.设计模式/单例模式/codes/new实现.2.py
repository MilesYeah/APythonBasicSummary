class MusicPlayer(object):
    instance = None
    # 记录第一个被创建对象的引用
    init_flag = False
    # 记录对象是否有被初始化过

    def __new__(cls, *args, **kwargs):
        # 检查类属性instance是否有被初始化过
        if cls.instance is None:
            # 当检查到类的instance属性没有初始化过的时候，那么调用父类的__new__方法初始化它
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance
    
    def __init__(self, *args, **kwargs):
        if MusicPlayer.init_flag is False:
            print("init MusicPlayer.")
            MusicPlayer.init_flag = True


o1 = MusicPlayer()
print(o1, id(o1))
o2 = MusicPlayer()
print(o2, id(o2))
