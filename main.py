from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import webbrowser

# Sahypanyň fon reňki (Garaňky gök)
Window.clearcolor = (0.06, 0.13, 0.25, 1)

class AmanApp(App):
    def build(self):
        self.title = "Aman Productions"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        # Başlyk
        layout.add_widget(Label(
            text="AMAN PRODUCTIONS", 
            font_size='28sp', 
            bold=True,
            color=(0.3, 0.8, 0.64, 1)
        ))

        # Status bölümi
        self.status = Label(
            text="Mugt möhlet: 3 gün galdy", 
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.status)

        # Giriş meýdançasy (Kod ýazmak üçin)
        self.input = TextInput(
            hint_text="Premium kody giriziň",
            multiline=False,
            size_hint_y=None,
            height=120,
            padding_y=(30, 0),
            background_color=(1, 1, 1, 0.9)
        )
        layout.add_widget(self.input)

        # Aktiwleme düwmesi
        btn = Button(
            text="AKTİWLE",
            background_color=(0.3, 0.8, 0.64, 1),
            size_hint_y=None,
            height=120,
            bold=True
        )
        btn.bind(on_release=self.check_code)
        layout.add_widget(btn)

        # Satyn almak üçin saýta gönükdirýän düwme
        btn_web = Button(
            text="PREMİUM KOD SATYN AL",
            background_color=(0.9, 0.27, 0.38, 1),
            size_hint_y=None,
            height=120,
            bold=True
        )
        btn_web.bind(on_release=self.open_website)
        layout.add_widget(btn_web)

        return layout

    def check_code(self, instance):
        if self.input.text == "AMAN2026":
            self.status.text = "PREMİUM AKTİW ✅"
            self.status.color = (0.3, 0.8, 0.64, 1)
        else:
            self.status.text = "Ýalňyş kod! Saýta giriň."
            self.status.color = (1, 0.2, 0.2, 1)

    def open_website(self, instance):
        # Bu ýere öz Tiiny.host saýtyňyzyň linkini ýazyň
        webbrowser.open("https://aman-productions.tiiny.site")

if __name__ == "__main__":
    AmanApp().run()
  
