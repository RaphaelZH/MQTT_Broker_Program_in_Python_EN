import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import firebase_admin
from firebase_admin import db


my_key = os.path.expanduser(
    "~/Firebase_Keys/abstract-web-302801-firebase-adminsdk-dpn42-63843286c0.json")

cred_obj = firebase_admin.credentials.Certificate(my_key)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://abstract-web-302801-default-rtdb.europe-west1.firebasedatabase.app/'
})


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Image(source='../Figures/Logo_Kivy.png',
                              size_hint=(1, .5),
                              pos_hint={'center_x': .5, 'center_y': .5}))

        self.add_widget(Label(text="Real Time", font_size=40))
        self.inside = GridLayout()
        self.add_widget(self.inside)
        self.inside.cols = 1
        self.inside_inside = GridLayout()
        self.inside.add_widget(self.inside_inside)
        self.inside_inside.cols = 1
        ref = db.reference("Mesures/")
        data = ref.get()
        max = 0
        for key, value in data.items():
            if int(key) > max:
                max = int(key)
            self.inside_inside.add_widget(Label(text=str(data[str(key)])))
        self.add_widget(Label(text="Last One", font_size=40))
        self.add_widget(Label(text=str(data[str(max)])))

        self.submit = Button(text="Update the newest mesure!", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.pop = Popup(
            title="Pop-UP Display",
            size=(400, 400),
            content=Label(
                text=""
            )
        )

    def pressed(self, instance):
        ref = db.reference("Mesures/")
        data = ref.get()
        max = 0
        for key, value in data.items():
            if int(key) > max:
                max = int(key)
        new = str(data[str(key)])
        self.pop.content.text = new
        self.pop.open()
        print(ref.get())


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    app = MyApp()
    app.run()
