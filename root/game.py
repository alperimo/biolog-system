import gameInfo
import event
import net
import localegame

	def __ServerCommand_Build(self):
		serverCommandList={
			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##
		}

	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)


	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)

	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0

		elif LuaToPython.find("biyolog_open#") != -1:
			#gameInfo.BIYOLOG["DURUM"] = "1"
			gameInfo.BIYOLOG_DURUM = 1
		elif LuaToPython.find("biyolog_verileri|#") != -1:
			gelen = LuaToPython.split("|")[1].replace("_"," ")
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(gelen))
			gameInfo.BIYOLOG["INFOS"] = str(gelen)
			gameInfo.BIYOLOG["YENILE"] = "1"
		elif LuaToPython.find("biyolog_verileri_gelecek|#") != -1:
			gelen = LuaToPython.split("|")[1].replace("_"," ")
			if str(gelen.split("#")[15]) == "1":
				gameInfo.BIYOLOG["INFOS"] = str(gelen)
			else:
				gameInfo.BIYOLOG["INFOS_GELECEK_"+str(gelen.split("#")[1])] = str(gelen)
			gameInfo.BIYOLOG["YENILE"] = "1"
		elif LuaToPython.find("biyolog_itemtoplandi#") != -1:
			bol = LuaToPython.split("#")
			if "ACIK" in gameInfo.BIYOLOG.keys() and gameInfo.BIYOLOG["ACIK"] == "1":
				gameInfo.BIYOLOG["ITEMTOPLANDI"] = bol[1]
		elif LuaToPython.find("biyolog_kapat#") != -1:
			if "ACIK" in gameInfo.BIYOLOG.keys() and gameInfo.BIYOLOG["ACIK"] == "1":
				gameInfo.BIYOLOG["ACIK"] = "2"
				
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Biyolog>: Tebrikler! tüm biyolog görevlerini baþarýyla tamamladýnýz.")
				
			gameInfo.BIYOLOG_DURUM = 0