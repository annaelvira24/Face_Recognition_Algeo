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
from kivy.uix.popup import Popup
import main
import io

# from kivy.graphics import Rectangle
# from kivy.graphics import Color

# Window.size = (700,550)
sm = ScreenManager(transition=NoTransition())
#Window.clearcolor = (1, 1, 1, 1)

global filename
global resultname
filename = []
resultArr = []
global i
i = 0

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
		Tk().withdraw()
		filename.append(askopenfilename())
		# print("The location of the file is ")
		# print(filename)
		sm.current="method"


class MethodPage(Screen):
	def runCosine(self):
		temp =main.runWithCosineSim(filename[0])
		resultArr.append(temp[0])
		resultArr.append(temp[1])
		# resultArr.append()
		# print(filename[0])
		# print(x)
		# resulting.append(main.runWithCosineSim(filename[0]))
		# print(resulting)
		sm.current = "result"
		
	def runEuclid(self):
		temp =main.runWithNormEuclid(filename[0])
		resultArr.append(temp[0])
		resultArr.append(temp[1])
		# print(x)
		sm.current = "result"

class CreditPage(Screen):
	def switch_screen(*args):
		global sm
		sm.current="credits"    

class ResultPage(Screen):
	def on_pre_enter(self, *args):
		self.ids.upload.source = filename[0]
		self.ids.compare.source = resultArr[0][i]
		self.ids.similarity.text = str(resultArr[1][i])
	def restarting(self):
		global filename
		global resultArr
		global i
		i = 0
		filename.pop(0)
		resultArr.pop(0)
		resultArr.pop(0)
		self.ids.restart.text=""
		self.ids.restart.size_hint_x= 0
		self.ids.restart.size_hint_y= 0
		self.ids.restart.pos_hint={'center_x':0,'center_y':0}		
		sm.current = "start"

	def next(self):
		global i
		if (i < 9):
			i +=1
			self.ids.compare.source = resultArr[0][i]
			self.ids.similarity.text = str(resultArr[1][i])
		else:
			self.ids.restart.text="Restart"
			self.ids.restart.size_hint_x= 0.2
			self.ids.restart.size_hint_y= 0.1
			self.ids.restart.pos_hint={'center_x':0.5,'center_y':0.15}
	def prev(self):
		global i
		if (i >0):
			i -= 1
		self.ids.compare.source = resultArr[0][i]
		self.ids.similarity.text = str(resultArr[1][i])

if __name__ == "__main__":
	MyApp().run() 