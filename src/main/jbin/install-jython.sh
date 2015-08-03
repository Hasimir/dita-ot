#!/bin/bash

# Gets the Jython 2.7.0 installer and installs it with the locally
# configured Java installation.  By default Jython is installed to
# src/main/jython and the Jython executable will be
# src/main/jython/bin/jython (src/main/jython/bin/jython on Windows if
# this script can be easily ported).

# It is recommended that the install be attempted with the Python
# script and other script(s) only be utilised if it fails or if Python
# is not available.  Especially if using Windows because what follows
# won't work without Cygwin or something like that.

# Run this script from the directory it is in, the same goes for the
# Python version.

mkdir ../resources/org/jython
mkdir ../jython
curl -o ../resources/org/jython/jython-installer-2.7.0.jar https://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar
echo "The Jython installer is launching, select the defaults for every option."
echo "Once the installation is complete run the link-jython.sh script from the same directory."
echo "When it asks the path to install to, use this (copy it to the clipboard now):"
cd ../jython
pwd
java -jar ../resources/org/jython/jython-installer-2.7.0.jar --console

