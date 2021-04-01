import cx_Freeze
import os
import sys


base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r"C:\Users\MadGeek\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\MadGeek\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable('img-to-doc.py', base=base, icon='icon.ico')]

cx_Freeze.setup(
    name='Image to Doc Converter',
    options={'build_exe': {'packages': ['tkinter', 'os', 'pytesseract', 'PIL'], 'include_files': ['icon.ico','tcl86t.dll', 'tk86t.dll']}},
    version='1.0',
    author='Md. Hasibul Hasan Shovo',
    author_email='it.hhs19@gmail.com',
    description='Image to doc converter tool helps to translate JPG or PNG images to word with the assistance of text scanner.',
    keywords=['image to text', 'converter', 'image to text converter', 'image to doc converter', 'image to text generator'],
    executables=executables
)
