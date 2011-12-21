hiddenimports = ['PySide.QtGui']

from hooks.hookutils import qt4_phonon_plugins_dir
pdir = qt4_phonon_plugins_dir(pyside=True)

datas = [
     (pdir + "/phonon_backend/*.so",      "qt4_plugins/phonon_backend"),
     (pdir + "/phonon_backend/*.dll",     "qt4_plugins/phonon_backend"),
     (pdir + "/phonon_backend/*.dylib",   "qt4_plugins/phonon_backend"),
]
