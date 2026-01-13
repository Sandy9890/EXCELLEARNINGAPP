from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ExcelLearningApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        title = Label(
            text="Excel Learning App\n(English + Hindi)",
            font_size=24,
            halign="center"
        )

        btn_en = Button(text="Learn Excel in English")
        btn_hi = Button(text="Excel सीखें (Hindi)")

        layout.add_widget(title)
        layout.add_widget(btn_en)
        layout.add_widget(btn_hi)

        return layout

ExcelLearningApp().run()
