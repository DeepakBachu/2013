#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-gtk-doc-html --disable-gtk-doc --enable-introspection")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("ChangeLog", "NEWS")
