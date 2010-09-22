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
class generator:
	__script = {}
	__check = 0

	__alert = ''
	__isText = 1
	__isToProfile = 1
	__input = ''
	__inputPart = ''
	__text = ''
	__userCode = '1'

	# Variabili di servizio
	__action = '' # form | code | error
	__page = 0 # numero pagina (form), qui non utilizzato
	__error = {}

	def __init__(self):
		try:
			self.__check = int(request.values['check'])
		except:
			pass
		try:
			self.__isText = int(request.values['profilecode_isText'])
		except:
			pass
		try:
			self.__isToProfile = int(request.values['profilecode_isToProfile'])
		except:
			pass
		try:
			self.__text = str(request.values['profilecode_text'])
		except:
			pass
		try:
			self.__alert = str(request.values['profilecode_alert'])
		except:
			pass
		
		if self.__isText:
			self.__inputPart = 'type="submit" value="%s" class="forminput"' % self.__text
		else:
			self.__inputPart = 'type="image" src="%s" style="border: 0;"' % self.__text
		self.__input = '''<input %s onclick="alert('Grazie del supporto! Ricordati di registrare le modifiche una volta aperta la pagina del tuo profilo personale!')">''' % self.__inputPart
		self.__userCode = self.__isToProfile and '1' or '22'

		if self.__check == 1:
			if self.__text == '':
				self.__action = 'error'
				if self.__isText:
					self.__error = errors.error('001', 'Non hai specificato un testo per il bottone')
				else:
					self.__error = errors.error('001', "Non hai specificato il link dell'immagine")
			elif not (self.__isText and errors.urlMatch(self.__text)):
				self.__action = 'error'
				self.__error = errors.error('002', "Il link dell'immagine deve iniziare con http:// e finire con un'estensione valida")
			elif self.__alert == '':
				self.__action = 'error'
				self.__error = errors.error('001', 'Devi specificare un codice da aggiungere!')
			else:
				self.__action = 'code'
				self.__script = self.__load()
		else:
			self.__action = 'form'

	def __load(self):
		s1 = '''<!-- Generato con il FFMag FastScripts - Script by Bowser -->
<form action="/" name="insert" method="get">
<input type="hidden" name="act" value="UserCP">
<input type="hidden" name="CODE" value="%s">
<input type="hidden" name="insertcode" value="1">
%s
</form>
<br><small>Ideato da Bowser (c) <a href="http://ffmagazine.forumfree.it/">ForumFree Magazine</a></small>''' % (self.__isToProfile, self.__input)
		s2 = '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
var code="%s";
if(location.search.indexOf('act=UserCP')!=-1 && location.search.indexOf('CODE=%s')!=-1 && location.search.indexOf('insertcode=1')!=-1 ){
if( document.REPLIER.Post.value.indexOf(code)==-1 ) document.REPLIER.Post.value = code}
</script>''' % (self.__alert, self.__userCode)
		s = {'s1': s1, 's2': s2}
		return s

	def output(self):
		i = {}
		i['action'] = self.__action
		i['code'] = self.__script
		i['page'] = self.__page
		if self.__error:
			i['error'] = self.__error
		return i