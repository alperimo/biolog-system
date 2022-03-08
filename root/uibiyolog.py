import ui
import os
import player
import net
import app
import chat
import snd
import item
import event
import localegame
import time
import gameInfo
import uiToolTip
import uiCommon
import uiPickMoney
import systemSetting
import playerSettingModule

YOL = str(gameInfo.CONFIG_YOL)+"biyolog/"
			
class BiyologWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem = tooltipItem
		
		self.zaman = 0
		self.suanGOREV = 0
		self.gelecekButon = 0
		self.gelecekLevel = ""
		self.gorevTAMAM = 0
		self.levelYETERSIZ = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		gameInfo.BIYOLOG["ACIK"] = "1"
		self.biyologVERIAL()
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)
	
	def Close(self):
		gameInfo.BIYOLOG={}
		snd.PlaySound("sound/ui/click.wav")
		self.Hide()
		
	def biyologVERIAL(self):
		gameInfo.PYTHONISLEM = "biyolog_verial#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/biyologwindow.py")
			
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			
			self.Animage = self.GetChild("Animage")
			
			self.GetChild("board").Show()
			
			self.zaman = app.GetTime()
			
			self.butonlar = {
			
				"30" : self.GetChild("gorev30Button"),
				"40" : self.GetChild("gorev40Button"),
				"50" : self.GetChild("gorev50Button"),
				"60" : self.GetChild("gorev60Button"),
				"70" : self.GetChild("gorev70Button"),
				"80" : self.GetChild("gorev80Button"),
				"85" : self.GetChild("gorev85Button"),
				"90" : self.GetChild("gorev90Button"),
				"92" : self.GetChild("gorev92Button"),
				"94" : self.GetChild("gorev94Button"),
				
				"baslat" : self.GetChild("gorevBaslat"),
				"teslimet" : self.GetChild("gorevTeslimEt"),
				
			}
			
			self.butonlar["baslat"].Hide()
			self.butonlar["teslimet"].Hide()
			self.GetChild("item1Tamamlandi").Hide()
			self.GetChild("item2Tamamlandi").Hide()
			
			for (level, buton) in self.butonlar.items():
				buton.SetEvent(lambda gelen=level: self.biyologGELECEK(gelen))
				
			self.GetChild("GorevVereceginItem1").SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowToolTips1)
			self.GetChild("GorevVereceginItem1").SAFE_SetStringEvent("MOUSE_OVER_OUT", self.HideToolTips)
			self.GetChild("GorevVereceginItem2").SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowToolTips2)
			self.GetChild("GorevVereceginItem2").SAFE_SetStringEvent("MOUSE_OVER_OUT", self.HideToolTips)
			self.GetChild("GorevKazancItem1").SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowToolTips3)
			self.GetChild("GorevKazancItem1").SAFE_SetStringEvent("MOUSE_OVER_OUT", self.HideToolTips)
						
		except:
			import exception
			exception.Abort("BiyologWindow.LoadWindow.LoadObject")
			
	def ShowToolTips1(self): self.itemID(1)	
	def ShowToolTips2(self): self.itemID(2)	
	def ShowToolTips3(self): self.itemID(3)
	def HideToolTips(self): self.tooltipItem.Hide()
		
	def itemID(self,yer):
		bol = gameInfo.BIYOLOG["INFOS"].split("#")
		if self.suanGOREV == 0:
			bol = gameInfo.BIYOLOG["INFOS_GELECEK_"+str(self.gelecekLevel)].split("#")
			
		if yer == 1:
			self.itemGOSTER(int(bol[7]))
		elif yer == 2:
			self.itemGOSTER(int(bol[8]))
		elif yer == 3:
			self.itemGOSTER(int(bol[9]))
		
	def itemGOSTER(self,kod):
		itemkodu = kod
		self.tooltipItem.ClearToolTip()
		metinSlot = [player.GetItemMetinSocket(itemkodu, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(itemkodu, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		self.tooltipItem.AddRefineItemData(itemkodu, metinSlot, attrSlot)
		self.tooltipItem.AppendSpace(3)
	
	def biyologGELECEK(self,gelen):
		bol = gameInfo.BIYOLOG["INFOS"].split("#")
		
		if gelen == "baslat":
			gameInfo.PYTHONISLEM = "biyolog_baslat#"+str(bol[1])
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			return
		if gelen == "teslimet":
			if bol[1] == "92" or bol[1] == "94":
				self.ozellikSecQuestionDialog = uiCommon.QuestionDialogGame()
				self.ozellikSecQuestionDialog.SetText("Hangi özelliði almak istiyorsun?")
				self.ozellikSecQuestionDialog.EscapeKeyStat(1)
				self.ozellikSecQuestionDialog.SetAcceptText(bol[10])
				self.ozellikSecQuestionDialog.SetOrtaText(bol[11])
				self.ozellikSecQuestionDialog.SetCancelText(bol[12])
				self.ozellikSecQuestionDialog.SetAcceptEvent(lambda sec=1:self.ozellikSEC(bol[1],sec))
				self.ozellikSecQuestionDialog.SetOrtaEvent(lambda sec=2:self.ozellikSEC(bol[1],sec))
				self.ozellikSecQuestionDialog.SetCancelEvent(lambda sec=3:self.ozellikSEC(bol[1],sec))
				self.ozellikSecQuestionDialog.Open()
				return
			
			gameInfo.PYTHONISLEM = "biyolog_teslimet#"+str(bol[1])+"#0"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			return
		
		if gelen != bol[1]:
			self.gelecekButon = 1
			self.gelecekLevel = str(gelen)
			if "INFOS_GELECEK_"+str(gelen) in gameInfo.BIYOLOG.keys():
				self.biyologSAYFA(1)
				return
			
			gameInfo.PYTHONISLEM = "biyolog_verial_gelecek#"+str(gelen)
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		else:
			self.biyologSAYFA()
			
	def ozellikSEC(self,gelen,gelen2):
		gameInfo.PYTHONISLEM = "biyolog_teslimet#"+str(gelen)+"#"+str(gelen2)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		self.ozellikSecQuestionDialog.Close()
			
	def biyologSAYFA(self,gelen=0):
		if gelen == 1:
			self.gelecekButon = 0
			self.suanGOREV = 0
			self.gorevTAMAM = 0
			#bol = gameInfo.BIYOLOG["INFOS_GELECEK_"].split("#")
			self.biyologDEGISTIR(self.gelecekLevel)
			return
			
		self.levelYETERSIZ = 0
		self.suanGOREV = 1
		self.gelecekButon = 0
		self.gorevTAMAM = 0
		bol = gameInfo.BIYOLOG["INFOS"].split("#")
		for (level, buton) in self.butonlar.items():
			if level == bol[1]:
				buton.SetUpVisual(YOL+"varolan.tga")
				buton.SetOverVisual(YOL+"varolan1.tga")
				buton.SetDownVisual(YOL+"varolan2.tga")
				
				if bol[2] == "0":
					self.butonlar["baslat"].Show()
					self.butonlar["baslat"].Enable()
					self.butonlar["teslimet"].Hide()
					self.butonlar["teslimet"].Disable()
				else:
					self.butonlar["teslimet"].Show()
					self.butonlar["teslimet"].Enable()
					self.butonlar["baslat"].Hide()
					self.butonlar["baslat"].Disable()
				
				if int(player.GetStatus(player.LEVEL)) < int(bol[1]):
					self.levelYETERSIZ = 1
				
				self.biyologDEGISTIR(level)
			else:
				if level == "baslat" or level == "teslimet":
					continue
				buton.SetUpVisual(YOL+"gelecek.tga")
				buton.SetOverVisual(YOL+"gelecek1.tga")
				buton.SetDownVisual(YOL+"gelecek2.tga")
				
			if level < bol[1]:
				buton.SetUpVisual(YOL+"bitmis.tga")
				buton.SetOverVisual(YOL+"bitmis1.tga")
				buton.SetDownVisual(YOL+"bitmis2.tga")
				
	def biyologDEGISTIR(self,gelen):
		bol = gameInfo.BIYOLOG["INFOS"].split("#")
		if gelen != bol[1]:
			bol = gameInfo.BIYOLOG["INFOS_GELECEK_"+str(gelen)].split("#")
		else:
			self.butonlar["baslat"].SetUp()
			self.butonlar["teslimet"].SetUp()
		
		self.GetChild("item1Tamamlandi").Hide()
		self.GetChild("item2Tamamlandi").Hide()
		
		self.GetChild("gorevAdi").SetText(bol[5])
		kalanITEM = ""
		
		if self.suanGOREV == 1:
			if bol[1] == "92":
				if int(bol[4]) <= 0:
					kalanITEM = "0"
					self.butonlar["teslimet"].SetUp()
					self.GetChild("item1Tamamlandi").Show()
				else:
					kalanITEM = bol[4]
					self.gorevTAMAM = 1
			else:
				if int(bol[4].split("x")[0]) <= 0:
					kalanITEM = "0"
					self.GetChild("item1Tamamlandi").Show()
				else:
					kalanITEM = bol[4].split("x")[0]
					
				if int(bol[4].split("x")[1]) <= 0:
					kalanITEM += "x0"
					self.GetChild("item2Tamamlandi").Show()
				else:
					kalanITEM += "x"+bol[4].split("x")[1]
					
				if kalanITEM == "0x0":
					self.butonlar["teslimet"].SetUp()
				else:
					self.gorevTAMAM = 1		
		else:
			kalanITEM = bol[4]
			
		self.GetChild("gorevVerdigin").SetText(bol[3])
		self.GetChild("gorevKalan").SetText(kalanITEM)
		self.GetChild("gorevGelecek").SetText(bol[6])
		self.GetChild("GorevVereceginItem1").Show()
		self.GetChild("GorevVereceginItem2").Show()
		self.GetChild("GorevKazancItem1").Show()
		if bol[7] != "...":
			item.SelectItem(int(bol[7]))
			self.GetChild("GorevVereceginItem1").LoadImage(str(item.GetIconImageFileName()))
		if bol[8] != "...":
			item.SelectItem(int(bol[8]))
			self.GetChild("GorevVereceginItem2").LoadImage(str(item.GetIconImageFileName()))
		else:
			self.GetChild("GorevVereceginItem2").Hide()
		if bol[9] != "...":
			item.SelectItem(int(bol[9]))
			self.GetChild("GorevKazancItem1").LoadImage(str(item.GetIconImageFileName()))
		else:
			self.GetChild("GorevKazancItem1").Hide()
		self.GetChild("gorevKazanc1").SetText(bol[10])
		self.GetChild("gorevKazanc2").SetText(bol[11])
		self.GetChild("gorevKazanc3").SetText(bol[12])
	
	def OnUpdate(self):
		if app.GetTime() >= self.zaman + 2:
			self.Animage.Hide()
			self.zaman = 0
			
		if "YENILE" in gameInfo.BIYOLOG.keys() and gameInfo.BIYOLOG["YENILE"] == "1":
			self.biyologSAYFA(self.gelecekButon)
			del gameInfo.BIYOLOG["YENILE"]
			
		if "ACIK" in gameInfo.BIYOLOG.keys() and gameInfo.BIYOLOG["ACIK"] == "2":
			self.Close()
			
		if self.suanGOREV == 0 or self.levelYETERSIZ == 1:
			self.butonlar["baslat"].Down()
			self.butonlar["baslat"].Disable()
			self.butonlar["teslimet"].Down()
			self.butonlar["teslimet"].Disable()
			self.butonlar["baslat"].Show()
			self.butonlar["teslimet"].Hide()
			
		if self.gorevTAMAM == 1:
			self.butonlar["teslimet"].Down()
			self.butonlar["teslimet"].Disable()
			
		if "ITEMTOPLANDI" in gameInfo.BIYOLOG.keys():
			self.biyologSAYFA()
			del gameInfo.BIYOLOG["ITEMTOPLANDI"]
			
	def OnPressEscapeKey(self):
		if self.zaman == 0:
			self.Close()
			return TRUE	

class Bug_Fatihbab34(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
