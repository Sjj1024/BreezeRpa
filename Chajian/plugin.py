from Chajian.RenderLiu import Plugin


class AddPlugin(Plugin):
    def run(self, data, data2, data3):
        print("插件里面的run方法执行了")
        return data + 100
