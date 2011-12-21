# This hook is an adapted version of pyi_rth_qt4plugins.py for PySide
import os

d = "qt4_plugins"

if "_MEIPASS2" in os.environ:
    d = os.path.join(os.environ["_MEIPASS2"], d)
else:
    d = os.path.join(os.path.dirname(sys.argv[0]), d)
# We remove QT_PLUGIN_PATH variable, beasuse we want Qt4 to load
# plugins only from one path.
os.environ['QT_PLUGIN_PATH'] = os.path.abspath(d)


# We cannot use QT_PLUGIN_PATH here, because it would not work when
# PyQt4 is compiled with a different CRT from Python (eg: it happens
# with Riverbank's GPL package).
from PySide.QtCore import QCoreApplication
# We set "qt4_plugins" as only one path for Qt4 plugins
QCoreApplication.setLibraryPaths([os.path.abspath(d)])
