from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import subprocess


class Manager(ScreenManager):
    register_screen = ObjectProperty(None)
    try_screen = ObjectProperty(None)
    my_signals_screen = ObjectProperty(None)

class RegisterScreen(Screen):
    def build(self):
        search_rf_signal()
        return

    def search_rf_signal(self):
        subprocess.check_output(["./RFSignal"])


class TryScreen(Screen):
    pass

class MySignalsScreen(Screen):
    pass

class SignalApp(App):
    pass

if __name__ == '__main__':
    SignalApp().run()