import pygame
import time
import easygui
import os
easygui.msgbox('基于 Python3.6，Pygame2.1.2,Easygui 0.98.3')
musicList = 'Music/'
MusicName = os.listdir(musicList)
chooseName = os.listdir(musicList)
path = r"Music/";
def play():
	global playName
	global value
	value = 0
	play = easygui.buttonbox('选择音乐',choices=chooseName,title=['CHooseMusic'])
	if play in MusicName:
		playName = path+play
		Music()
def Music():
	pygame.mixer.init()
	pygame.mixer.music.load(playName)
	pygame.mixer.music.play(start=0.0)
	#播放时长
	easygui.msgbox('停止音乐')
	pygame.mixer.music.stop()
	play()
play()