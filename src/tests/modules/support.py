# -*- coding: utf-8 -*-
#!/usr/bin/python
# -------------------------------------------------------------------------
# Modulo: Scripts Anti Copiatura
# Guida associata: http://ffmagazine.forumfree.it/?t=36582013
# -------------------------------------------------------------------------
# ForumFree Magazine Fast Scripts Generator
# Ultimo aggiornamento: 10/09/2010 20:48 - v0.1alpha
# Copyright (C) 2010 ForumFree Magazine http://ffmagazine.forumfree.it
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
from flask import request, jsonify
class generator:
	__script = ''
	__check = 0

	__alert = ''
	__isText = 1
	__id = '0'
	__inputText = ''
	__inputImage = ''
	__json = False
	__json_dict = {}

	# Variabili di servizio
	__action = '' # form | code
	__page = 0 # numero pagina (form), qui non utilizzato
	__error = {}

	def __init__(self):
		try:
			self.__check = int(request.values['check'])
		except:
			pass
		try:
			self.__isText = int(request.values['support_isText'])
		except:
			pass
		try:
			self.__alert = str(request.values['support_text'])
		except:
			pass
		try:
			self.__id = str(request.values['support_id'])
		except:
			pass
		try:
			self.__json = str(request.values['json'])
		except:
			pass
		
			
		self.__inputText = self.__isText and '<input type="submit" value="%s" class="forminput">\n' % self.__alert or ''
		self.__inputImage = (not int(self.__isText)) and '<input type="image" src="%s" style="border: 0;">\n' % self.__alert or ''

		if self.__check == 1:
			if self.__alert == '':
				self.__action = 'error'
				self.__error = errors.error('001', 'Devi inserire un testo per il bottone')
			if self.__id == '':
				self.__action = 'error'
				self.__error = errors.error('001', "Devi inserire un ID")
			if not self.__id.isdigit():
				self.__action = 'error'
				self.__error = errors.error('002', "L'ID deve essere un numero!")
			if not self.__error:
				if self.__json:
					self.__action = 'json'
					self.__json_dict['script'] = self.__load()
					self.__json_dict['error'] = self.__error
				else:
					self.__action = 'code'
					self.__script = self.__load()
		else:
			self.__action = 'form'
		
	def __load(self):
		return '''<!-- Generato con il FFMagazine FastScripts - Script by Delta & Bowser -->
<form action="http://supporto.forumfree.it/" method="post" name="REPLIER">
<input type="hidden" name="st" value="0">
<input type="hidden" name="act" value="Post">
<input type="hidden" name="f" value="26622">
<input type="hidden" name="CODE" value="03">
<input type="hidden" name="t" value="%s">
%s<input type="hidden" name="Post" value="Up!">
%s</form><br>
<small>Ideato da Delta & Bowser (c) <a href="http://ffmagazine.forumfree.it/">ForumFree Magazine</a></small>''' % (self.__id, self.__inputImage, self.__inputText)

	def output(self):
		i = {}
		i['action'] = self.__action
		i['code'] = self.__script
		i['page'] = self.__page
		i['error'] = self.__error
		i['json'] = jsonify(self.__json_dict)

		return i