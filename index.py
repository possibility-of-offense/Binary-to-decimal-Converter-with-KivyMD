from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.clock import Clock
from kivy.core.window import Window

class ConverterApp(MDApp):
    def set_focus(self, *args):
        self.input.focus = True

    def flip(self):
        if self.state == 0:
            self.toolbar.title = 'Decimal to Binary:'
            self.input.text = 'Enter a decimal number'
            self.label.text = ''
            self.convert_label.text = ''
            self.state = 1
        elif self.state == 1:
            self.toolbar.title = 'Binary to Decimal:'
            self.input.text = 'Enter a binary number'
            self.label.text = ''
            self.convert_label.text = ''
            self.state = 0

    def convert(self, args):
        nums_to_check_in_binary = ['2', '3', '4', '5', '6', '7', '8', '9']

        try:
            if '.' not in self.input.text:
                if self.state == 0:
                    keep_forward = True
                    for ch in self.input.text:
                        if ch in nums_to_check_in_binary:
                            keep_forward = False
                            self.convert_label.text = 'There are not allowed digits in binary format'
                            self.input.text = ''
                            Clock.schedule_once(self.set_focus, .5)

                    if keep_forward:
                        parse_to_int = int(self.input.text, 2)
                        self.label.text = 'Decimal output:'
                        self.convert_label.text = str(parse_to_int)
                elif self.state == 1:
                    parse_to_int = bin(int(self.input.text, 10))[2:]
                    self.label.text = 'Binary output:'
                    self.convert_label.text = parse_to_int
            else:
                whole, fract = self.input.text.split('.')

                if self.state == 0:
                    keep_forward = True
                    for ch in self.input.text:
                        if ch in nums_to_check_in_binary:
                            keep_forward = False
                            self.convert_label.text = 'There are not allowed digits in binary format'
                            self.input.text = ''
                            Clock.schedule_once(self.set_focus, .5)

                    if keep_forward:
                        whole = int(whole, 2)
                        floating = 0

                        for ind, digit in enumerate(fract):
                            floating += int(digit)*2**(-(ind + 1))

                        self.label.text = 'Decimal output:'
                        self.convert_label.text = str(whole + floating)
                elif self.state == 1:
                    decimal_places = 10

                    whole = bin(int(whole))[2:]
                    fract = float("0." + fract)

                    floating = []

                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append('0')
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append('1')
                            fract = fract*2 - 1
                        elif fract*2 == 1:
                            floating.append('1')
                            break
                        
                    self.label.text = 'Binary output:'
                    self.convert_label.text = whole + '.' + ''.join(floating)
        except ValueError:
            self.convert_label.text = ''

            if self.state == 0:
                self.label.text = 'Enter a valid binary number'
            else:
                self.label.text = 'Enter a valid decimal number'

    def build(self):
        self.state = 0

        screen = MDScreen()
        
        self.toolbar = MDToolbar(title="Binary to Decimal:")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ['rotate-3d-variant', lambda x: self.flip(), 'Rotate']
        ]

        screen.add_widget(MDLabel(
            text="Created by Me", 
            pos_hint ={"center_x": 0.5, "center_y": 0.8}, 
            halign="center",
            font_style = 'H3'
            )
        )

        # User input
        self.input = MDTextField(
            text="Enter a binary number",
            halign="center",
            size_hint = (0.8, 1),
            pos_hint ={"center_x": 0.5, "center_y": 0.5}, 
            font_size = 22
        )

        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35}, 
            theme_text_color = 'Secondary' 
        )

        self.convert_label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3}, 
            theme_text_color = 'Primary',
            font_style = "H5" 
        )

        # Button to convert
        screen.add_widget(MDFillRoundFlatButton(
            text = 'CONVERT',
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15}, 
            on_press = self.convert
        ))

        data = {
            'Unncessary functionality added! Whatever :D': 'close-box-outline',
        }

        def add_cb(self):
            Window.close()

        self.floating_btn = MDFloatingActionButtonSpeedDial()
        self.floating_btn.data = data
        self.floating_btn.callback = add_cb
        screen.add_widget(self.floating_btn)

        screen.add_widget(self.toolbar)
        screen.add_widget(self.input)

        screen.add_widget(self.label)
        screen.add_widget(self.convert_label)

        return screen

if __name__ == '__main__':
    ConverterApp().run()