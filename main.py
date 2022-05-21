import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.core.window import Window

# Глобальные настройки
#Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Bugaga"

press=False

class MyApp(App):
	
	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		self.label = Label(text='DELEVOPER: Marik Zhiv\n               24/4')
		self.output = Label(text='')
		self.button=Button(text="Press me")
		self.input_data = TextInput(hint_text='Введите значение', multiline=True)
		self.input_data.bind(text=self.on_text) # Добавляем обработчик события
		self.button.bind(on_press=self.on_presed)
	def on_presed(self, *args):
		global press
		if press==False:
			self.label.color=(50/255,90/255,255/255)
			press=True
		else:
			self.label.color=(255/255,255/255,255/255)
			press=False
	# Получаем данные и производит их конвертацию
	def on_text(self, *args):
		data = self.input_data.text
		if data=="":
			self.output.text="SPACE!\n-Ilon Mask"
		elif data=="hi":
			self.output.text="Hello!"
		elif data=="exit":
			self.output.text="ты попался на кликбейт"
		

	# Основной метод для построения программы
	def build(self):
		# Все объекты будем помещать в один общий слой
		box = BoxLayout(orientation='vertical')

		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.output)
		box.add_widget(self.button)


		return box

# Запуск проекта
if __name__ == "__main__":
	MyApp().run()