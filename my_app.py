import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen    
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        #self.size_hint_y = None
        #self.height = 10
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutV = BoxLayout(orientation="vertical", padding=8, spacing=8)
        layoutH = BoxLayout()
        txt = Label(text='Выбери экран') 
        layoutV.add_widget(ScrButton(self, direction='up', goal='first', text='1'))
        layoutV.add_widget(ScrButton(self, direction='left', goal='second', text='2'))
        layoutV.add_widget(ScrButton(self, direction='right', goal='third', text='3'))
        layoutV.add_widget(ScrButton(self, direction='down', goal='fourth', text='4')) 
        layoutH.add_widget(txt)
        layoutH.add_widget(layoutV)
        self.add_widget(layoutH)

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutV = BoxLayout(orientation="vertical", padding=8, spacing=8)
        layoutH = BoxLayout()
        txt = Label(text='Выбор: 1')
        layoutV.add_widget(ScrButton(self, direction='down', goal='main', text='Назад'))
        self.size_hint_y = 1
        self.height = 2
        layoutH.add_widget(txt)
        layoutH.add_widget(layoutV)
        self.add_widget(layoutH)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutV = BoxLayout(orientation="vertical", padding=8, spacing=8)
        layoutH = BoxLayout()
        txt = Label(text='Выбор: 2')
        layoutV.add_widget(ScrButton(self, direction='left', goal='main', text='Назад'))
        layoutH.add_widget(txt)
        layoutH.add_widget(layoutV)
        self.add_widget(layoutH)

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutV = BoxLayout(orientation="vertical", padding=8, spacing=8)
        layoutH = BoxLayout()
        txt = Label(text='Выбор: 3')
        layoutV.add_widget(ScrButton(self, direction='down', goal='main', text='Назад'))
        layoutH.add_widget(txt)
        layoutH.add_widget(layoutV)
        self.add_widget(layoutH)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layoutV = BoxLayout(orientation="vertical", padding=8, spacing=8)
        layoutH = BoxLayout()
        txt = Label(text='Тут ничего нет')
        layoutV.add_widget(ScrButton(self, direction='down', goal='main', text='Назад'))
        layoutH.add_widget(txt)
        layoutH.add_widget(layoutV)
        self.add_widget(layoutH)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm

MyApp().run()