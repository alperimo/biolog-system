import gameInfo
import systemSetting
import uiBiyolog

class GameButtonWindow(ui.ScriptWindow):
	
			self.gameButtonDict={
				
				"BIOLOG" : self.GetChild("BiyologButton"),
			}

			self.gameButtonDict["BIOLOG"].SetEvent(ui.__mem_func__(self.__OnClickBiyologGOSTER))

	def __OnClickBiyologGOSTER(self):
		if "ACIK" in gameInfo.BIYOLOG.keys():
			gameInfo.BIYOLOG["ACIK"] = "2"
			return
		self.ac = uiBiyolog.BiyologWindow()
		self.ac.Show()

	def CheckGameButton(self):

		biologButton=self.gameButtonDict["BIOLOG"]
		
		#degistir#
		if self.__IsSkillStat():
			skillPlusButton.Show()
			self.biyologPOS(systemSetting.GetWidth()-50-32, systemSetting.GetHeight()-170)
		else:
			skillPlusButton.Hide()
			self.biyologPOS(systemSetting.GetWidth()-50-32, systemSetting.GetHeight()-100)
			
		#ekle#
		if gameInfo.BIOLOG_SISTEMI == 1:
			biologButton.Hide()
		else:
			if gameInfo.BIYOLOG_DURUM == 1:
				biologButton.Show()
			else:
				biologButton.Hide()
			
	def biyologPOS(self, x, y):
		self.gameButtonDict["BIOLOG"].SetPosition(x,y)

	def OnUpdate(self):
	
		if gameInfo.BIYOLOG_DURUM == 0:
			self.gameButtonDict["BIOLOG"].Hide()
