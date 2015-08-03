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


How much disk space does it need?
---------------------------------

A full installation is about 180MB plus any additional modules installed along with their dependencies.  Expect around 200MB or so with the three additions (see below).  The installer .jar file is about 90MB.  A standalone installation is a little under 40MB, but cannot use additional Python modules.  Unless space is at an absolute premium, use the full installation.


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


What about Python 3?
--------------------

There is no Jython implementation using Python 3 yet.  If you need it, do what I do: write Python 3 scripts and then get Jython to call them as commands with subprocess or load them with the python3 interpreter also via subprocess.

Be careful, though, this also enables running any system command and could be a security issue depending on where dita-ot is installed and who has access to it.


What specifically does this add to DITA?  What problem does it solve?
---------------------------------------------------------------------

To implement ePub 3.0 correctly the dc:modified element must be updated in the metadata every time the .epub file is modified and saved.  The format for that is the ISO date and time format of "YYYY-MM-DDThh:mm:ssZ" and the "Z" on the end indicates that it MUST be UTC (Zulu time).  While XSLTs can add a datetime string in that format, they can't consistently obtain the timezone offset and add the correct real time.  Whereas Python and, in this case, Jython can.

The datetime module can be used to obtain the correct string to use at the time it is needed, while the xml modules can rewrite the metadata file itself.  These are all part of the standard library in Python and will thus be available even if only the standalone Jython .jar file is used instead of a full installation.

The correct datetime command to produce the string is::

    datetime.datetime.utcnow().isoformat()[:19] + "Z"

Like this::

    Python 2.7.10 (default, Jul 23 2015, 12:29:14) 
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import datetime
    >>> print(datetime.datetime.utcnow().isoformat()[:19] + "Z")
    2015-08-03T03:23:37Z
    >>> ^D

That's the thing which made me consider it necessary to at least have as an optional installation component.  No doubt there will be other tasks it will be better suited to addressing.


Couldn't that datetime thing have been done in Java directly?
-------------------------------------------------------------

Probably, but it wasn't.


Why didn't you do it in Java then?
----------------------------------

I loathe Java with the intensity of a thousand suns, never in Hell.


But why?  Java is great, it's platform independent and ...
----------------------------------------------------------

Let me just stop you right there.  It's not platform independent and never has been, though it has blurred the lines a little.  There are many, many faults with it and very good reasons why we never used it internally if we could avoid it and we always found ways to avoid it.

Sooner or later you'll dig deep enough on a system different from your usual one.  When the dull throbbing behind your eyes reaches a peak, remember, you were warned.


We?
---

Erm ... go find my LinkedIn if you haven't worked it out already.


You're a computing snob, aren't you?
------------------------------------

Well ... yes, I guess I am.


What directories and files are created?
---------------------------------------

Jython is installed to src/main/jython with the executables in src/main/jython/bin and symbolic links for those files created in src/main/bin.  The installer and/or stand alone .jar files are downloaded to src/main/resources/org/jython (with that last part made during the installation process.

When the installation completes, different things happen depending on the type of installation it is.

If you opted for a stand alone implementation via download then the following happens:

* The standalone file is saved in resources/org/jython.
* A shell script is created as bin/jython to load the .jar through java.
* A Windows batch file is made to mirror it as bin/jython.bat (maybe).
* jbin/ is moved into resources/org/jython
* src/main/jython is removed if it exists.

If you downloaded the full installer, but generated the standalone then this happened:

* The new standalone is installed to src/main/jython.
* The install file is saved in resources/org/jython.
* A shell script is created as bin/jython to load the .jar through java.
* A Windows batch file is made to mirror it as bin/jython.bat (maybe).
* jbin/ is moved into resources/org/jython

If the full installation was made then it is all in src/main/jython and this happened:

* The install file is saved in resources/org/jython.
* The jython executable is in src/main/jython/bin.
* Easy_install and pip are also in src/main/jython/bin.
* The Jython docs are in src/main/jython/Doc/javadoc.
* A new jydoc directory is made here: src/main/jython/Doc/jydoc.
* pip is used to install requests.
* requests is used to obtain the current docutils snapshot.
* docutils snapshot is installed with pip.
* sphinx is installed with pip (normally).
* sphinx files are generated and installed into jydoc.
* sphinx is made.
* jbin/docs files are copied to jydoc.
* jbin is moved to resources/org/jython.
* symlinks are made for the files in jython/bin to bin/
  
