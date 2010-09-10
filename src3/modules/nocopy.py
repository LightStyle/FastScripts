#! -*- coding: utf-8 -*-
from flask import request
class generator:
	__script = ''
	__check = ''

	__alert = ''
	__select = 1
	
	def __init__(self):
		try:
			self.__select = int(request.args['nocopy_select'])
		except:
			pass
			
		try:
			self.__check = str(request.args['check'])
		except:
			pass
			
		try:
			self.__alert = str(request.args['nocopy_message'])
		except:
			pass

		if len(self.__check) > 0:
			self.__script = self.__load()
		
	def __load(self):
		if self.__select == 1:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
var tdmessaggio="%s";
// Autore dello script: Maximus (maximus@nsimail.com) w/ By DynamicDrive.com
// http://www.dynamicdrive.com/dynamicindex9/noright.htm
// Funzione che disabilita il tasto destro su Internet Explorer
function clickIE4(){ if(event.button==2){ if(tdmessaggio!= '') alert(tdmessaggio); return false; } }
// Funzione che disabilita il tasto destro su Netscape e FireFox
function clickNS4(e){
if (document.layers||document.getElementById&&!document.all){ if (e.which==2||e.which==3){ if(tdmessaggio!= '') alert(tdmessage); return false; } }
}
// Controlli per la selezione del browser
if (document.layers){ document.captureEvents(Event.MOUSEDOWN); document.onmousedown=clickNS4; }
else if (document.all&&!document.getElementById){ document.onmousedown=clickIE4; }
document.oncontextmenu=function(){ if(tdmessaggio!= '') alert(tdmessaggio); return false;};
</script>''' % self.__alert
		elif self.__select == 2:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
document.oncontextmenu=document.onselectstart=document.ondragstart=function() {return false;};
</script>'''
		elif self.__select == 3:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
var tdmessaggio = "%s";
document.oncontextmenu=function(){ alert(tdmessaggio + "\nAdesso apparira il menu'"); return true; }
</script>''' % self.__alert
		else:
			return 'ERROR'

	def output(self):
		return self.__script
