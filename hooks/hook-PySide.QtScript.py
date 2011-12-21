hiddenimports = [ 'PyQt4.QtCore']

from hooks.hookutils import qt4_plugins_dir
pdir = qt4_plugins_dir(pyside=True)

datas = [
     (pdir + "/script/*.so",      "qt4_plugins/script"),
     (pdir + "/script/*.dll",     "qt4_plugins/script"),
     (pdir + "/script/*.dylib",   "qt4_plugins/script"),
]
