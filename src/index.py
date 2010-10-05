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
import datetime
import hashlib
import os
import pymongo
from flask import Flask, render_template, request, current_app, jsonify

app = Flask(__name__)

# ----- Index ------
@app.route("/", methods=['GET', 'POST'])
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
	statsbox = statsbox_init(cookie('statsbox'), param('submit'), param('nick'), param('forum')) # Inizializzamento Box Inserimento Dati
	
	html = render_template('index.html', statsbox=statsbox, gen_parsed_list=gen_parsed_list) # Render Template
	
	# ----- Cookie Box Inserimento Dati ------
	response = current_app.make_response(html)
	statsbox_cookie(response, param('submit'), param('nick'), param('forum'))

	return response

# ----- Generatori ------
@app.route("/generator/<gen_name>", methods=['GET', 'POST'])
def generatore(gen_name):
	gen_name = gen_name.lower()
	gen_list = os.listdir('modules')

	if (gen_name + '.py') in gen_list:
		gen_load = __import__('modules.'+gen_name, globals(), locals(), ['generator'], -1)
		gen = gen_load.generator()

		output = gen.output()
		
		statsbox = statsbox_init(cookie('statsbox'), param('submit'), param('nick'), param('forum')) # Inizializzamento Box Inserimento Dati
		
		html = render_template('modules/'+gen_name+'.html', statsbox=statsbox, output=output) # Render Template
		
		# ----- Cookie Box Inserimento Dati ------
		response = current_app.make_response(html)
		statsbox_cookie(response, param('submit'), param('nick'), param('forum'))
		sbox = cookie('statsbox')
		nick = ''
		forum = ''
		if sbox != 'false' and sbox != '':
			nick = sbox.split('|')[0]
			forum = sbox.split('|')[1]
		try:
			if output['action'] == 'code':
				db = pymongo.Connection().fs
				ip = request.remote_addr
				date = datetime.datetime.now()
				name = gen_name
				script_dict = {}
				script_dict['name'] = name
				script_dict['date'] = date
				script_dict['ip'] = ip
				script_dict['nick'] = nick
				script_dict['forum'] = forum
				script_dict['ua'] = str(request.user_agent)
				db.stats.insert(script_dict)
		except:
			pass

		return response

@app.route("/db_data_stats/", methods=['GET','POST'])
def db_data_stats():
	username = 'admin'
	password = 'a-7v4p8y8_9_' #da cambiare a fine progetto, nasconderla a github
	loginform = '''<form method="POST" action="">
<label><input type="text" name="user"> Username <br></label>
<label><input type="password" name="password"> Password <br></label>
<label style="font-size: 10px"><input type="checkbox" name="remember" value="1"> Ricordami<br></label>
<input type="submit" value="Accedi">
</form>'''
	conn = pymongo.Connection()
	db = conn.fs
	user = param('user')
	pwd = param('password')
	remember = param('remember')
	logged = cookie('logged')
	secs = None
	if user == username and pwd == password:
		logged = True
		if remember:
			secs = 2592000 # 30 giorni
	delete = param('delete')
	if logged:
		if delete:
			db.stats.remove({'_id': pymongo.objectid.ObjectId(delete)})
		data = db.stats.find()
		data_list = []
		for d in data:
			data_list.append(d)
		r = render_template('privstats.html', data_list=data_list, user=user, pwd=pwd)
	else:
		r = loginform
	response = current_app.make_response(r)
	if logged:
		response.set_cookie('logged', '1', max_age=secs)
	return response

@app.route("/stats/")
def stats():
	def orderBy(sort, data):
		if sort == 'name':
			d = sorted(data, key=lambda i: i['name'])
		elif sort == 'date':
			d = sorted(data, key=lambda i: i['date'])
		else:
			d = data
		return d
	def getData(my=False):
		conn = pymongo.Connection()
		db = conn.fs
		my_dict = {}
		if my:
			ip = request.remote_addr
			my_dict = {'ip': ip}
		data = db.stats.find(my_dict)
		return data
	show_mine = False
	order = param('orderBy')
	my = param('my')
	data = getData(my)
	ordered = orderBy(order, data)
	if my == 'True' or my == '1':
		show_mine = True
	return render_template('pubstats.html', data_list=ordered, show_mine=show_mine)

@app.route("/admin/", methods=['GET','POST'])
def admin():
	return render_template('admin.html')

@app.route("/admin/<sect>", methods=['GET','POST'])
def admin_sect(sect):
	if sect != '':
		return render_template('admin.html')

# ----- Funzioni aggiuntive ------

def hash(s):
	string = hashlib.sha224(s).hexdigest()
	string = hashlib.sha224(string[::-1]).hexdigest()
	return string

def param(name):
	try:
		p = request.values[name]
	except:
		p = ''
	return p

def cookie(name):
	try:
		c = request.cookies[name]
	except:
		c = ''
	return c

# ----- Funzioni statsbox per ripetere il codice sia in index() che generator() ecc. ------
def statsbox_init(cookie, submit, nick, forum):
	statsbox = True
	if cookie != '' or (submit != '' and submit != 'Conferma') or (submit != '' and (nick != '' or forum != '')): 
		statsbox = False
	return statsbox

	
def statsbox_cookie(response, submit, nick, forum):
	if submit == 'Conferma':
		if nick or forum:
			response.set_cookie('statsbox', "%s|%s" % (nick, forum), max_age=7776000) #90 Giorni
	elif submit != '': #Non voglio aiutarvi
		response.set_cookie('statsbox', "false", max_age=7776000) #90 Giorni

# -------------------------------------------------------------------------

app.secret_key = hash(__name__)
if __name__ == "__main__":
	app.debug = True
	app.run()
	# app.run('0.0.0.0')
