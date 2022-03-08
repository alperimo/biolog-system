import gameInfo

class QuestionDialogGame(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.EscapeStat = 0
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialoggame.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.ortaButton = self.GetChild("orta")
		self.cancelButton = self.GetChild("cancel")
		self.kapatButton = self.GetChild("kapat")
		
		self.kapatButton.SetEvent(self.Close)

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)
		
	def SAFE_SetOrtaEvent(self, event):
		self.ortaButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		
	def SetOrtaEvent(self, event):
		self.ortaButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)
		
	def SetOrtaText(self, text):
		self.ortaButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def EscapeKeyStat(self, gelen):
		self.EscapeStat = gelen
	
	def OnPressEscapeKey(self):
		if self.EscapeStat == 1:
			return TRUE
		self.Close()
		return TRUE