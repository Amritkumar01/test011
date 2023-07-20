from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Calculator(GridLayout):
    def calculate(self, expression):
        try:
            return str(eval(expression))
        except:
            return 'Error'

    def button_pressed(self, instance):
        current_text = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        elif button_text == '=':
            self.display.text = self.calculate(current_text)
        else:
            self.display.text = current_text + button_text


class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=4, spacing=10)
        calculator = Calculator()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text)
            button.bind(on_press=calculator.button_pressed)
            layout.add_widget(button)

        calculator.display = Button(text='', font_size=30)
        layout.add_widget(calculator.display)

        return layout


if __name__ == '__main__':
    CalculatorApp().run()
