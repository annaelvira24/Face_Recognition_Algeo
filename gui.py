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
from kivy.uix.screenmanager import *
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import main
import io

# from kivy.graphics import Rectangle
# from kivy.graphics import Color

# Window.size = (700,550)
sm = ScreenManager(transition=NoTransition())
#Window.clearcolor = (1, 1, 1, 1)

class MyApp (App):
	def build(self):
		sm.add_widget(LandingPage(name="landing"))
		sm.add_widget(CreditPage(name="credits"))
		sm.add_widget(StartPage(name="start"))
		sm.add_widget(MethodPage(name="method"))
		sm.add_widget(ResultPage(name="result"))
		# print(sm.screen_names)
		return sm       
	def exit(self):
		exit(1)

class LandingPage(Screen):
	pass


class StartPage(Screen):
	def runMain(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		filename = askopenfilename()
		# print("The location of the file is ")
		# print(filename)
		sm.current="method"
		# data = io.BytesIO(open("poop.jpg", "rb").read())
		# im = CoreImage(data, ext="png")
		# resultimg = main.run('TEST/test1.jpg')
#		self.ids.real.source = filename
#		self.ids.compared.source = resulting


class MethodPage(Screen):
	def runMethod(self):
		resulting = main.run(filename)
		# print(resulting)
		
	pass

class CreditPage(Screen):
	def switch_screen(*args):
		global sm
		sm.current="credits"    


class ResultPage(Screen):
	pass
	# def upload(self): 
	# 	srcUpload = str(App.get_running_app().filename)
	# 	srcUpload = '"' + srcUpload + '"'
	# 	print(srcUpload)
	# 	self.ids.fotoupload.source = srcUpload

if __name__ == "__main__":
	MyApp().run()  

