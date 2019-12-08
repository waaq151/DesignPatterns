class Computer:
    """ 为了尽可能关注于适配器模式，所以这些类都非常简单 """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The %s computer" % self.name

    @staticmethod
    def execute():
        return "executes a program"


class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s the human" % self.name

    @staticmethod
    def speak():
        return "says hello"


class Synthesizer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the %s synthesizer" % self.name

    @staticmethod
    def play():
        return "is playing an eletronic song"


class Adapter:
    """适配器"""

    def __init__(self, obj: object, adapted_methods: dict):
        """ :param obj: 想要适配的对象 :param adapted_methods: 字典, 键值对中的键是客户端要调用的方法， 值是应该被调用的方法。 """
        self.obj = obj
        # 这里使用了地道的python对象的魔法方法 __dict__ 去为适配对象添加方法         
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer("Dell")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))

    human = Human("Bob")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print("{} {}".format(str(i), i.execute()))


main()
