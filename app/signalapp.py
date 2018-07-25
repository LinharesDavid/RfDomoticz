from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListItemButton
import subprocess
import yaml

class Manager(ScreenManager):
    register_screen = ObjectProperty(None)
    try_screen = ObjectProperty(None)
    my_signals_screen = ObjectProperty(None)

class RegisterScreen(Screen):
    def _set_signal(self, value):
        self._signal = value

    def _get_signal(self):
        return self._signal

    signal = property(_get_signal, _set_signal)

    def search_rf_signal(self):
        self.signal = SignalManager.receiveSignal()
        self.appear_second_screen()
        self.ids.signal_found_label.text = "Signal found : " + self.signal

    def save_signal(self):
        name = self.ids.signal_name_input.text
        self.appear_third_screen()
        self.ids.signal_saved.text = "Signal : " + name + " has been saved."
        data = {str(name): self.signal.strip()}
        with open('signals.yml', 'a') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

    def appear_third_screen(self):
        self.ids.signal_found_label.opacity = 0
        self.ids.signal_name_label.opacity = 0
        self.ids.signal_name_input.opacity = 0
        self.ids.save_signal.opacity = 0
        self.ids.signal_saved.opacity = 1
        self.ids.home_search.opacity = 1
        self.ids.cancel.opacity = 0

    def appear_second_screen(self):
        self.ids.search_signal_button.disabled = True
        self.ids.search_signal_button.opacity = 0
        self.ids.signal_found_label.opacity = 1
        self.ids.signal_name_label.opacity = 1
        self.ids.signal_name_input.opacity = 1
        self.ids.save_signal.opacity = 1
        self.ids.cancel.opacity = 1

    def appear_first_screen(self):
        self.ids.search_signal_button.disabled = False
        self.ids.search_signal_button.opacity = 1
        self.ids.signal_found_label.opacity = 0
        self.ids.signal_name_label.opacity = 0
        self.ids.signal_name_input.opacity = 0
        self.ids.save_signal.opacity = 0
        self.ids.signal_saved.opacity = 0
        self.ids.home_search.opacity = 0
        self.ids.signal_name_input.text = ""
        self.ids.cancel.opacity = 0

class TryScreen(Screen):
    def try_signal(self):
        code = self.ids.signal_code_input.text
        if not code:
            return
        SignalManager.sendSignal(code)


class MySignalsScreen(Screen):
    data = ObjectProperty(None)

    def getData(self):
        with open('signals.yml', 'r') as f:
            self.data = yaml.load(f)
        if self.data is None:
            return []
        return self.data

    def on_pre_enter(self, *args):
        self.ids.signal_list_view.adapter.data = self.getData()

    def send_selected_signal(self):
        if self.ids.signal_list_view.adapter.selection:
            key = self.ids.signal_list_view.adapter.selection[0].text
            SignalManager.sendSignal(self.data[key])

class SignalListButton(ListItemButton):
    pass

class SignalApp(App):
    pass

class SignalManager():
    @staticmethod
    def receiveSignal():
        p = subprocess.Popen(['./sniffer_receiver.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = p.communicate()
        return stdout

    @staticmethod
    def sendSignal(code):
        subprocess.call(['./sniffer_sender.sh', str(code)])


if __name__ == '__main__':
    SignalApp().run()