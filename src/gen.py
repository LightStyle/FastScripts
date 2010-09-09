def nocopy(type, alert = ""):
    type = str(type)
    if type == "1":
        script = '''<script type="text/javascript"> \
//Generato con il FFMag FastScripts - Script by Bowser \
var tdmessaggio="%s"; \
// Autore dello script: Maximus (maximus@nsimail.com) w/ By DynamicDrive.com \
// http://www.dynamicdrive.com/dynamicindex9/noright.htm \
// Funzione che disabilita il tasto destro su Internet Explorer \
function clickIE4(){ if(event.button==2){ if(tdmessaggio!= '') alert(tdmessaggio); return false; } } \
// Funzione che disabilita il tasto destro su Netscape e FireFox \
function clickNS4(e){ \
if (document.layers||document.getElementById&&!document.all){ if (e.which==2||e.which==3){ if(tdmessaggio!= '') alert(tdmessage); return false; } } \
} \
// Controlli per la selezione del browser \
if (document.layers){ document.captureEvents(Event.MOUSEDOWN); document.onmousedown=clickNS4; } \
else if (document.all&&!document.getElementById){ document.onmousedown=clickIE4; } \
document.oncontextmenu=function(){ if(tdmessaggio!= '') alert(tdmessaggio); return false;}; \
</script>''' % alert
    elif type == "2":
        script = '''<script type="text/javascript"> \
//Generato con il FFMag FastScripts - Script by Bowser \
document.oncontextmenu=document.onselectstart=document.ondragstart=function() {return false;}; \
</script>'''
    else:
        script = '''<script type="text/javascript"> \
//Generato con il FFMag FastScripts - Script by Bowser \
var tdmessaggio = "%s"; \
document.oncontextmenu=function(){ alert(tdmessaggio + "\nAdesso apparira' il menu'"); return true; } \
</script>''' % alert
    return script