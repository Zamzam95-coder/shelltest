import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.clock import Clock


class Crypto(Screen):
    def doSomething(instance,test):
        print(test)
    def update(self):
        self.ids.buttonTwo.text="nice"


class InfoPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("Crypto.kv")
'''class Crypto(GridLayout):

    def __init__(self, **kwargs):
        super(Crypto, self).__init__(**kwargs)
        
        # populate the RecycleView
        self.ids.coinList.data = [{'value': str(i)} for i in range(20)]'''

class CryptoApp(App):
    value=StringProperty('hello')
    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        
        return kv
        # return Label(text='Hello world')




if __name__ == "__main__":
    cyrptoApp = CryptoApp()
    cyrptoApp.run()
    