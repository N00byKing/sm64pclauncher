#!/usr/bin/python3

import PySimpleGUI as sg
import os
from sys import exit
from themeconfig import *
from urllib.request import urlopen
sg.theme_background_color(windowBackgroundColor)

mode = 'r' if os.path.exists('builds.txt') else 'w+'
with open('builds.txt', mode) as blist:
    builds = blist.readlines()
mode = 'r' if os.path.exists('launchopts.txt') else 'w+'
with open('launchopts.txt', mode) as optlist:
    launch_opts = optlist.read()

url = "https://raw.githubusercontent.com/N00byKing/sm64pclauncher/archipelago/news.txt"
newstext = urlopen(url).read().decode("utf-8")

news=[
    [sg.Text('News', font=(1), background_color=windowBackgroundColor, text_color=textColor)],
    [sg.Multiline(newstext, disabled=True, size=(36, 16), background_color=boxColor, text_color=boxTextColor)]
    ]
options=[
    [sg.Button('Play', size=(10, 2), button_color=("white", playButtonColor),font=(1),disabled=True)],
    [sg.Button('Build', size=(14, 1), button_color=('white', otherButtonColor))],
    [sg.Text("Launch Options:", background_color=windowBackgroundColor, text_color=textColor)],
    [sg.Multiline(default_text=launch_opts, background_color=boxColor, text_color=boxTextColor, key="launchopt")]
]
buildselect=[[
    sg.Text('Select your sm64pc build:', background_color=windowBackgroundColor, text_color=textColor),

],
[
    sg.Listbox(
        values=builds, enable_events=True,select_mode='single', size=(40, 20), key="buildlist", bind_return_key = True, background_color=boxColor, text_color=boxTextColor
    )
]
]
   
layout = [
    [
        sg.Column(buildselect, size=(200, 300)),
        sg.VSeperator(),
        sg.Column(options,size=(200, 300)),
        sg.VSeparator(),
        sg.Column(news, size=(300, 300)),
    ]
]
    
window = sg.Window('SM64pc launcher', layout)
while True:
    event, values = window.read()
    if event == 'buildlist':
        buildselected = os.path.join(
            values['buildlist'][0]
        )

        buildselected = buildselected.rstrip("\n")
        if buildselected == "":
            window['Play'].update(disabled=True)
        if not buildselected == "":
            window["Play"].update(disabled=False)
    if event == "Play":
        buildfolder, sep, region = buildselected.partition(':')
        launchoptionslist = values['launchopt']
        with open('launchopts.txt', 'w+') as optlist:
            optlist.write(launchoptionslist)
        launchoptions = ""
        for launcho in values['launchopt']:
            launchoptions += launcho.replace("\n", " ") 
        if os.name == 'nt':
            os.system('"'+buildfolder+'\\build\\'+region+'_pc\\sm64.'+region+'.f3dex2e.exe '+launchoptions+'"')
        if os.name == 'posix':
            os.system('cd "'+buildfolder+'/build/'+region+'_pc/" && ./sm64.'+region+'.f3dex2e '+launchoptions+'')
        break
        
    if event == 'Build':
        import builder
        with open('builds.txt', 'r') as blist:
            builds = blist.readlines()
        window.Element('buildlist').Update(values=builds)
    if event == sg.WIN_CLOSED:
        exit()

        
