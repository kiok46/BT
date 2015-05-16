# -*- coding: UTF-8 -*-
__version__ = '1.0'

from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Property, ListProperty, BooleanProperty
from kivy.graphics import Canvas, Color, BorderImage
from kivy.animation import Animation
from kivy.clock import Clock, ClockEvent
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import SlideTransition, FadeTransition
#from kivy.utils import platform

#from jnius import autoclass
	
#PythonActivity = autoclass('org.renpy.android.PythonActivity')
#activity = PythonActivity.mActivity
#Context = autoclass('android.content.Context')
#PowerManager = autoclass('android.os.PowerManager')
#pm = activity.getSystemService(Context.POWER_SERVICE)
#wl = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, 'TAG')
#wl.acquire()


Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<Butt@Button>:
    background_normal: './data/44.png'
    background_down: './data/4.png'
    background_disabled_normal: './data/4.png'


<Butt1@Button>:
    background_normal: './data/nb.png'
    background_down: './data/nb_down.png'
    background_disabled_normal: './data/nb.png'


<BoxingTimer>:
	BoxLayout:
		orientation: 'vertical'	
		canvas:
			Color:
				rgb: .16, .16, .24    
			Rectangle:
				size: self.size
				pos: self.pos			    
		ScreenManager:
			id: screen_manager
			    	
			Screen:			
				name: 'screen1'
				BoxLayout:
					orientation: 'vertical'
			        size_hint_x: 0.9
			        pos_hint: {'center_x': 0.5}

			        BoxLayout:
			        	orientation: 'vertical'
			        	size_hint_y: 1.3
			        	BoxLayout:
			        	BoxLayout:
				        	BoxLayout:
				        		orientation: 'vertical'
					        	BoxLayout:
					        		Label:
					        			font_size: min(self.height, self.width/2) / 1.5
					        			text:str(("%02d")%(root.timeRound//60))+':'+str(("%02d")%((root.timeRound% 60)))
					        			bold: True
					        	BoxLayout:
					        		size_hint_y:0.3
					        		Label:
					        			text:'round'
					        
					        BoxLayout:	
					        	orientation: 'vertical'
						        BoxLayout:
						        	Label:
						        		font_size: min(self.height, self.width/2) / 1.5
						        		text: str(("%02d")%(root.timePause//60))+':'+str(("%02d")%((root.timePause% 60)))
						        		bold: True 
					        	BoxLayout:
					        		size_hint_y:0.3
					        		Label:
					        			text:'pause'

						    BoxLayout:   	
						        orientation: 'vertical'	
						        BoxLayout:
						        	Label:
						        		font_size: min(self.height, self.width/2) / 1.5
						        		text: str(root.raund)
						        		bold: True
					        	BoxLayout:
					        		size_hint_y:0.3
					        		Label:
					        			text:'rounds'

						BoxLayout:
						        		
			        BoxLayout:
			        	size_hint_y: 0.3
						
						Butt:
							text:'Round'
							on_release:root.menu_screen('screen1') if root.block_button==False else ''
							disabled: True if screen_manager1.current == 'screen1' else False			
						
						Butt:
							text:'Pause'
							on_release:root.menu_screen('screen2') if root.block_button==False else ''
							disabled: True if screen_manager1.current == 'screen2' else False

						Butt:
							text:'Rounds'        	
							on_release:root.menu_screen('screen3') if root.block_button==False else ''	
							disabled: True if screen_manager1.current == 'screen3' else False

			        BoxLayout:
			        	size_hint_y: 2
					    ScreenManager:
					    	id: screen_manager1
					    	Screen: 					    	
								name: 'screen1'
								on_enter:root.block_button=False
								BoxLayout:
									orientation: 'vertical'
									BoxLayout:
									BoxLayout:
										spacing: '5dp'
										padding: '5dp'
										Butt1:
											text:'+30sec'
											on_release:root._timeRound(30)
										Butt1:
											text:'+1min'
											on_release:root._timeRound(60)
										Butt1:
											text:'+2min'
											on_release:root._timeRound(120)
										Butt1:
											text:'+3min'
											on_release:root._timeRound(180)
										Butt1:
											text:'+5min'
											on_release:root._timeRound(300)
									BoxLayout:
										padding: '5dp'
										Butt1:
											text:'RESET'
											on_release:root._timeRound_reset()
									BoxLayout:
					    	
					    	Screen:
								name: 'screen2'
								on_enter:root.block_button=False					        	
								BoxLayout:
									orientation: 'vertical'
									BoxLayout:
									BoxLayout:
										spacing: '5dp'
										padding: '5dp'
										
										Butt1:
											text:'+5sec'
											on_release:root._timePause(5)
										Butt1:
											text:'+15sec'
											on_release:root._timePause(15)
										Butt1:
											text:'+30sec'
											on_release:root._timePause(30)
										Butt1:
											text:'+45sec'
											on_release:root._timePause(45)
										Butt1:
											text:'+1min'
											on_release:root._timePause(60)
						
									BoxLayout:
										padding: '5dp'
										Butt1:
											text:'RESET'
											on_release:root._timePause_reset()
									BoxLayout:
					    	
					    	Screen:
								name: 'screen3'
								on_enter:root.block_button=False
								BoxLayout:
									orientation: 'vertical'
									BoxLayout:
									BoxLayout:
										spacing: '5dp'
										padding: '5dp'
										
										Butt1:
											text:'+1 round'
											on_release:root._round_plus()
										Butt1:
											text:'-1 round'
											on_release:root._round_minus()														
									
									BoxLayout:
									BoxLayout:

			        BoxLayout:
			        	size_hint_y: 0.5
			        	Butt1:
			        		text:'START'
			        		on_release:root.start_timer() 
			   
			        BoxLayout:
			        	size_hint_y: 0.2        		

			Screen:
				name: 'screen2'
				canvas:
					Color:
						rgb: .18, .85, .18    
					Rectangle:
						size: self.size
						pos: self.pos				
				BoxLayout:
					orientation: 'vertical'
			        size_hint_x: 0.9
			        pos_hint: {'center_x': 0.5}

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		size_hint_y: 0.5
			        	BoxLayout:
			        		BoxLayout:
			        			Butt1:
			        				text:'back'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.stop(); screen_manager.transition = SlideTransition(direction="left");screen_manager.current = "screen1"		
			        				        		
			        		BoxLayout:
			        			size_hint_x: 1.4
			        		BoxLayout:
			        			Butt1:
			        				text:'restart'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.resetTimer()			        		
			        	BoxLayout:
			        	BoxLayout:
			        		Label:
			        			text:'Round: '+str(root.raund_index)
			        			font_size: min(self.height, self.width/2.5) / 1.4
			        			bold: True

			        BoxLayout:
			        	id: ellips_clock
			        	size_hint_y: 2
			        	Label:
			        		text:str(("%02d")%(root.timeRound//60))+':'+str(("%02d")%((root.timeRound% 60)))
			        		font_size: min(self.height, self.width/2.5) / 2
			        		bold: True
				        	canvas.before:
								Color:
									rgb: .0, .74, .13    
								Ellipse:			        	
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10) 

								Color:
									rgb: .40, .99, .0    
								Ellipse:
									angle_end: root.time360
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10)

								Color:
									rgb: .18, .85, .18     
								Ellipse:											        	
									size: (ellips_clock.size[1]-80,ellips_clock.size[1]-80)
									pos: (self.center_x-((ellips_clock.size[1]/2)-40), ellips_clock.pos[1]+40)

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		orientation: 'vertical'
				        	BoxLayout:
				        		size_hint_y: 1
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(("%02d")%(root.timeRound_i//60))+':'+str(("%02d")%((root.timeRound_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'round'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:(("%02d")%(root.timePause_i//60))+':'+str(("%02d")%((root.timePause_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'pause'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(root.raund)
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'Rounds'

				        	BoxLayout:
				        		size_hint_y: 0.2
				        				
			        	BoxLayout:
			        		Butt1:
			        			size_hint_y: 1
			        			text:'Pause' if root.pause_index==False else 'Start'
			        			font_size: min(self.height, self.width/2.5) / 2.5
			        			on_release:root.pause()			        	
			        	BoxLayout:
			        		size_hint_y: 0.2

			Screen:
				name: 'screen3'
				canvas:
					Color:
						rgb: .99, .84, .0    
					Rectangle:
						size: self.size
						pos: self.pos				
				BoxLayout:
					orientation: 'vertical'
			        size_hint_x: 0.9
			        pos_hint: {'center_x': 0.5}

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		size_hint_y: 0.5
			        	BoxLayout:
			        		BoxLayout:
			        			Butt1:
			        				text:'back'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.stop(); screen_manager.transition = SlideTransition(direction="left");screen_manager.current = "screen1"		        		
			        		BoxLayout:
			        			size_hint_x: 1.4
			        		BoxLayout:
			        			Butt1:
			        				text:'restart'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.resetTimer()			        		
			        	BoxLayout:
			        	BoxLayout:
			        		Label:
			        			text:'Round: '+str(root.raund_index)
			        			font_size: min(self.height, self.width/2.5) / 2
			        			bold: True

			        BoxLayout:
			        	size_hint_y: 2
			        	Label:
			        		text:str(("%02d")%(root.timeRound//60))+':'+str(("%02d")%((root.timeRound% 60)))
			        		font_size: min(self.height, self.width/2.5) / 2
			        		bold: True
				        	canvas.before:
								Color:
									rgb: .95, .71, .0     
								Ellipse:
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10) 		        	
								
								Color:
									rgb: .99, .99, .0    
								Ellipse:
									angle_end: root.time360
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10) 
				        	
								Color:
									rgb: .99, .84, .0     
								Ellipse:
									size: (ellips_clock.size[1]-80,ellips_clock.size[1]-80)
									pos: (self.center_x-((ellips_clock.size[1]/2)-40), ellips_clock.pos[1]+40)											        	

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		orientation: 'vertical'
				        	BoxLayout:
				        		size_hint_y: 1
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(("%02d")%(root.timeRound_i//60))+':'+str(("%02d")%((root.timeRound_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'round'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:(("%02d")%(root.timePause_i//60))+':'+str(("%02d")%((root.timePause_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'pause'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(root.raund)
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'Rounds'

				        	BoxLayout:
				        		size_hint_y: 0.2
				        				
			        	BoxLayout:
			        		Butt1:
			        			size_hint_y: 1
			        			text:'Pause' if root.pause_index==False else 'Start'
			        			font_size: min(self.height, self.width/2.5) / 2.5
			        			on_release:root.pause()
			        			disabled: True if root.finish == True else False			        	
			        	BoxLayout:
			        		size_hint_y: 0.2

			Screen:
				name: 'screen4'
				canvas:
					Color:
						rgb: .84, .20, .24    
					Rectangle:
						size: self.size
						pos: self.pos				
				BoxLayout:
					orientation: 'vertical'
			        size_hint_x: 0.9
			        pos_hint: {'center_x': 0.5}

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		size_hint_y: 0.5
			        	BoxLayout:
			        		BoxLayout:
			        			Butt1:
			        				text:'back'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.stop(); screen_manager.transition = SlideTransition(direction="left");screen_manager.current = "screen1"		        		
			        		BoxLayout:
			        			size_hint_x: 1.4
			        		BoxLayout:
			        			Butt1:
			        				text:'restart'
			        				font_size: min(self.height, self.width/2.5) / 2.5
			        				on_release:root.resetTimer()			        		
			        	BoxLayout:
			        	BoxLayout:
			        		Label:
			        			text:'Round: '+str(root.raund_index) if root.timer_index == True else 'Prepare !!!'
			        			font_size: min(self.height, self.width/2.5) / 2
			        			bold: True

			        BoxLayout:
			        	id: ellips_clock
			        	size_hint_y: 2
			        	Label:
			        		text:str(("%02d")%(root.timePause//60))+':'+str(("%02d")%((root.timePause% 60))) if root.timer_index == True else str(("%02d")%(root.timer_ready//60))+':'+str(("%02d")%((root.timer_ready% 60)))
			        		font_size: min(self.height, self.width/2.5) / 2
			        		bold: True
				        	canvas.before:
								Color:
									rgb: .72, .16, .23     
								Ellipse:
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10) 		        	
								
								Color:
									rgb: .99, .26, .29    
								Ellipse:
									angle_end: root.time360
									size: (ellips_clock.size[1]-20,ellips_clock.size[1]-20)
									pos: (self.center_x-((ellips_clock.size[1]/2)-10), ellips_clock.pos[1]+10) 
				        	
								Color:
									rgb: .84, .20, .24    
								Ellipse:
									size: (ellips_clock.size[1]-80,ellips_clock.size[1]-80)
									pos: (self.center_x-((ellips_clock.size[1]/2)-40), ellips_clock.pos[1]+40)											        	

			        BoxLayout:
			        	orientation: 'vertical'
			        	BoxLayout:
			        		orientation: 'vertical'
				        	BoxLayout:
				        		size_hint_y: 1
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(("%02d")%(root.timeRound_i//60))+':'+str(("%02d")%((root.timeRound_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'round'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:(("%02d")%(root.timePause_i//60))+':'+str(("%02d")%((root.timePause_i% 60)))
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'pause'
				        		BoxLayout:
				        			orientation: 'vertical'
				        			BoxLayout:
				        				size_hint_y: 1.5
					        			Label:
					        				font_size: min(self.height, self.width/2) / 2
					        				text:str(root.raund)
					        				bold: True			        				
				        			BoxLayout:
				        				size_hint_y: 0.5
					        			Label:
					        				#font_size: min(self.height, self.width/2.5) / 2
					        				text:'Rounds'

				        	BoxLayout:
				        		size_hint_y: 0.2
				        				
			        	BoxLayout:
			        		Butt1:
			        			size_hint_y: 1
			        			text:'Pause' if root.pause_index==False else 'Start'
			        			font_size: min(self.height, self.width/2.5) / 2.5
			        			on_release:root.pause()
			        			disabled: True if root.timer_index == False else False			        	
			        	BoxLayout:
			        		size_hint_y: 0.2
""")



class BoxingTimer(BoxLayout):
	timeRound = NumericProperty(0)
	timeRound_i = NumericProperty(0)
	timePause = NumericProperty(0)
	timePause_i = NumericProperty(0)
	raund = NumericProperty(1)
	raund_index = NumericProperty(1)
	pause_index = BooleanProperty(False)
	time360 = NumericProperty(0.0)
	time360_step = NumericProperty(0.0)
	gong = SoundLoader.load('data/sound/gong.ogg')
	gong10 = SoundLoader.load('data/sound/gong10.ogg')
	gong10_3 = SoundLoader.load('data/sound/gong10_3.ogg')
	sound_start = SoundLoader.load('data/sound/start.ogg')
	timer_index = BooleanProperty(False)
	timer_ready = NumericProperty(10)
	finish = BooleanProperty(False)
	block_button = BooleanProperty(False)		

	def _timeRound(self, i):
		self.timeRound+=i

	def _timeRound_reset(self):
		self.timeRound=0	

	def _timePause(self, i):
		self.timePause+=i

	def _timePause_reset(self):
		self.timePause=0

	def _round_plus(self):
		self.raund+=1	

	def _round_minus(self):
		if self.raund>1: self.raund-=1	

	def start_timer_ready(self):
		self.timer_ready = 10
		self.ids.screen_manager.transition = SlideTransition(direction="left")
		self.ids.screen_manager.current = 'screen4'
		Clock.schedule_interval(self.tic_timer_ready, 1)
		self.sound_start.loop
		self.sound_start.play()

	def tic_timer_ready(self, dt):
		if self.timer_ready>0: 
			self.timer_ready-=1
			self.time360+=36

		else:
			Clock.unschedule(self.tic_timer_ready)
			self.sound_start.stop()
			self.ids.screen_manager.transition = SlideTransition(direction="left")
			self.ids.screen_manager.current = 'screen2'			
			self.startTimer()


	def start_timer(self):
		self.timer_index = False
		if self.timeRound>0:
			self.ids.screen_manager.transition = SlideTransition(direction="left")
			self.ids.screen_manager.current = 'screen4'
			self.newTimer()
			self.start_timer_ready()  
		else: 
			self.ids.screen_manager1.transition = SlideTransition(direction="up") 
			self.ids.screen_manager1.current = 'screen1'	

	def step(self, i):
		self.time360=0 
		self.time360_step=360/i

	def startTimer(self):
		self.timer_index = True
		self.gong.play()
		self.step(self.timeRound)
		Clock.schedule_interval(self.ticTimer, 1)

	def startPause(self):
		self.gong.play()
		self.step(self.timePause)
		self.ids.screen_manager.transition = SlideTransition(direction="left")
		self.ids.screen_manager.current = "screen4"
		Clock.schedule_interval(self.ticPause, 1)
				
	def ticTimer(self,dt):
		if self.timeRound>0:
			self.timeRound-=1
			if self.timeRound==10:
				self.gong10.play()
				self.ids.screen_manager.transition = FadeTransition()
				self.ids.screen_manager.current = "screen3"			
			self.time360+=self.time360_step	
		else:
			Clock.unschedule(self.ticTimer)
			self.next_round()

	def ticPause(self,dt):
		if self.timePause>0:			
			self.timePause-=1
			if self.timePause==10:
				self.gong10.play()			
			self.time360+=self.time360_step	
		else:
			Clock.unschedule(self.ticPause)
			self.timeRound=self.timeRound_i
			self.raund_Up()	

	def next_round(self):
		if self.raund_index<self.raund:
			self.timePause=self.timePause_i
			self.startPause()
		else:
			self.gong10_3.play()
			self.finish = True		

	def newTimer(self):
		self.timeRound_i=self.timeRound
		self.timePause_i=self.timePause
		self.raund_index=1

	def resetTimer(self):
		Clock.unschedule(self.ticTimer)
		Clock.unschedule(self.ticPause)
		Clock.unschedule(self.tic_timer_ready)
		self.timer_index = False
		self.sound_start.stop()		
		self.timeRound=self.timeRound_i
		self.timePause=self.timePause_i
		self.raund_index=1
		self.time360=0
		self.ids.screen_manager.transition = SlideTransition(direction="left")
		self.ids.screen_manager.current = "screen4"
		self.start_timer_ready()
		self.finish = False	

	def raund_Up(self):
		self.raund_index+=1
		self.startTimer()
		self.ids.screen_manager.transition = SlideTransition(direction="left")
		self.ids.screen_manager.current = "screen2"


	def pause(self):
		if self.pause_index==False:
			Clock.unschedule(self.ticTimer)
			Clock.unschedule(self.ticPause)
			self.pause_index=True
		else:
			if self.ids.screen_manager.current == "screen2" or self.ids.screen_manager.current == "screen3":Clock.schedule_interval(self.ticTimer, 1)
			if self.ids.screen_manager.current == "screen4":Clock.schedule_interval(self.ticPause, 1)	
			self.pause_index=False

	def stop(self):
		Clock.unschedule(self.ticTimer)
		Clock.unschedule(self.ticPause)
		Clock.unschedule(self.tic_timer_ready)
		self.sound_start.stop()
		self.gong10_3.stop()		
		self.timeRound=self.timeRound_i
		self.timePause=self.timePause_i
		self.raund_index=1
		self.time360=0
		self.finish = False

	def menu_screen(self, screen):
		try:
			self.block_button=True	
			self.ids.screen_manager1.transition = SlideTransition(direction="up")
			self.ids.screen_manager1.current = screen
		except:
			print('screen error')


class TimerApp(App):
    def build(self):
        app = BoxingTimer()
        return app

    def open_settings(self, *largs):
        pass

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    TimerApp().run()