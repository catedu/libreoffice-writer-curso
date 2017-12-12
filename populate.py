import os

archivos = []
RUTA = '''{% include "git+https://github.com/catedu/libreOffice-la-suite-ofimatica-libre.git/'''
FINALRUTA = '''" %}'''

for root, dirs, files in os.walk(os.getcwd()):
    if "node_modules" in dirs:
        dirs.remove("node_modules")
    for file in files:
        if file.endswith('.md'):
            archivos.append(file)

for file in archivos:
    fh = open(file, 'a')
    fh.write(RUTA + file + FINALRUTA)
    fh.close()