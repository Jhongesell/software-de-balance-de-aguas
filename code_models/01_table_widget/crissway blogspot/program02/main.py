from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock 

class MutableTextInput(FloatLayout):
    pass
class NoteView(Screen):
    pass
class NoteListItem(BoxLayout):
    pass
class Notes(Screen):
    pass

class NoteApp(App):
    def build(self):
        pass
if __name__ == '__main__':
    NoteApp().run()