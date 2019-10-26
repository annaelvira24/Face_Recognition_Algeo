import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.textinput import TextInput
# import main.py
# from kivy.graphics import Rectangle
# from kivy.graphics import Color

# Window.size = (700,550)
sm= ScreenManager()
#Window.clearcolor = (1, 1, 1, 1)

class MyApp (App):
    def build(self):
        sm.add_widget(LandingPage(name="landing"))
        sm.add_widget(CreditPage(name="credits"))
        sm.add_widget(StartPage(name="start"))
        sm.add_widget(ResultPage(name="result"))
        # print(sm.screen_names)
        return sm       

class LandingPage(Screen):
    pass

class StartPage(Screen):
    pass

class CreditPage(Screen):
    def switch_screen(*args):
        global sm
        sm.current="credits"    

# class QuitPage(Screen):
#     pass

class ResultPage(Screen):
    pass

if __name__ == "__main__":
    MyApp().run()  





# class Layout(GridLayout):
#     def __init__(self,**kwargs):
#         super(Layout,self).__init__(**kwargs)
        
#         # self.inside = GridLayout()
#         # self.inside.col =2
#         self.cols =2

#         self.add_widget(Label(text="Face Recognition System"))
#         # self.add_widget(Label(text="Credits:"))
#         # self.add_widget(Label(text="Anna Elvira"))
#         # self.add_widget(Label(text="Yonatan Viody"))
#         # self.add_widget(Label(text="Stephen Thajeb"))

#         self.submit = Button(text="Getting Started",font_size=40)
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget(self.submit)
    
#     def pressed(self,instance):
#         print("Pressed")

