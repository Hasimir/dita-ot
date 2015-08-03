Things to be done for Jython installation
=========================================

* Finish the Python script.
* Proper manual instructions.
* Post-install scripts.


Post-Install Scripts and Action
-------------------------------

In these examples, assume running from dita-ot/src/main/ directory.

* make jython/Doc/jydoc as default sphinx target.
* make jython/Doc/jydoc/installation subdirectory.
* copy jbin/docs contents into jython/Doc/jydoc/installation firectory.
* make symlinks from jython/bin/* to bin/
* include both .rst and .md as source types for documentation.

With luck this may encourage greater use of docutils and reST to
provide additional methods of converting data to DITA and open
additional avenues for DITA exporting to other formats.

Obviously systems with pandoc as well as Jython/Python and Sphinx will
be even better suited to the task.  Those with stronger CPython
integration and the ReportLab package (or LaTeX) may be able to skip
using Java, Ant and FOP entirely when generating PDFs (very good if
the font bug in FOP 1.1 affects you).

