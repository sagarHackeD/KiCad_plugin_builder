import pcbnew
print(pcbnew.PLUGIN_DIRECTORIES_SEARCH)



import os




source_dir = r'C:\Users\ECHS\Desktop\KiCad\Place_By_Sch_KiCad\src'
link_dir = r'C:\Users\ECHS\Documents\KiCad\9.0\scripting\plugins\PBS'

try:
    os.symlink(source_dir, link_dir)
except FileExistsError:
    print("Symmlink exsist")