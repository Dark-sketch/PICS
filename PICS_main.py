 #Система проверки целостности программ - СПЦП
 # необходимое
import shutil
import os
import sys
import requests
import winreg
import subprocess
import zlib
import time
 #
process_name = "discord.exe"
sign_have = 0
 #
 sigs_path = "./sigs/" + process_name + "_sigs.txt"
 sigs_local_path = "./sig.txt"

#сигнатуры
 if sign_have == 0:
     sign_have = 1
     sigs = subprocess.check_output('listdlls' + process_name).decode("utf-8")
     f = open(sigs_path, 'w')
     f.write( sigs )
     f.close()
