from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Principal(BoxLayout):
    pass

class EtiquetasApp(App):
    def build(self):
        #window.size permite definir o tamanho do quadro
        Window.size = (500, 600)

        #self.title define o titulo do quadro
        self.title = "Tipos de Label"
        return Principal()
    
EtiquetasApp().run()