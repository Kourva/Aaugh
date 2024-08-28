#!/usr/bin/env python3

# Imports
from sys import exit
import pygame
import random
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar.toolbar import MDTopAppBar
from kivymd.uix.slider.slider import MDSlider
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.clock import Clock
pygame.mixer.init()

# App Class
class AaughApp(MDApp):

    # Opens Github Dialog
    def githubOpen(self, *args):
        self.Github.open()

    # Closes Github Dialog
    def githubClose(self, *args):
        self.Github.dismiss(force=True)

    # Updater
    def update(self, *args):
        value = int(self.Slider.value)
        chnl = random.randint(0,6)
        self.Text.text = f"Current Value = {str(value).rjust(5)}"
        if value == 0:
            pass
        elif value == 1:
            channel = pygame.mixer.Channel(chnl)
            punch = pygame.mixer.Sound(f"Samples/{1}.wav")
            channel.play(punch)
        else:
            channel = pygame.mixer.Channel(chnl)
            punch = pygame.mixer.Sound(f"Samples/{value//2}.wav")
            channel.play(punch)


    # Build method
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # Home Screen
        home = MDScreen()


        # Top Toolbar
        self.Toolbar = MDTopAppBar(
            opposite_colors = True,
            title = "Aaaaaaaugh",
            pos_hint = {"top": 1},
            right_action_items = [
                ["close-thick", lambda _: exit()]
            ]
        ) 

        # Slider
        self.Slider = MDSlider(
            size_hint = (.5, .5),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            show_off = True,
            value = "0",
            step = 2
        )

        # Text Label
        self.Text = MDLabel(
            font_style= "H6",
            text = "Current Value = 0",
            theme_text_color = "Custom",
            text_color = "orange",
            halign = "center",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
        )

        # Github Dialog
        self.Github = MDDialog(
            title = "Developers",
            text = "NetworkDeus: https://github.com/NetworkDeus\nKourva: https://github.com/Kourva",
            buttons = [
                MDFlatButton(
                    text = "Close",
                    theme_text_color = "Custom",
                    text_color = "orange",
                    on_press = self.githubClose
                )
            ]
        )

        self.LIcon = MDIconButton(
            icon="emoticon-poop",
            theme_text_color = "Custom",
            text_color = "orange",
            pos_hint={"center_x": 0.22, "center_y": 0.5},
            on_press = self.githubOpen
        )
        self.RIcon = MDIconButton(
            icon="emoticon-poop",
            theme_text_color = "Custom",
            text_color = "orange",
            pos_hint={"center_x": 0.78, "center_y": 0.5},
            on_press = self.githubOpen
        )

        # Updater
        Clock.schedule_interval(lambda _:self.update(self.Text, self.Slider), .01)

        # Add widgets
        home.add_widget(self.Toolbar)
        home.add_widget(self.Slider)
        home.add_widget(self.LIcon)
        home.add_widget(self.RIcon)
        home.add_widget(self.Text)

        # Return home
        return home

# Run
AaughApp().run()
