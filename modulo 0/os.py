import os 

#obtener el directorio actual
cwd = os.getcwd()
print('Directorio de trabajo actual', cwd)

#Listar los archivos
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)

#renombrar archivo
os.rename('cuento.txt', 'little red hoody')
print('archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)
