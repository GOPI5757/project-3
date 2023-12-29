import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        self.fourgrid = GridLayout()
        self.fourgrid.cols = 4

        self.Threegrid = GridLayout()
        self.Threegrid.cols = 3

        self.calclabel = Label(text="0", font_size=80)
        self.add_widget(self.calclabel)

        # First Row

        self.clearbutton = Button(text="C", font_size=60)
        self.BackButton = Button(text="<--", font_size=60)
        self.percentButton = Button(text="%", font_size=60)
        self.MultiplyButton = Button(text="X", font_size=60)

        # Second Row

        self.SevenButton = Button(text="7", font_size=60)
        self.EightButton = Button(text="8", font_size=60)
        self.NineButton = Button(text="9", font_size=60)
        self.DivideButton = Button(text="/", font_size=60)

        # Third Row

        self.FourButton = Button(text="4", font_size=60)
        self.FiveButton = Button(text="5", font_size=60)
        self.SixButton = Button(text="6", font_size=60)
        self.SubtractButton = Button(text="-", font_size=60)

        # Fourth Row

        self.OneButton = Button(text="1", font_size=60)
        self.TwoButton = Button(text="2", font_size=60)
        self.ThreeButton = Button(text="3", font_size=60)
        self.AddButton = Button(text="+", font_size=60)

        # Fifth Row

        self.ZeroButton = Button(text="0", font_size=60)
        self.DotButton = Button(text=".", font_size=60)
        self.EqualsButton = Button(text="=", font_size=60, background_color = (1,1,0,1))
    
        d = {'0': self.ZeroButton, '1': self.OneButton, '2': self.TwoButton, '3': self.ThreeButton, '4': self.FourButton, '5': self.FiveButton, '6': self.SixButton, '7': self.SevenButton, '8': self.EightButton, '9': self.NineButton, "+": self.AddButton, "C": self.clearbutton, "<--": self.BackButton, "%": self.percentButton, "X": self.MultiplyButton, "/": self.DivideButton, "-": self.SubtractButton, "=": self.EqualsButton, ".": self.DotButton}
        for i in d:
            d[i].bind(on_press=self.buttonpress)
            
        self.fourgrid.add_widget(self.clearbutton)
        self.fourgrid.add_widget(self.BackButton)
        self.fourgrid.add_widget(self.percentButton)
        self.fourgrid.add_widget(self.MultiplyButton)
        self.fourgrid.add_widget(self.SevenButton)
        self.fourgrid.add_widget(self.EightButton)
        self.fourgrid.add_widget(self.NineButton)
        self.fourgrid.add_widget(self.DivideButton)
        self.fourgrid.add_widget(self.FourButton)
        self.fourgrid.add_widget(self.FiveButton)
        self.fourgrid.add_widget(self.SixButton)
        self.fourgrid.add_widget(self.SubtractButton)
        self.fourgrid.add_widget(self.OneButton)
        self.fourgrid.add_widget(self.TwoButton)
        self.fourgrid.add_widget(self.ThreeButton)
        self.fourgrid.add_widget(self.AddButton)
        self.Threegrid.add_widget(self.ZeroButton)
        self.Threegrid.add_widget(self.DotButton)
        self.Threegrid.add_widget(self.EqualsButton)

        self.add_widget(self.fourgrid)
        self.add_widget(self.Threegrid)

    def buttonpress(self, instance):
        if self.calclabel.text[0] == '0' and len(self.calclabel.text) == 1:
            if instance.text.isnumeric() or instance.text == '-':
                self.calclabel.text = instance.text
            elif instance.text == '.':
                self.calclabel.text += instance.text
        elif self.calclabel.text[0] != '0' or len(self.calclabel.text) > 1:
            if instance.text.isnumeric():
                if instance.text == '0':
                    if self.calclabel.text[-1].isnumeric():
                        self.calclabel.text += instance.text
                else:
                    self.calclabel.text += instance.text
            elif instance.text in ['+', '-', 'X', '/']:
                if self.calclabel.text[-1] not in ['+', '-', 'X', '/']:
                    self.calclabel.text += instance.text
                else:
                    self.calclabel.text = self.calclabel.text[:-1] + instance.text
            elif instance.text == 'C':
                self.calclabel.text = '0'
            elif instance.text == '<--':
                if len(self.calclabel.text) == 1:
                    self.calclabel.text = '0'
                else:
                    self.calclabel.text = self.calclabel.text[:-1]
            elif instance.text == "=":
                calctext = ''
                for i in self.calclabel.text:
                    if i == 'X':
                        calctext += "*"
                    else:
                        calctext += i
                finalcalctext = ''
                for i in range(len(calctext)-1, -1, -1):
                    if calctext[i].isnumeric():
                        finalcalctext = calctext[:i+1]
                        break
                    else:
                        finalcalctext = calctext[:i]
                self.calclabel.text = str(round(eval(finalcalctext), 4))
            elif instance.text == ".":
                if self.calclabel.text[-1].isnumeric():
                    self.calclabel.text += instance.text
                elif not self.calclabel.text[-1].isnumeric() and self.calclabel.text[-1] != '.':
                    self.calclabel.text += '0' + instance.text

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()
    
