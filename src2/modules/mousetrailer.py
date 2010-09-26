# -*- coding: utf-8 -*-
#!/usr/bin/python
# -------------------------------------------------------------------------
# Modulo: Scripts Anti Copiatura
# Guida associata: http://ffmagazine.forumfree.it/?t=36582013
# -------------------------------------------------------------------------
# ForumFree Magazine Fast Scripts Generator
# Ultimo aggiornamento: 10/09/2010 20:48 - v0.1alpha
# Copyright (C) 2010 ForumFree Magazine http://ffmagazine.forumfree.it/
#
# Sviluppatori:
# Niccolo` "Kurono" Campolungo <damnednickix@hotmail.it>
# Antonio Micari <darkstyle96@gmail.com>
# Damiano Faraone (aka Bowser) <bowser@ffmagazine.net>
# -------------------------------------------------------------------------
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
# -------------------------------------------------------------------------
import utils.errors as errors
from flask import request
from textwrap import wrap
class generator:
	__script = ''
	__check = 0
	__array = ''

	__text = ''
	__speed = ''
	__speedPers = ''
	__distance = ''
	__color = ''
	__size = ''
	__sizeType = ''
	__isBold = 1
	__isItalic = 0
	__isBlink = 0

	__bold = ''
	__italic = ''
	__blink = ''

	# Variabili di servizio
	__action = ''
	__page = 0
	__error = {}

	def __init__(self):
		try:
			self.__check = int(request.values['check'])
		except:
			pass
		try:
			self.__text = str(request.values['mousetrailer_text'])
		except:
			pass
		try:
			self.__speed = str(request.values['mousetrailer_speed'])
		except:
			pass
		try:
			self.__speedPers = str(request.values['mousetrailer_speedPers'])
		except:
			pass
		try:
			self.__distance = str(request.values['mousetrailer_distance'])
		except:
			pass
		try:
			self.__color = str(request.values['mousetrailer_color'])
		except:
			pass
		try:
			self.__size = str(request.values['mousetrailer_size'])
		except:
			pass
		try:
			self.__sizeType = str(request.values['mousetrailer_sizeType'])
		except:
			pass
		try:
			self.__isBold = int(request.values['mousetrailer_isBold'])
		except:
			pass
		try:
			self.__isItalic = int(request.values['mousetrailer_isItalic'])
		except:
			pass
		try:
			self.__isBlink = int(request.values['mousetrailer_isBlink'])
		except:
			pass
			
		if self.__isBold:
			self.__bold = 'font-weight: bold; '
		if self.__isItalic:
			self.__italic = 'font-style: italic; '
		if self.__isBlink:
			self.__blink = 'text-decoration: blink; '
		if self.__color:
			self.__color = 'color: %s; ' % self.__color
		else:
			self.__color = ''
		if self.__size:
			self.__size = 'font-size: %s%s; ' % (self.__size, self.__sizeType)
		else:
			self.__size = ''
		if not self.__speed:
			self.__speed = 'medium'
		if self.__speed == 'pers':
			self.__speed = self.__speedPers
		
		self.__array = str(wrap(self.__text, 1))
		self.__array = self.__array.replace('[', 'new Array(')
		self.__array = self.__array.replace(']', ')')
		self.__styles = '%s%s%s%s%s' % (self.__size, self.__color, self.__bold, self.__italic, self.__blink)


		if self.__check == 1:
			if self.__text == '':
				self.__action = 'error'
				self.__error = errors.error('001', 'Devi inserire un messaggio valido!')
			elif not self.__distance.isdigit():
				self.__action = 'error'
				self.__error = errors.error('002', 'La distanza deve essere un numero!')
			elif self.__size and not self.__size.isdigit():
				self.__action = 'error'
				self.__error = errors.error('002', 'La dimensione deve essere un numero')
			elif (self.__speed == 'pers') and (not self.__speedPers.isdigit()):
				self.__action = 'error'
				self.__error = errors.error('001', "La velocita' deve essere espressa sotto forma di numero")
			else:
				self.__action = 'code'
				self.__script = self.__load()
		else:
			self.__action = 'form'
	def __load(self):
		a = '''<style>.spanstyle &#91;position: absolute; visibility: visible; top: -50px; left: 0; font-family: "segoe ui", Verdana, Arial; z-index: 9999; {0}&#92;</style>
<script type="text/javascript">
/*
Cursor Trailer Text- By Peter Gehrig (http://www.24fun.ch/)
Thanks to Dynamic Drive: http://www.dynamicdrive.com/dynamicindex13/trailortext.htm
***************************************************************************************************
Edited by DarkStyle / Modificato da DarkStyle
Made compatible with Forumfree by DarkStyle / Reso compatibile con Forumfree da DarkStyle
Made compatible with gecko browsers (Mozilla, Opera, ...) by DarkStyle / Reso compatibile con i browsers gecko (Mozilla, Opera, ...) da DarkStyle
(C) 2009 http://ffmagazine.forumfree.net
*/
var x,y; var flag = 0;
var trailerSpeed = '{1}'; //'slow', 'medium', 'fast' o valore numerico - Velocita' del fade
var trailerMessage = {2};
var offPos = {3}; //Distanza dal cursore
switch(trailerSpeed) &#91;case 'medium':trailerSpeed=30;break; case 'slow':trailerSpeed=50;break; case 'fast':trailerSpeed=10;break;&#92; var ind = new function() &#91;this.i = 0;&#92;; var xpos = new Array(); for (i = 0; i < trailerMessage.length; i++) &#91;ind.i = i; xpos[ind.i] = -50;&#92; var ypos = new Array(); for (i = 0; i < trailerMessage.length; i++) &#91;ind.i = i; ypos[ind.i] = -50;&#92;var IE = document.all ? true : false; if (!IE) document.captureEvents(Event.MOUSEMOVE); document.onmousemove = function(e) &#91; if (IE) &#91;x = event.clientX + document.body.scrollLeft; y = event.clientY + document.body.scrollTop;&#92; else &#91;x = e.pageX; y = e.pageY;&#92; x = x < 0 ? 0 : x; y = y < 0 ? 0 : y; flag = 1;&#92;; function makesnake() &#91;if (flag == 1 && IE) &#91;for (i = trailerMessage.length-1; i >= 1; i--) &#91;ind.i = i; xpos[ind.i] = xpos[ind.i - 1] + offPos; ypos[ind.i] = ypos[ind.i - 1];&#92; xpos[0] = x + offPos; ypos[0] = y + offPos; for (i = 0; i < trailerMessage.length; i++) &#91;ind.i = i; var thisspan = document.getElementById('span' + ind.i).style; thisspan.posLeft = xpos[ind.i]; thisspan.posTop = ypos[ind.i];&#92;&#92; else if (flag == 1 && !IE) &#91;for (i = (trailerMessage.length - 1); i >= 1; i--) &#91;ind.i = i; xpos[ind.i] = xpos[ind.i - 1] + offPos; ypos[ind.i] = ypos[ind.i - 1];&#92; xpos[0] = x + offPos; ypos[0] = y + offPos; for (i = 0; i < trailerMessage.length; i++) &#91;ind.i = i; var thisspan = document.getElementById('span' + ind.i); thisspan.style.left = xpos[ind.i]; thisspan.style.top = ypos[ind.i];&#92;&#92; var timer = setTimeout("makesnake()", trailerSpeed);&#92;for (i=0;i<=trailerMessage.length-1;i++) &#91;ind.i = i; trailerMessage[ind.i] = trailerMessage[ind.i] == ' ' ? ' ' : trailerMessage[ind.i]; document.write('<span id="span' + ind.i + '" class="spanstyle">' + trailerMessage[ind.i] + '</span>');&#92; window.onload = makesnake(); var body = document.body ? document.body : (document.activeElement ? document.activeElement : 0); if(body) &#91;body.style.overflowX = 'hidden'; body.style.overflowY = 'auto'; body.style.minHeight = 0; body.style.width = '100';&#92;
</script>'''.format(self.__styles,
					self.__speed,
					self.__array,
					self.__distance)
		a = a.replace('&#91;','{')
		a = a.replace('&#92;','}')
		return a

	def output(self):
		i = {}
		i['action'] = self.__action
		i['code'] = self.__script
		i['page'] = self.__page
		if self.__error:
			i['error'] = self.__error
		return i