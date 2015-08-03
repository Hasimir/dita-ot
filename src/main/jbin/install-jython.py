#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import os.path
import sys
import subprocess

oe = os.environ
ls = os.listdir
op = os.path
gtfo = None
sp = subprocess


try:
    import requests
    gotRequests = True
except:
    import urllib.request
    gotRequests = False

jpurls = "https://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar"
jpurlp = "http://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar"
jpydir = "../resources/org/jython"
jpyjar = "jython-installer-2.7.0.jar"


jpyinst = jpydir+"/"+jpyjar


maninst = """
We recommend you install the requests package or install manually.

Follow these instructions to install Jython manually:

    https://wiki.python.org/jython/InstallationInstructions

We recommend the full install by running:

java -jar jython_installer-2.7.0.jar --console

Accept the defaults for everything and install to src/main/jython in
the dita-ot distribution.
"""

if gotRequests is True:
    try:
        r = requests.get(jpurls, verified=True)
    except:
        r = requests.get(jpurlp, verified=False)
    afile = open(jpyinst, "wb")
    afile.write(r.content)
    afile.close()
elif gotRequests is False and sys.version_info[0] == 3:
    try:
        import urllib.request
        afile = open(jpyinst, "wb")
        with urllib.request.urlopen(jpurlp) as f:
            afile.write(f.read())
        afile.close()
    except:
        print(maninst)
        gtfo = True
else:
    print(maninst)
    gtfo = True


if gtfo is True:
    sys.exit()
else:
    pass


try:
    java_home = oe["JAVA_HOME"]
except KeyError:
    java_home = None

if java_home is not None and java_home != "":
    java = "{0}/bin/java".format(java_home)
else:
    java = "java"


try:
    s1a = sp.Popen([java, "-jar", jpyinst, "--console"], stdout=sp.PIPE)
    s1b = s1a.communicate()[0].decode("utf-8")
    # install with console (may not work unless using os.system).
    # better put this in a shell script and launch that way.
except:
    s1a = sp.Popen([java, "-jar", jpyinst], stdout=sp.PIPE)
    s1b = s1a.communicate()[0].decode("utf-8")        
    # install without console, uses GUI instead.

# check to see if human opted for full install or just the stand alone from the
# installer.

if op.exists("../jython/bin/jython") is True:
    jpfull = True
    jython = "../jython/bin/jython"
    pip = "../jython/bin/pip2"
elif op.exists("../jython/jython.jar") is True:
    jpfull = False
else:
    jpfull = None


if jpfull is True:
    j1a = sp.Popen([pip, "install", "requests"], stdout=sp.PIPE)
    j1b = j1a.communicate()[0].decode("utf-8")
    os.mkdir("temp")
    import requests
    snap = "./temp/docutils-snapshot.tar.gz"
    shot = "http://docutils.sourceforge.net/docutils-snapshot.tgz"
    r = requests.get(shot)
    afile = open(snap, "wb")
    afile.write(r.content)
    afile.close()
    j2a = sp.Popen(["tar", "-xzvf", snap], stdout=sp.PIPE)
    j2b = j2a.communicate()[0].decode("utf-8")
    j3a = sp.Popen([pip, "install", "-e", "temp/"], stdout=sp.PIPE)
    j3b = j3a.communicate()[0].decode("utf-8")
    os.mkdir("../jython/Doc/jydoc")
    jydocs = "../jython/Doc/jydoc"
    j4a = sp.Popen([pip, "install", "sphinx"], stdout=sp.PIPE)
    j4b = j4a.communicate()[0].decode("utf-8")
    mydocs = ls("docs/")
    for i in range(len(mydocs)):
        shutil.copy2("docs/{0}".format(mydocs[i]),
                     "{0}/{1}".format(jydoc, mydocs[i]))
    jyb = ls("../jython/bin/")
    for i in range(len(jyb)):
        os.symlink("../jython/bin/{0}".format(jyb[i]),
                   "../bin/{0}".format(jyb[i]))
    print("""
To complete the installation process, run the sphinx-quickgen script
and direct the output to Doc/jydocs/ when prompted.
""")
    os.move("../jbin/", "../resources/org/jython/")
elif jpfull is False:
    afile = open("../bin/jython", "w")
    afile.write("""#!/bin/bash

{0} -jar ../jython/jython.jar
""".format(java))
    afile.close()
    os.chmod("../bin/jython", 755)
    os.move("../jbin/", "../resources/org/jython/")
elif jpfull is None:
    print(maninst)
    # Leave installation directories intact.
