Jython Installation
===================

The installation scripts should be run from within the jbin/ directory.  This is because they use relative paths to determine the install locations.  This is also necessary because users might install dita-ot/ anywhere and a false assumption regarding paths will breakthings fast.

When the installation process has completed successfully a few Jython/Python commands will be issued.  These will install a current snapshot of docutils, the current version of requests and then move the jbin/ directory and all its components into resources/org/jython/ to get it out of the way.

Uninstallation should simply be a matter of removing the src/main/jython/ firectory and deleting the symbolic links in the bin/ directory.


Why install it at all?
----------------------

Docutils opens up a number of additional avenues for importing and exporting data and data types.  It may also provide alternatives to ant and fop when it comes to PDF conversions.


How complete is it?
-------------------

Anything written in pure Python for version 2.7.x should run.  Those modules which depend on C code, however, will not run.  This is a limitation of Java and cannot be circumvented.  So PIL is not available and neither are most of the cryptographic libraries (including PyCrypto, cryptography.py, PyME, GPyGME, etc.).  Interestingly, while CFFI cannot be installed (unsurprisingly), Cython can be installed.  So perhaps it can form part of a work around for that, but I'll leave that to the more adventurous.

Other major packages of interest which can be installed include Sphinx, Flask, Django and no doubt many others.


Which non-standard packages are installed here and why?
-------------------------------------------------------

* Requests

This is the single best HTTP library and module around for Python and it makes too many other things much easier to be ignored.  It is, for example, used to obtain the next package in the list.

* Docutils snapshot

The recommendation of the docutils developers is to install a recent snapshot instead of the last "official" stable as it is actually more stable and with better functionality.  The "official" one only exists as a concession to certain OS distributions.

* Sphinx

The Python documentation generator and manager of which docutils is the major component.  It has its own methods of generating certain file types from other mark up and down systems, especially reStructuredText (.rst) and Markdown (.md).  It also provides another avenue for generating ePub files and possibly PDF files.


What about ReportLab?
---------------------

ReportLab needs PIL and therefore C, so you'll need to utilise it outside of the Java environment, but no doubt that can be scripted.


I've got an API to generate/submit/etc. certain document types, can this help?
------------------------------------------------------------------------------

I'll direct your attention back to requests, go have fun.  ;)


