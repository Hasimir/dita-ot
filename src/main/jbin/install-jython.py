#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import os.path
import sys
import subprocess

ls = os.listdir
op = os.path
gtfo = None
    
try:
    import requests
    gotRequests = True
except:
    import urllib.request
    gotRequests = False

jpbigs = "https://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar"
jpjars = "https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar"
jpbigp = "http://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar"
jpjarp = "http://repo1.maven.org/maven2/org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar"
jpydir = "../resources/org/jython"
jpyijar = "jython-installer-2.7.0.jar"
jpysjar = "jython-standalone-2.7.0.jar"


if len(sys.argv) >= 2:
    jpyver = sys.argv[1]
elif len(sys.argv) < 2 and sys.version_info[0] == 2:
    jpyver = raw_input("""Which version of Jython do you want:

        1. full
        2. self-contained
    """)
elif len(sys.argv) < 2 and sys.version_info[0] == 3:
    jpyver = input("""Which version of Jython do you want:

        1. full
        2. self-contained
    """)


if jpyver.lower() == "all" or "full" or "1":
    jpyinst = jpydir+"/"+jpyijar
    jpsurl = jpbigs
    jppurl = jpbigp
    jpfull = True
else:
    jpyinst = jpydir+"/"+jpysjar
    jpsurl = jpjars
    jppurl = jpjarp
    jpfull = False


if gotRequests is True:
    try:
        r = requests.get(jpsurl, verified=True)
    except:
        r = requests.get(jppurl, verified=False)
    afile = open(jpyinst, "wb")
    afile.write(r.content)
    afile.close()
elif gotRequests is False and sys.version_info[0] == 3:
    import urllib.request
    afile = open(jpyinst, "wb")
    with urllib.request.urlopen(jpurl) as f:
        afile.write(f.read())
    afile.close()
elif gotRequests is False and sys.version_info[0] == 2:
    print("""We recommend you install the requests package or install manually.

Follow these instructions to install Jython manually:

    https://wiki.python.org/jython/InstallationInstructions

We recommend the full install by running:

java -jar jython_installer-2.7.0.jar --console

Accept the defaults for everything and install to src/main/jython in
the dita-ot distribution.

""")
    os.mkdir('../jython')
    gtfo = True
else:
    print("""You may need to install Jython manually.

Follow these instructions to install Jython manually:

    https://wiki.python.org/jython/InstallationInstructions

We recommend the full install by running:

java -jar jython_installer-2.7.0.jar --console

Accept the defaults for everything and install to src/main/jython in
the dita-ot distribution.

If you are using OS X, Linux, BSD or any similar *nix, the two bash
scripts should do most of this.  Windows users will need to do it
manually.
    """)
    os.mkdir('../jython')
    gtfo = True


if gtfo is True:
    sys.exit()
else:
    pass


if jpfull is True:
    try:
        # install with console
        # run pip to install docutils and requests
    except:
        # install without console
        # run pip to install docutils and requests
else:
    # add a shell script called "jython" to bin/ which calls the standalone
    # script via java.
