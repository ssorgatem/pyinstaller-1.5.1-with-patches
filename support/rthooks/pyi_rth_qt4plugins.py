# Qt4 plugins are bundled as data files (see hooks/hook-PyQt4*),
# within a "qt4_plugins" directory.
# We add a runtime hook to tell Qt4 where to find them.
import os

d = "qt4_plugins"

if "_MEIPASS2" in os.environ:
    d = os.path.join(os.environ["_MEIPASS2"], d)
else:
    d = os.path.join(os.path.dirname(sys.argv[0]), d)
# We remove QT_PLUGIN_PATH variable, beasuse we want Qt4 to load
# plugins only from one path.
if 'QT_PLUGIN_PATH' in os.environ:
    #In some platform python is unable to unset environment variables,
    #thus setting it to an empty string should do the trick there
    os.environ['QT_PLUGIN_PATH'] = ''
    del os.environ['QT_PLUGIN_PATH']

###################################################################################
#This is in order to make pyinstaller work when using PyQt4 with api v2
#Unfortunately it makes it stop working for applications using api v1
#In the near future (python3) only api2 will be supported, so applications using api v1
#should port their applications to api v2 anyway, which is, in addition, a lot 
#more pythonic
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
#Maybe there's a way to determine if an application is making to sip.setapi 
#and wrap this piece of code into an if statement
####################################################################################


# We cannot use QT_PLUGIN_PATH here, because it would not work when
# PyQt4 is compiled with a different CRT from Python (eg: it happens
# with Riverbank's GPL package).
from PyQt4.QtCore import QCoreApplication
# We set "qt4_plugins" as only one path for Qt4 plugins
QCoreApplication.addLibraryPath(os.path.abspath(d))
