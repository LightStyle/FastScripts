# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# ForumFree Magazine Fast Scripts Generator
#
# Copyright (C) 2010 
# Niccolo` "Kurono" Campolungo <damnednickix@hotmail.it>
# Antonio Micari <darkstyle96@gmail.com>
# Damiano "Bowser" Faraone <bowser@ffmagazine.net>
#
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
#

import hashlib
from flask import Flask, render_template, Markup

app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha224(__name__).hexdigest()

@app.route("/")
def index():
    script = Markup("document.write('Test JavaScript<br />')")
    style = "body { background: #000; color: #fff; }"
    return render_template('index.html', **locals())

#funzione solo di controlla, verra' rimossa in seguito
@app.route("/s/")
def s():
    return hashlib.sha224(__name__).hexdigest()

@app.route("/admin/")
def admin():
    return render_template('admin.html', **locals())

if __name__ == "__main__":
    app.debug = True
    app.run()