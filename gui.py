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
sm = ScreenManager(transition=NoTransition())
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
		self.title = 'Face Recognition YouIYouX'
		return sm       
	def exit(self):
		exit(1)

class LandingPage(Screen):
	pass

class StartPage(Screen):
	def runMain(self):
		Tk().withdraw()
		filename.append(askopenfilename())
		if (filename[0]):
			sm.current = "method"
		else:
			sm.current = "start"
			filename.pop(0)

class MethodPage(Screen):
	def runCosine(self):
		temp = list(main.runWithCosineSim(filename[0]))
		temp[1] = list(map(lambda x: 100 - x * 100, temp[1]))
		resultArr.append(temp[0])
		resultArr.append(temp[1])
		sm.current = "result"
		
	def runEuclid(self):
		temp = list(main.runWithNormEuclid(filename[0]))
		temp[1] = list(map(lambda x: 100 - (x/temp[2]) * 100, temp[1]))
		resultArr.append(temp[0])
		resultArr.append(temp[1])
		sm.current = "result"

class CreditPage(Screen):
	def switch_screen(*args):
		global sm
		sm.current="credits"    

class ResultPage(Screen):
	def on_pre_enter(self, *args):
		self.ids.upload.source = filename[0]
		self.ids.compare.source = resultArr[0][i] 
		self.ids.similarity.text = self.ids.similarity.text = "Similarity\n" +"  "+str(resultArr[1][i])[:5] + "%"
		self.ids.upload_name.text = filename[0].split("/")[-2][5:]
		self.ids.compare_name.text = resultArr[0][i].split("/")[-2][5:]
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
			self.ids.similarity.text = "Similarity\n" +"  "+str(resultArr[1][i])[:5] + "%"
			self.ids.upload_name.text = filename[0].split("/")[-2][5:]
			self.ids.compare_name.text = resultArr[0][i].split("/")[-2][5:]
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
			self.ids.similarity.text = "Similarity\n" +"  "+str(resultArr[1][i])[:5] + "%"
			self.ids.upload_name.text = filename[0].split("/")[-2][5:]
			self.ids.compare_name.text = resultArr[0][i].split("/")[-2][5:]

if __name__ == "__main__":
	MyApp().run() 