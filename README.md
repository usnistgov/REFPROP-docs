# REFPROP-docs
A repository containing information about REFPROP for public consumption.  This includes the FAQ and other documentation provided by the REFPROP team

This repository is the home of [the FAQ page for REFPROP](http://pages.nist.gov/REFPROP-docs), which are stored on the ``nist-pages`` branch of this repository.

For questions about the contents of this repository, please email [Ian Bell](mailto:ian.bell@nist.gov)

The docs are hosted on ReadTheDocs: [![Documentation Status](https://readthedocs.org/projects/refprop-docs/badge/?version=latest)](http://refprop-docs.readthedocs.io/en/latest/?badge=latest)

# For developers

The GUI documentation came from the .CHM file that was provided with older versions of REFPROP.  There is a script in the scripts folder to convert the old CHM to restructured text (via ``Hh -decompile REFPROP.CHM``).  Likewise, the documentation from the FORTRAN files were stripped out and also converted to restructured text (see the script in the ``scripts`` folder).  The documentation generation process is entirely driven by a [Sphinx](http://www.sphinx-doc.org/en/master/)-based workflow; the underlying source files are in RST format, under source control, and then a range of other output formats can be generated (``htmlhtml`` (for CHM), PDF (via LaTeX), and HTML).

To generate one of the output formats, open a shell in the ``doc`` folder, and then do: ``make XXXX`` where ``XXXX`` is one of the output formats.  Here we currently use and support ``latex``,``html``, and ``htmlhelp`` output formats.  The documentation on RTD also generates epub output in addition to PDF and HTML outputs.

## Generation of CHM

The most challenging "feature" of the documentation generation is that the VB6-based graphical user interface of REFPROP requires that the ``mapid`` are also added and sychronized between the VB6 GUI and the documentation in the CHM.  After significant iteration, it was determined that the most reliable means of ensuring that the correct mapid are added is to add a block that looks like this to the .hhp file that is generated in ``_build/htmlhelp`` folder.

```
...

[MAP]
#define GENERAL_INFORMATION_STATUSLINE 5
#define GENERAL_INFORMATION_FIRSTTIMEUSERS 813

[ALIAS]
GENERAL_INFORMATION_STATUSLINE=General Information\statusline.html
GENERAL_INFORMATION_FIRSTTIMEUSERS=General Information\firsttimeusers.html

...
```

In theory an alias can be defined without the ``[MAP]`` entry, but that proved unsuccessful.  The VB6 GUI project file then needs to use the 813 id, for instance, to point to the page for first time users.  A complete build script of the CHM, plus compilation, is provided in the build_chm.py script next to this file.  It loads the aliases from the file aliases_backpack.txt into the .hhp file, and then, if all goes well, you should be able to do something like 
```
Hh -mapid 813 REFPROPdoc.chm
```
in ``doc/_build/htmlhelp`` to open the CHM right to the page for first time users.  If this doesn't work, you probably won't get any output at all, which is not at all helpful for debugging purposes.

### Other resources/information

* The ``#IVB`` file inside the .CHM (which is itself simply a compressed zip files that can be opened by tools like 7-zip) contains the ``mapid`` that are being used in binary format.  they can also be read out by several commercial or freeware CHM decompilers.