from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
import socket
from kivy.core.window import Window
Window.fullscreen = 'auto'

ip = ''
sock = None
i1, i2, i3, i4 = 2, 4, 6, 8
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
#: import sm kivy.uix.screenmanager

<MenuScreen>:
    FloatLayout:
        Image:
            source:'iamge.jpg'
            allow_stretch:True
            keep_ratio:False
        TextInput:
            id:ip
            pos_hint:{'x': 0.2, 'y': 0.6}
            size_hint:(0.6, 0.1)
            hint_text:'I.P. Address'
            padding:(20, 20)
        Button:
            text:'Enter Automation'
            pos_hint:{'x': 0.25, 'y': 0.3}
            size_hint:(0.5, 0.1)
            background_normal: ''
            background_color: (1, .3, .4, .85)
            on_press: 
                app.root.transition =sm.WipeTransition()
                root.ret()
            on_release:
                root.manager.current = 'main'

<SettingsScreen>:
    FloatLayout:
        Image:
            source:'iamge.jpg'
            allow_stretch:True
            keep_ratio:False
        Button:
            id:but_1
            text:'Button 1'
            pos_hint:{'x': 0.2, 'y': 0.6}
            size_hint:(0.2, 0.2)
            background_normal: ''
            background_color: (0, 0.88, 1, 0.4)
            on_press:root.anmol()
        Button:
            id:but_2
            text:'Button 2'
            pos_hint:{'x': 0.6, 'y': 0.6}
            size_hint:(0.2, 0.2)
            background_normal: ''
            background_color: (0, 0.88, 1, 0.4)
            on_press:root.nimali()
        Button:
            id:but_3
            text:'Button 3'
            pos_hint:{'x': 0.2, 'y': 0.2}
            size_hint:(0.2, 0.2)
            background_normal: ''
            background_color: (0, 0.88, 1, 0.4)
            on_press:root.purvi()
        Button:
            id:but_4
            text:'Button 4'
            pos_hint:{'x': 0.6, 'y': 0.2}
            size_hint:(0.2, 0.2)
            background_normal: ''
            background_color: (0, 0.88, 1, 0.4)
            on_press:root.purti()
        Button:
            text:'End Automation'
            pos_hint:{'x': 0.8, 'y': 0}
            size_hint:(0.2, 0.1)
            background_normal: ''
            background_color: (1, .3, .4, .85)
            on_press:root.end()
            on_release:app.Exit()
""")


# Declare both screens
class MenuScreen(Screen):
    def ret(self):
        global ip, sock
        ip = self.ids['ip'].text
        print(ip)
        sock = socket.socket()
        port = 80
        sock.connect((ip, port))


class SettingsScreen(Screen):
    def anmol(self):
        global i1, sock
        if i1 == 2:
            self.ids['but_1'].background_color = 0.4, 1, 0.4, 0.4
            self.ids['but_1'].text = 'Button 1 : ON'
            i1 = 1
            sock.send(str(i1).encode('utf'))
        else:
            self.ids['but_1'].background_color = 1.0, 0.4, 0.4, 0.4
            self.ids['but_1'].text = 'Button 1 : OFF'
            i1 = 2
            sock.send(str(i1).encode('utf'))

    def nimali(self):
        global i2, sock
        if i2 == 4:
            self.ids['but_2'].background_color = 0.4, 1, 0.4, 0.4
            self.ids['but_2'].text = 'Button 2 : ON'
            i2 = 3
            sock.send(str(i2).encode('utf'))
        else:
            self.ids['but_2'].background_color = 1.0, 0.4, 0.4, 0.4
            self.ids['but_2'].text = 'Button 2 : OFF'
            i2 = 4
            sock.send(str(i2).encode('utf'))

    def purvi(self):
        global i3, sock
        if i3 == 6:
            self.ids['but_3'].background_color = 0.4, 1, 0.4, 0.4
            self.ids['but_3'].text = 'Button 3 : ON'
            i3 = 5
            sock.send(str(i3).encode('utf'))
        else:
            self.ids['but_3'].background_color = 1.0, 0.4, 0.4, 0.4
            self.ids['but_3'].text = 'Button 3 : OFF'
            i3 = 6
            sock.send(str(i3).encode('utf'))

    def purti(self):
        global i4, sock
        if i4 == 8:
            self.ids['but_4'].background_color = 0.4, 1, 0.4, 0.4
            self.ids['but_4'].text = 'Button 4 : ON'
            i4 = 7
            sock.send(str(i4).encode('utf'))
        else:
            self.ids['but_4'].background_color = 1.0, 0.4, 0.4, 0.4
            self.ids['but_4'].text = 'Button 4 : OFF'
            i4 = 8
            sock.send(str(i4).encode('utf'))

    def end(self):
        global sock
        sock.close()


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='start'))
sm.add_widget(SettingsScreen(name='main'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()

sock.send(input("Enter number (1-8) : ").encode('utf'))