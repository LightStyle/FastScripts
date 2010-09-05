# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# ForumFree Magazine Fast Scripts Generator
#
# Copyright (C) 2010  Niccolo` "Kurono" Campolungo <damnednickix@hotmail.it>
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

from flask import *

run_port = 8080
app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Page'

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', run_port)