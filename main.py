import customtkinter
import tkinter
from PIL import Image
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import requests
import subprocess
import re
import appdirs
from colorama import Fore, Style
import shutil
from tkinter import filedialog
from pydub import AudioSegment
from tqdm import tqdm
import time

var_settings_themes = [0]

def change_to_music_directory():
    user_home = os.path.expanduser("~")
    music_directory = os.path.join(user_home, "Music")

    try:
        os.chdir(music_directory)
        print(f"Successfully changed to directory: {music_directory}")
    except FileNotFoundError:
        print(f"The directory does not exist: {music_directory}")
    except PermissionError:
        print(f"Permission denied to change to directory: {music_directory}")

def change_to_Videos_directory():
    user_home = os.path.expanduser("~")
    music_directory = os.path.join(user_home, "Videos")

    try:
        os.chdir(music_directory)
        print(f"Successfully changed to directory: {music_directory}")
    except FileNotFoundError:
        print(f"The directory does not exist: {music_directory}")
    except PermissionError:
        print(f"Permission denied to change to directory: {music_directory}")

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CeNtis")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        # load and create background image for Youtube Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_yt_video_downloader = customtkinter.CTkImage(Image.open(current_path + "/images/img2.jpg"),
                                                size=(self.width, self.height))
        self.bg_image_yt_video_downloader_label = customtkinter.CTkLabel(self, image=self.bg_image_yt_video_downloader, text="")
        self.bg_image_yt_video_downloader_label.grid(row=0, column=0)

        # load and create background image for Youtube Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_yt_video_downloader_grey = customtkinter.CTkImage(Image.open(current_path + "/images/darkgrey.jpg"),
                                                size=(self.width, self.height))
        self.bg_image_yt_video_downloader_grey_label = customtkinter.CTkLabel(self, image=self.bg_image_yt_video_downloader_grey, text="")
        self.bg_image_yt_video_downloader_grey_label.grid(row=0, column=0)

        # load and create background image for Youtube Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_yt_video_downloader_grey2 = customtkinter.CTkImage(Image.open(current_path + "/images/darkgrey2.jpg"),
                                                size=(self.width, self.height))
        self.bg_image_yt_video_downloader_grey2_label = customtkinter.CTkLabel(self, image=self.bg_image_yt_video_downloader_grey2, text="")
        self.bg_image_yt_video_downloader_grey2_label.grid(row=0, column=0)

        # load and create background image for Youtube Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_yt_video_downloader_white = customtkinter.CTkImage(Image.open(current_path + "/images/img3.jpg"),
                                                size=(self.width, self.height))
        self.bg_image_yt_video_downloader_white_label = customtkinter.CTkLabel(self, image=self.bg_image_yt_video_downloader_white, text="")
        self.bg_image_yt_video_downloader_white_label.grid(row=0, column=0)

        # load and create background image for Youtube Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_yt_video_downloader_turcoise = customtkinter.CTkImage(Image.open(current_path + "/images/img6.jpg"),
                                                size=(self.width, self.height))
        self.bg_image_yt_video_downloader_turcoise_label = customtkinter.CTkLabel(self, image=self.bg_image_yt_video_downloader_turcoise, text="")
        self.bg_image_yt_video_downloader_turcoise_label.grid(row=0, column=0)

        # load and create background image for Explicit Video Downloader frame
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_xxx_video_downloader = customtkinter.CTkImage(Image.open(current_path + "/images/333366.png"),
                                                size=(self.width, self.height))
        self.bg_image_xxx_video_downloader_label = customtkinter.CTkLabel(self, image=self.bg_image_xxx_video_downloader, text="")
        self.bg_image_xxx_video_downloader_label.grid(row=0, column=0)

        # load and create background image for main
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image_main = customtkinter.CTkImage(Image.open(current_path + "/images/KaliRedSticker.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_main_label = customtkinter.CTkLabel(self, image=self.bg_image_main)
        self.bg_image_main_label.grid(row=0, column=0)

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#12171e')
        self.main_frame.grid(row=0, column=0, sticky="ns")
        self.main_logo = customtkinter.CTkImage(Image.open(current_path + "/images/5.png"), 
                                                size=(350, 150))#size=(300, 100))                                                
        self.main_logo_label = customtkinter.CTkLabel(self.main_frame, image=self.main_logo, text="")
        self.main_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        self.main_optionmenu = customtkinter.CTkOptionMenu(self.main_frame, dynamic_resizing=False,
                                                        values=["-- options --", "Youtube Downloader", "Explicit Video Downloader", "Combination and Convertion", "Settings"], fg_color = "#dc161e", button_color = "#dc161e", button_hover_color = "#ee5157", dropdown_hover_color = "#ee5157")
        self.main_optionmenu.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.main_button = customtkinter.CTkButton(self.main_frame, text="start", command=self.open_option_event, fg_color = "#dc161e", hover_color = "#ee5157", width=200)
        self.main_button.grid(row=2, column=0, padx=30, pady=(15, 15))

        # create Youtube Video Downloader frame 
        self.yt_video_downloader_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#0a256c')#2e6de8')
        self.yt_video_downloader_frame.grid_columnconfigure(0, weight=1)
        self.yt_video_downloader_logo = customtkinter.CTkImage(Image.open(current_path + "/images/youtube6.png"), 
                                                size=(300, 100))#size=(300, 100))                                                
        self.yt_video_downloader_logo_label = customtkinter.CTkLabel(self.yt_video_downloader_frame, image=self.yt_video_downloader_logo, text="")
        self.yt_video_downloader_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        switch_var_1 = customtkinter.StringVar(value="off")
        self.yt_video_downloader_switch = customtkinter.CTkSwitch(self.yt_video_downloader_frame, text="audio only",
                                 variable=switch_var_1, onvalue="on", offvalue="off", progress_color="#489eef")
        self.yt_video_downloader_switch.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_entry = customtkinter.CTkEntry(self.yt_video_downloader_frame, width=200, placeholder_text="enter youtube link", fg_color="#489eef", placeholder_text_color="#0a256c", border_color="#489eef")
        self.yt_video_downloader_entry.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.yt_video_downloader_button_download = customtkinter.CTkButton(self.yt_video_downloader_frame, text="Download", command=self.yt_video_downloader_event, width=200, fg_color = "#489eef", hover_color = "#7ebbf3")
        self.yt_video_downloader_button_download.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_button_back = customtkinter.CTkButton(self.yt_video_downloader_frame, text="back", command=self.back_yt_video_downloader_event, width=75, fg_color = "#489eef", hover_color = "#7ebbf3")
        self.yt_video_downloader_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create Youtube Video Downloader frame darkmode
        self.yt_video_downloader_frame_darkmode = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#333333')
        self.yt_video_downloader_frame_darkmode.grid_columnconfigure(0, weight=1)
        self.yt_video_downloader_logo = customtkinter.CTkImage(Image.open(current_path + "/images/youtube2.png"), 
                                                size=(300, 100))                                               
        self.yt_video_downloader_logo_label = customtkinter.CTkLabel(self.yt_video_downloader_frame_darkmode, image=self.yt_video_downloader_logo, text="")
        self.yt_video_downloader_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        switch_var_2 = customtkinter.StringVar(value="off")
        self.yt_video_downloader_switch_darkmode = customtkinter.CTkSwitch(self.yt_video_downloader_frame_darkmode, text="audio only",
                                 variable=switch_var_2, onvalue="on", offvalue="off", progress_color="#ff0000")
        self.yt_video_downloader_switch_darkmode.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_entry_darkmode = customtkinter.CTkEntry(self.yt_video_downloader_frame_darkmode, width=200, placeholder_text="enter youtube link", fg_color="#ff0000", border_color="#ff0000", placeholder_text_color="white")
        self.yt_video_downloader_entry_darkmode.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.yt_video_downloader_button_download = customtkinter.CTkButton(self.yt_video_downloader_frame_darkmode, text="Download", command=self.yt_video_downloader_event_darkmode, width=200, fg_color = "#ff0000", hover_color = "#ff4c4c")
        self.yt_video_downloader_button_download.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_button_back = customtkinter.CTkButton(self.yt_video_downloader_frame_darkmode, text="back", command=self.back_yt_video_downloader_event, width=75, fg_color = "#ff0000", hover_color = "#ff4c4c")
        self.yt_video_downloader_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create Youtube Video Downloader frame lightmode
        self.yt_video_downloader_frame_lightmode = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='white')
        self.yt_video_downloader_frame_lightmode.grid_columnconfigure(0, weight=1)
        self.yt_video_downloader_logo = customtkinter.CTkImage(Image.open(current_path + "/images/youtube4.png"), 
                                                size=(300, 100))                                               
        self.yt_video_downloader_logo_label = customtkinter.CTkLabel(self.yt_video_downloader_frame_lightmode, image=self.yt_video_downloader_logo, text="")
        self.yt_video_downloader_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        switch_var_3 = customtkinter.StringVar(value="off")
        self.yt_video_downloader_switch_lightmode = customtkinter.CTkSwitch(self.yt_video_downloader_frame_lightmode, text="audio only",
                                 variable=switch_var_3, onvalue="on", offvalue="off", progress_color="#695eff", text_color="black")
        self.yt_video_downloader_switch_lightmode.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_entry_lightmode = customtkinter.CTkEntry(self.yt_video_downloader_frame_lightmode, width=200, placeholder_text="enter youtube link", fg_color="#695eff")
        self.yt_video_downloader_entry_lightmode.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.yt_video_downloader_button_download = customtkinter.CTkButton(self.yt_video_downloader_frame_lightmode, text="Download", command=self.yt_video_downloader_event_lightmode, width=200, fg_color = "#695eff", hover_color = "#695eff")
        self.yt_video_downloader_button_download.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_button_back = customtkinter.CTkButton(self.yt_video_downloader_frame_lightmode, text="back", command=self.back_yt_video_downloader_event, width=75, fg_color = "#695eff", hover_color = "#695eff")
        self.yt_video_downloader_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create Youtube Video Downloader frame turcoise
        self.yt_video_downloader_frame_turcoise = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#147278')
        self.yt_video_downloader_frame_turcoise.grid_columnconfigure(0, weight=1)
        self.yt_video_downloader_logo = customtkinter.CTkImage(Image.open(current_path + "/images/youtube3.png"), 
                                                size=(300, 100))                                               
        self.yt_video_downloader_logo_label = customtkinter.CTkLabel(self.yt_video_downloader_frame_turcoise, image=self.yt_video_downloader_logo, text="")
        self.yt_video_downloader_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        switch_var_4 = customtkinter.StringVar(value="off")
        self.yt_video_downloader_switch_turcoise = customtkinter.CTkSwitch(self.yt_video_downloader_frame_turcoise, text="audio only",
                                 variable=switch_var_4, onvalue="on", offvalue="off", progress_color="#ff4c4c")
        self.yt_video_downloader_switch_turcoise.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_entry_turcoise = customtkinter.CTkEntry(self.yt_video_downloader_frame_turcoise, width=200, placeholder_text="enter youtube link", fg_color="#239f98", border_color="#239f98", placeholder_text_color="white")
        self.yt_video_downloader_entry_turcoise.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.yt_video_downloader_button_download = customtkinter.CTkButton(self.yt_video_downloader_frame_turcoise, text="Download", command=self.yt_video_downloader_event_turcoise, width=200, fg_color = "#239f98", hover_color = "#ff4c4c")
        self.yt_video_downloader_button_download.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.yt_video_downloader_button_back = customtkinter.CTkButton(self.yt_video_downloader_frame_turcoise, text="back", command=self.back_yt_video_downloader_event, width=75, fg_color = "#239f98", hover_color = "#ff4c4c")
        self.yt_video_downloader_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create Explicit Video Downloader frame
        self.xxx_video_downloader_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#333366')#2e6de8')
        self.xxx_video_downloader_frame.grid_columnconfigure(0, weight=1) 
        self.xxx_video_downloader_logo = customtkinter.CTkImage(Image.open(current_path + "/images/explicit2.png"), 
                                                size=(600, 80))                                        
        self.xxx_video_downloader_label = customtkinter.CTkLabel(self.xxx_video_downloader_frame, image=self.xxx_video_downloader_logo, text="")
        self.xxx_video_downloader_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        self.xxx_video_downloader_entry = customtkinter.CTkEntry(self.xxx_video_downloader_frame, width=200, placeholder_text="input download-link", fg_color="#575791", placeholder_text_color="#ff6699", border_color="#575791")##ff6699
        self.xxx_video_downloader_entry.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.xxx_video_downloader_button_download = customtkinter.CTkButton(self.xxx_video_downloader_frame, text="Download", command=self.xxx_video_downloader_event, width=200, fg_color="#575791", hover_color = "#ff6699")
        self.xxx_video_downloader_button_download.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.xxx_video_downloader_button_back = customtkinter.CTkButton(self.xxx_video_downloader_frame, text="back", command=self.back_xxx_video_downloader_event, width=75, fg_color="#575791", hover_color = "#ff6699")
        self.xxx_video_downloader_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create Settings frame
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#12171e')
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_logo = customtkinter.CTkImage(Image.open(current_path + "/images/5.png"), 
                                                size=(100, 100))                                              
        self.settings_logo_label = customtkinter.CTkLabel(self.settings_frame, image=self.settings_logo, text="")
        self.settings_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        radio_var = tkinter.IntVar(value=0)
        self.settings_radiobutton_1 = customtkinter.CTkRadioButton(self.settings_frame, text="Youtube-Blue-Theme",
                                                    command=self.settings_radiobutton_blue_event, variable= radio_var, value=1, fg_color = "green", hover_color = "#dc161e")
        self.settings_radiobutton_1.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.settings_radiobutton_2 = customtkinter.CTkRadioButton(self.settings_frame, text="Youtube-Dark-Mode-Theme",
                                                    command=self.settings_radiobutton_darkmode_event, variable= radio_var, value=2, fg_color = "green", hover_color = "#dc161e")
        self.settings_radiobutton_2.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.settings_radiobutton_3 = customtkinter.CTkRadioButton(self.settings_frame, text="Youtube-Turcois-Theme",
                                                    command=self.settings_radiobutton_turcoise_event, variable= radio_var, value=3, fg_color = "green", hover_color = "#dc161e")
        self.settings_radiobutton_3.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.settings_radiobutton_4 = customtkinter.CTkRadioButton(self.settings_frame, text="Youtube-Light-Mode-Theme",
                                                    command=self.settings_radiobutton_lightmode_event, variable= radio_var, value=4, fg_color = "green", hover_color = "#dc161e")
        self.settings_radiobutton_4.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.settings_button_back = customtkinter.CTkButton(self.settings_frame, text="back", command=self.back_settings_event, width=75, fg_color = "#dc161e", hover_color = "#ee5157")
        self.settings_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create combination and convertion frame
        self.cac_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#12171e')
        self.cac_frame.grid_columnconfigure(0, weight=1)
        self.cac_logo = customtkinter.CTkImage(Image.open(current_path + "/images/audio.png"), 
                                                size=(300, 100))                                              
        self.cac_logo_label = customtkinter.CTkLabel(self.cac_frame, image=self.cac_logo, text="")
        self.cac_logo_label.grid(row=0, column=0, padx=30 , pady=(100, 15))
        self.cac_optionmenu = customtkinter.CTkOptionMenu(self.cac_frame, dynamic_resizing=False,
                                                        values=["-- options --", "Combinate Audio Files", "Convert to .mp3", "Convert to .mp4"], fg_color = "#f00b51", button_color = "#f00b51", button_hover_color = "#ee5157", dropdown_hover_color = "#ee5157")
        self.cac_optionmenu.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.cac_button = customtkinter.CTkButton(self.cac_frame, text="start", command=self.select_file_and_download, fg_color = "#f00b51", hover_color = "#ee5157", width=200)
        self.cac_button.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.cac_button_back = customtkinter.CTkButton(self.cac_frame, text="back", command=self.back_cac_event, width=75, fg_color="#f00b51", hover_color = "#ee5157")
        self.cac_button_back.grid(row=5, column=0, padx=30, pady=(15, 15))

    def open_option_event(self):
        self.bg_image_xxx_video_downloader_label.grid_forget()
        self.bg_image_yt_video_downloader_label.grid_forget()
        self.bg_image_yt_video_downloader_grey_label.grid_forget()
        self.bg_image_yt_video_downloader_grey2_label.grid_forget()
        self.bg_image_yt_video_downloader_white_label.grid_forget()
        self.bg_image_yt_video_downloader_turcoise_label.grid_forget()
        print("Process starting...")
        print("Option: ", self.main_optionmenu.get())
        value_optionmenu = self.main_optionmenu.get()
        if value_optionmenu == "Youtube Downloader":
            global var_settings_themes
            for element in var_settings_themes:
                if element == 1:
                    self.main_frame.grid_forget()  # remove main frame
                    self.bg_image_main_label.grid_forget() # remove default background image
                    self.bg_image_yt_video_downloader_label.grid(row=0, column=0)
                    self.yt_video_downloader_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame
                elif element == 2:
                    self.main_frame.grid_forget()  # remove main frame
                    self.bg_image_main_label.grid_forget() # remove default background image
                    self.bg_image_yt_video_downloader_grey_label.grid(row=0, column=0)
                    self.yt_video_downloader_frame_darkmode.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame
                elif element == 3:
                    self.main_frame.grid_forget()  # remove main frame
                    self.bg_image_main_label.grid_forget() # remove default background image
                    self.bg_image_yt_video_downloader_turcoise_label.grid(row=0, column=0)
                    self.yt_video_downloader_frame_turcoise.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame
                elif element == 4:
                    self.main_frame.grid_forget()  # remove main frame
                    self.bg_image_main_label.grid_forget() # remove default background image
                    self.bg_image_yt_video_downloader_white_label.grid(row=0, column=0)
                    self.yt_video_downloader_frame_lightmode.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame
                else:
                    self.main_frame.grid_forget()  # remove main frame
                    self.bg_image_main_label.grid_forget() # remove default background image
                    self.bg_image_yt_video_downloader_grey_label.grid(row=0, column=0)
                    self.yt_video_downloader_frame_darkmode.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame
        elif value_optionmenu == "Explicit Video Downloader":
            self.main_frame.grid_forget()  # remove main frame
            self.bg_image_main_label.grid_forget() # remove default background image
            self.bg_image_xxx_video_downloader_label.grid(row=0, column=0)
            self.xxx_video_downloader_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show Explicit Video Downloader frame

        elif value_optionmenu == "Combination and Convertion":
            self.main_frame.grid_forget()  # remove main frame
            self.bg_image_main_label.grid_forget() # remove default background image
            self.bg_image_yt_video_downloader_grey2_label.grid(row=0, column=0)
            self.cac_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show Youtube Video Downloader frame

        elif value_optionmenu == "Settings":
            self.main_frame.grid_forget()  # remove main frame
            self.settings_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show Explicit Video Downloader frame

    def back_yt_video_downloader_event(self):
        self.yt_video_downloader_frame.grid_forget()  # remove main frame
        self.yt_video_downloader_frame_darkmode.grid_forget()
        self.yt_video_downloader_frame_lightmode.grid_forget()
        self.yt_video_downloader_frame_turcoise.grid_forget()
        self.bg_image_yt_video_downloader_label.grid_forget()
        self.bg_image_yt_video_downloader_grey_label.grid_forget()
        self.bg_image_yt_video_downloader_white_label.grid_forget()
        self.bg_image_yt_video_downloader_turcoise_label.grid_forget()
        self.bg_image_main_label.grid(row=0, column=0)
        self.main_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def back_xxx_video_downloader_event(self):
        self.xxx_video_downloader_frame.grid_forget()  # remove main frame
        self.bg_image_xxx_video_downloader_label.grid_forget()
        self.bg_image_main_label.grid(row=0, column=0)
        self.main_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def back_cac_event(self):
        self.cac_frame.grid_forget()  # remove main frame
        self.bg_image_yt_video_downloader_grey2_label.grid_forget()
        self.bg_image_main_label.grid(row=0, column=0)
        self.main_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def back_settings_event(self):
        self.settings_frame.grid_forget()  # remove main frame
        self.main_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def yt_video_downloader_event(self):
        def download_video_link_func():
            url = self.yt_video_downloader_entry.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry.get())

                ydl_opts = {
                    'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        def download_audio_link_func():
            url = self.yt_video_downloader_entry.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry.get())

                ydl_opts = {
                    'format': 'bestaudio[ext=m4a]',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        switch_value = self.yt_video_downloader_switch.get()
        print("Switch:" ,self.yt_video_downloader_switch.get())
        change_to_music_directory()
        if switch_value == "off":
            download_video_link_func()
        elif switch_value == "on":
            download_audio_link_func()

    def yt_video_downloader_event_darkmode(self):
        def download_video_link_func():
            url = self.yt_video_downloader_entry_darkmode.get()
            if len(url) == 0:
                print("No input found...")
            else:
                if url.startswith('https://youtu.be') or url.startswith('https://www.youtube'):
                    print("Download Button Pressed - link:", self.yt_video_downloader_entry_darkmode.get())

                    ydl_opts = {
                        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',         
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download(url)
                else:
                    print("invalid youtube url!")
                    print("please try again...")

        def download_audio_link_func():
            url = self.yt_video_downloader_entry_darkmode.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry_darkmode.get())

                ydl_opts = {
                    'format': 'bestaudio[ext=m4a]',
                    #'format': 'bestaudio/best',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        switch_value = self.yt_video_downloader_switch_darkmode.get()
        print("Switch:" ,self.yt_video_downloader_switch_darkmode.get())
        change_to_music_directory()
        if switch_value == "off":
            download_video_link_func()
        elif switch_value == "on":
            download_audio_link_func()
        print("done...")        

    def yt_video_downloader_event_lightmode(self):
        def download_video_link_func():
            url = self.yt_video_downloader_entry_lightmode.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry_lightmode.get())

                ydl_opts = {
                    'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        def download_audio_link_func():
            url = self.yt_video_downloader_entry_lightmode.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry_lightmode.get())

                ydl_opts = {
                    'format': 'bestaudio[ext=m4a]',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        switch_value = self.yt_video_downloader_switch_lightmode.get()
        print("Switch:" ,self.yt_video_downloader_switch_lightmode.get())
        change_to_music_directory()
        if switch_value == "off":
            download_video_link_func()
        elif switch_value == "on":
            download_audio_link_func()

    def yt_video_downloader_event_turcoise(self):
        def download_video_link_func():
            url = self.yt_video_downloader_entry_turcoise.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry_turcoise.get())

                ydl_opts = {
                    'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        def download_audio_link_func():
            url = self.yt_video_downloader_entry_turcoise.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.yt_video_downloader_entry_turcoise.get())

                ydl_opts = {
                    'format': 'bestaudio[ext=m4a]',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        switch_value = self.yt_video_downloader_switch_turcoise.get()
        print("Switch:" ,self.yt_video_downloader_switch_turcoise.get())
        change_to_music_directory()
        if switch_value == "off":
            download_video_link_func()
        elif switch_value == "on":
            download_audio_link_func()
    
    def xxx_video_downloader_event(self):
        def get_video_folder():
            video_folder = appdirs.user_data_dir(appname='ExplicitDownloader', appauthor=False)
            return video_folder
        def get_user_folder_name():
            folder_name = ''
            return folder_name
        def gotanynudes(url):
            change_to_Videos_directory()
            url = url
            def vid_crawler(url, folder_name):
                def extract_video_links(url):
                    response = requests.get(url)
                
                    if response.status_code == 200:
                        page_content = response.text
                        video_links = set()


                        video_extensions = ['mp4', 'mov', 'mpeg', 'gif']
                        pattern = r'(https?://[^\s/$.?#].[^\s]*)'
                        for ext in video_extensions:
                            pattern += f'\.{ext}|'
                        pattern = pattern[:-1]  

                        matches = re.finditer(pattern, page_content, re.IGNORECASE)
                        for match in matches:
                            video_links.add(match.group(0))

                        return video_links

                    return None
                
                def download_links_from_file(links_file, download_folder):
                    if not os.path.exists(download_folder):
                        os.makedirs(download_folder)
                    with open(links_file, "r") as file:
                        for line in file:
                            url = line.strip()
                            if url:
                                os.system('clear')
                                print(f"[{Fore.YELLOW}url{Style.RESET_ALL}] -> {url}")
                                print(f"[{Fore.YELLOW}folder{Style.RESET_ALL}] -> {download_folder}")
                                download_file(url, download_folder)
                
                def download_file(url, folder):
                    response = requests.get(url, stream=True)
                    if response.status_code == 200:
                    
                        content_length = response.headers.get('Content-Length')
                        if content_length is not None:
                            file_size = int(content_length)
                            print(f"[{Fore.YELLOW}filesize{Style.RESET_ALL}] {file_size} Bytes")

                        filename = os.path.join(folder, url.split("/")[-1])
                        downloaded_bytes = 0  

                        with open(filename, 'wb') as f:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                                    downloaded_bytes += len(chunk)

                                    if file_size is not None:
                                    
                                        progress = (downloaded_bytes / file_size) * 100
                                        print(f"[{Fore.YELLOW}Download{Style.RESET_ALL}] {Fore.YELLOW}{progress:.2f}%{Style.RESET_ALL}", end='\r')

                
                video_links = extract_video_links(url)

                if video_links:
                    with open("links.txt", "w") as file:
                        for link in video_links:
                            file.write(link + '\n')
                    print(f"{Fore.YELLOW}### {Style.RESET_ALL}{Fore.WHITE}[Progress] Video links saved to 'links.txt'{Style.RESET_ALL}{Fore.YELLOW} ###{Style.RESET_ALL}")

                links_file = "links.txt"  
                    
                download_folder = os.path.join("download_files", folder_name)
                if not os.path.exists(download_folder):
                    os.makedirs(download_folder)
                download_links_from_file(links_file, download_folder)
                print(f"[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> {download_folder}")
                os.remove("links.txt")
            folder_name = get_user_folder_name()
            vid_crawler(url, folder_name)
        def pornhub(url):
            change_to_Videos_directory()
            os.chdir('download_files')
            os.system(f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {url}")
        
        def read_and_print_links_with_progress(path_to_text_file):
            try:
                with open(path_to_text_file, 'r') as file:
                    all_links = file.readlines()
                    total_links = len(all_links)
                    print(f"Links: {total_links}\n")

                    for i, line in enumerate(all_links):
                        akt_link = line.strip()
                        time.sleep(0.1)
                        
                        if re.search(r'gotanynudes\.com', akt_link):
                            gotanynudes(akt_link)
                        elif re.search(r'pornhub\.com', akt_link):
                            pornhub(akt_link)
                        elif re.search(r'xhamster\.com', akt_link):
                            xhamster(akt_link)
                        elif re.search(r'xvideos\.com', akt_link):
                            xvideos(akt_link)
                        elif re.search(r'xnxx\.com', akt_link):
                            xnxx(akt_link)
                        
                        progress = ((i + 1) / total_links) * 100
                        print(f"Progress: {progress:.2f}%", end='\r')

                        time.sleep(0.1)
            except FileNotFoundError:
                print(f"The File '{path_to_text_file}' was not found.")
            except Exception as e:
                print(f"Error: {e}")
        
        def xhamster(url):
            change_to_Videos_directory()
            def rename_to_mp4(folder_path):
                if os.path.exists(folder_path):
                    for filename in os.listdir(folder_path):
                        original_path = os.path.join(folder_path, filename)
                        if os.path.isfile(original_path):
                            file_name, file_extension = os.path.splitext(filename)
                            if file_extension != '.mp4':
                                new_extension = '.mp4'
                                new_filename = file_name + new_extension
                                new_path = os.path.join(folder_path, new_filename)
                                os.rename(original_path, new_path)
                                print(f"Renamed: {file_name}{file_extension} to {file_name}{new_extension}")
                else:
                    print(f"The folder '{folder_path}' does not exist.")
            def find_and_save_mp4_links(url):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    mp4_pattern = re.compile(r'https?://.*\.mp4')
                    with open('mp4_links.txt', 'w') as mp4_file:
                        for link in soup.find_all('a'):
                            href = link.get('href')
                            if href and mp4_pattern.search(href):
                                mp4_url = urljoin(url, href)  
                                mp4_file.write(mp4_url + '\n')
                    
                    print(f"[{Fore.YELLOW}process{Style.RESET_ALL}] -> .mp4-link saved to 'mp4_links.txt'")
                
                except Exception as e:
                    print(f'[{Fore.RED}error{Style.RESET_ALL}] Error occured while downloading or analyying element {e}')   
            def download_hamster():
                def get_user_folder_name():
                    folder_name = ''
                    return folder_name

                def download_mp4_files(links, download_directory):
                    if not os.path.exists(download_directory):
                        os.makedirs(download_directory)
                
                    for link in links:
                        try:
                            response = requests.get(link)
                            response.raise_for_status()
                            file_name = link.split("/")[-1]
                            file_path = os.path.join(download_directory, file_name)
                            with open(file_path, 'wb') as mp4_file:
                                mp4_file.write(response.content)
                        
                            print(f'[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> file stored in {download_directory}')
                    
                        except Exception as e:
                            print(f'[{Fore.RED}error{Style.RESET_ALL}] Error while downloading file {e}')

                folder_name = get_user_folder_name()
                script_directory = os.path.dirname(os.path.abspath(__file__))
                download_directory = os.path.join(script_directory, 'download_files', folder_name)
                with open('mp4_links.txt', 'r') as file:
                    mp4_links = file.read().splitlines()

                download_mp4_files(mp4_links, download_directory)
                os.remove("mp4_links.txt")
            find_and_save_mp4_links(url)
            download_hamster()
            folder_path = "download_files"
            rename_to_mp4(folder_path)
        def xvideos(url_orig):
            change_to_Videos_directory()
            def remove_characters_until_https(input_string):
                https_index = input_string.find("https://")
                
                if https_index != -1:
                    result_string = input_string[https_index:]
                    return result_string
                else:
                    return input_string

            def download_link(url, destination):
                try:
                    response = requests.get(url)
                    response.raise_for_status()

                    with open(destination, 'wb') as file:
                        file.write(response.content)

                except requests.exceptions.RequestException as e:
                    print(f"[ERROR] while downloading link: {e}")

            def find_hls_1080p_url(m3u8_file_path):
                try:
                    with open(m3u8_file_path, 'r') as file:
                        lines = file.readlines()
                        for line_number, line in enumerate(lines):
                            if line.strip().startswith("hls-1080p"):
                                return line.strip(), line_number
                    return None, -1
                except FileNotFoundError:
                    print(f"[ERROR] file {m3u8_file_path} not found.")
                    return None, -1

            def replace_characters(input_string, replacement):
                return input_string.replace('hls.m3u8', replacement)

            def filter_hls_lines(input_file_path, output_file_path):
                try:
                    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
                        for line in input_file:
                            if line.strip().startswith("hls"):
                                output_file.write(line)
                    
                except FileNotFoundError:
                    print(f"[ERROR] file {input_file_path} not found.")

            def remove_hls_m3u8_from_link(link):
                new_link = link.replace('hls.m3u8', '')
                return new_link

            def insert_link_to_each_line(file_path, new_link, output_file_path):
                try:
                    with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
                        for line in input_file:
                            updated_line = new_link + line
                            output_file.write(updated_line)
                    
                except FileNotFoundError:
                    print(f"[ERROR] file {file_path} not found.")

            def download_links_from_file(file_path, download_directory):
                try:
                    with open(file_path, 'r') as file:
                        for line_number, line in enumerate(file, start=1):
                            line = line.strip()
                            if line:
                                try:
                                    response = requests.get(line, stream=True)
                                    response.raise_for_status()

                                    file_name = f"{line_number}.ts"
                                    file_path = f"{download_directory}/{file_name}"

                                    with open(file_path, 'wb') as downloaded_file:
                                        for chunk in response.iter_content(chunk_size=8192):
                                            if chunk:
                                                downloaded_file.write(chunk)

                                    print(f"File {file_name} downloaded")
                                except requests.exceptions.RequestException as e:
                                    print(f"[ERROR] while downloading line {line_number}: {e}")
                    
                except FileNotFoundError:
                    print(f"[ERROR] file {file_path} not found")

            def combine_ts_files(input_folder, output_file):
                
                ts_files = [f for f in os.listdir(input_folder) if f.endswith('.ts')]
                ts_files.sort(key=lambda x: int(x.split('.')[0]))

                if not ts_files:
                    print("[ERROR] no .ts-File in folder found.")
                    return

                
                with open('filelist.txt', 'w') as filelist:
                    for ts_file in ts_files:
                        filelist.write(f"file '{os.path.join(input_folder, ts_file)}'\n")

            
                os.system(f"ffmpeg -f concat -safe 0 -i filelist.txt -c copy {output_file}")

            
                os.remove('filelist.txt')

                

            def ts_to_mp4(input_ts_file, output_mp4_file):
                try:
                    cmd = f'ffmpeg -i {input_ts_file} -c:v copy -c:a aac -strict experimental -y {output_mp4_file}'
                    subprocess.run(cmd, shell=True, check=True)
                    
                except subprocess.CalledProcessError as e:
                    print(f"[ERROR] while converting file {input_ts_file}: {e}")

            def get_title_from_link(url):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.title.string
                    return title
                except Exception as e:
                    print(f"[ERROR] while fetching title: {e}")
                    return None

            def entferne_sonderzeichen(text):
                return re.sub(r'[^A-Za-z0-9\s]', '', text)

            def entferne_leerzeichen(text):
                return text.replace(" ", "")
            #----------------get_link_hls.m3u8----------------------------------------
            if not os.path.exists('download_files'):
                os.mkdir('download_files')
            os.chdir('download_files')
            os.mkdir('ts_downloads')

            user_input = url_orig
            title = get_title_from_link(user_input)
            if title:
                print(f"[title] {title}")
            else:
                print("[ERROR] title not found")
            response = requests.get(user_input)
            html_content = response.text


            pattern = r'(.*?hls\.m3u8)'


            matches = re.findall(pattern, html_content)

            if matches:
                for match in matches:
                    print("Found link for hls.m3u8-File:", match)
            else:
                print("[ERROR] no hls.m3u8-File found in source-code.")

            #----------------print_link_hls.m3u8--------------------------------------
            result = remove_characters_until_https(match)
            print(result)
            #----------------download_link_hls.m3u8-----------------------------------
            url = result  
            ziel_datei = "hls.m3u8"
            download_link(url, ziel_datei)
            #----------------read_hls.m3u8--------------------------------------------

            available_resolutions = {}  

            with open("hls.m3u8", 'r') as hls_file:
                lines = hls_file.readlines()
                resolution = None

                for line in lines:
                    if line.startswith("#EXT-X-STREAM-INF"):
                        
                        resolution = re.search(r'RESOLUTION=(\d+x\d+)', line).group(1)
                    elif line.startswith("hls-"):
                        
                        available_resolutions[resolution] = line.strip()


            highest_resolution = max(available_resolutions.keys(), key=lambda x: int(x.split('x')[0]))


            selected_m3u8_file = available_resolutions[highest_resolution]
            download_link(selected_m3u8_file, selected_m3u8_file)
            print(f"highest resolution: ",{highest_resolution}) 

            result = remove_characters_until_https(match)
            input_string = result
            replacement = selected_m3u8_file
            result3 = replace_characters(input_string, replacement)
            
            #----------------download_hls-highest-quality.m3u8----------------------------------
            url = result3  
            ziel_datei = selected_m3u8_file
            download_link(url, ziel_datei)
            #----------------edit_hls-highest-quality.m3u8--------------------------------------
            input_file_path = selected_m3u8_file  
            output_file_path = "new_hls.m3u8"

            filter_hls_lines(input_file_path, output_file_path)
            #----------------download-.ts-files-from-new_hls.m3u8---------------
            link = result
            new_link = remove_hls_m3u8_from_link(link)
            

            file_path = "new_hls.m3u8"
            new_link = new_link
            output_file_path = "link_plus_new_hls.m3u8"

            insert_link_to_each_line(file_path, new_link, output_file_path)

            file_path = "link_plus_new_hls.m3u8"
            download_directory = "ts_downloads"

            download_links_from_file(file_path, download_directory)
            #----------------combine_ts_files_into_mp4_file---------------------------
            input_folder = download_directory
            output_file = 'movie.ts'
            combine_ts_files(input_folder, output_file)

            input_ts_file = 'movie.ts'
            output_mp4_file = title
            output_mp4_file_new = entferne_leerzeichen(entferne_sonderzeichen(output_mp4_file) + '.mp4')
            ts_to_mp4(input_ts_file, output_mp4_file_new)
            #----------------delete_files---------------------------------------------
            os.remove('hls.m3u8')
            os.remove(selected_m3u8_file)
            os.remove('link_plus_new_hls.m3u8')
            os.remove('new_hls.m3u8')
            os.remove('movie.ts')
            shutil.rmtree('ts_downloads')

            subprocess.run(["rm", "-rf", "~/.local/share/Trash"])
        def xnxx(url):
            xvideos(url)
            
        change_to_Videos_directory()
        url = self.xxx_video_downloader_entry.get()
        video_folder = get_video_folder()
        os.makedirs(video_folder, exist_ok=True)
        self.xxx_video_downloader_entry.grid_forget()
        self.xxx_video_downloader_entry = customtkinter.CTkEntry(self.xxx_video_downloader_frame, width=200, placeholder_text="input download-link", fg_color="#575791", placeholder_text_color="#ff6699", border_color="#575791")##ff6699
        self.xxx_video_downloader_entry.grid(row=1, column=0, padx=30, pady=(175, 15))
        if not os.path.exists('download_files'):
            os.makedirs('download_files')
        if re.search(r'gotanynudes\.com', url):
            '''self.xxx_video_downloader_label.grid_forget()
            self.xxx_video_downloader_gotanynudes_label.grid(row=0, column=0, padx=30 , pady=(100, 15))'''
            gotanynudes(url)
        elif re.search(r'pornhub\.com', url):
            '''self.xxx_video_downloader_label.grid_forget()
            self.xxx_video_downloader_pornhub_label.grid(row=0, column=0, padx=30 , pady=(100, 15))'''
            pornhub(url)
        elif re.search(r'xhamster\.com', url):
            '''self.xxx_video_downloader_label.grid_forget()
            self.xxx_video_downloader_xhamster_label.grid(row=0, column=0, padx=30 , pady=(100, 15))'''
            xhamster(url)
        elif re.search(r'xvideos\.com', url):
            '''self.xxx_video_downloader_label.grid_forget()
            self.xxx_video_downloader_xvideos_label.grid(row=0, column=0, padx=30 , pady=(100, 15))'''
            xvideos(url)
        elif re.search(r'xnxx\.com', url):
            '''self.xxx_video_downloader_label.grid_forget()
            self.xxx_video_downloader_xnxx_label.grid(row=0, column=0, padx=30 , pady=(100, 15))'''
            xnxx(url)
        elif re.search(r'/home/', url):
            read_and_print_links_with_progress(url)
        else:
            self.xxx_video_downloader_entry.grid_forget()
            self.xxx_video_downloader_entry = customtkinter.CTkEntry(self.xxx_video_downloader_frame, width=200, placeholder_text="unsupported link", fg_color="#575791", placeholder_text_color="#ff0000", border_color="#ff0000")##ff6699
            self.xxx_video_downloader_entry.grid(row=1, column=0, padx=30, pady=(175, 15))

    def select_file_and_download(self):
        val_optionmenu = self.cac_optionmenu.get()
        if val_optionmenu == "Combinate Audio Files":
            file_path = filedialog.askdirectory(initialdir="/", title="Select File")
            print(file_path)
            def combine_audio_files(input_folder, output_file):
                files = os.listdir(input_folder)
                audio_files = [file for file in files if file.endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a'))]
                combined = AudioSegment.silent(duration=0)

                for audio_file in audio_files:
                    file_path = os.path.join(input_folder, audio_file)
                    sound = AudioSegment.from_file(file_path)
                    combined += sound

                combined.export(output_file, format="mp3")
            user_home = os.path.expanduser("~")
            output_file = os.path.join(user_home, "Music", "audio_combination.mp3")
            combine_audio_files(file_path, output_file)
            print("done...")            
        elif val_optionmenu == "Convert to .mp3":
            file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.m4a"), ("Text files", "*.wav"), ("Text files", "*.ogg"), ("Text files", "*.flac"), ("All files", "*.opus")))
            print(file_path)
        elif val_optionmenu == "Convert to .mp4":
            file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.*")))
            print(file_path)    

    def settings_radiobutton_blue_event(self):
        global var_settings_themes
        var_settings_themes.clear()
        var_settings_themes.append(1)
        print(var_settings_themes)
    def settings_radiobutton_darkmode_event(self):
        global var_settings_themes
        var_settings_themes.clear()
        var_settings_themes.append(2)
        print(var_settings_themes)
    def settings_radiobutton_turcoise_event(self):
        global var_settings_themes
        var_settings_themes.clear()
        var_settings_themes.append(3)
        print(var_settings_themes)
    def settings_radiobutton_lightmode_event(self):
        global var_settings_themes
        var_settings_themes.clear()
        var_settings_themes.append(4)
        print(var_settings_themes)

if __name__ == "__main__":
    app = App()
    app.mainloop()
