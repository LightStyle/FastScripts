# -*- coding: utf-8 -*-
#!/usr/bin/python
# -------------------------------------------------------------------------
# Index File
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

# Core Modules
import hashlib
import os
from flask import Flask, render_template, request, session, response

app = Flask(__name__)

# ----- Index ------
@app.route("/")
def index():
	def scriptList(l):
		i = []
		ignList = ['__init__', 'utils']
		for e in l:
			s = e.split('.')[0]
			if not (s in i) and not (s in ignList):
				i.append(s)
		return i

	gen_list = os.listdir('modules')
	gen_parsed_list = scriptList(gen_list)
	show_box = False
	return render_template('index.html', gen_parsed_list=gen_parsed_list)

# ----- Generatori ------
@app.route("/generator/<gen_name>", methods=['GET', 'POST'])
def generatore(gen_name):
	gen_name = gen_name.lower()
	gen_list = os.listdir('modules')

	if (gen_name + '.py') in gen_list:
		gen_load = __import__('modules.'+gen_name, globals(), locals(), ['generator'], -1)
		gen = gen_load.generator()

		output = gen.output()

		nick = cookie('nick') or param('nick')
		forum = cookie('nick') or param('forum')
		show_box = True
		if nick or forum:
			show_box = False

		html = render_template('modules/'+gen_name+'.html', output=output, show_box=show_box)
		return html

# ----- Feedback ------

#@app.route("/feedback", methods="['GET','POST']")
#def feedback():
#	response.set_cookie
# ----- Funzioni esterne ------

def hash(s):
	string = hashlib.sha224(s).hexdigest()
	string = hashlib.sha224(string[::-1]).hexdigest()
	return string

def param(name):
	try:
		p = request.args[name]
	except:
		p = ''
	return p

def cookie(name):
	try:
		c = request.cookies[name]
	except:
		c = ''
	return c

# -------------------------------------------------------------------------

app.secret_key = hash(__name__)
if __name__ == "__main__":
	app.debug = True
	app.run()
	# app.run('0.0.0.0')
