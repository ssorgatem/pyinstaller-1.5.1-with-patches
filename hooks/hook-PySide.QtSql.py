hiddenimports = ['PySide.QtCore', 'PySide.QtGui']

from hooks.hookutils import qt4_plugins_dir
pdir = qt4_plugins_dir(pyside=True)

datas = [
     (pdir + "/sqldrivers/*.so",      "qt4_plugins/sqldrivers"),
     (pdir + "/sqldrivers/*.dll",     "qt4_plugins/sqldrivers"),
     (pdir + "/sqldrivers/*.dylib",   "qt4_plugins/sqldrivers"),
]
