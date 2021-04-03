from google.drive import files
arch_sub = files.upload()
for fn in arch_sub.keys():
    print('Nombre del archivo subido: "{name}" tamaño del archivo: {length} bytes \n'.format(
      name=fn, length=len(arch_sub[fn])))
      