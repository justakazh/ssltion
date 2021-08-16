import os


os.system("frida-ps -Uai")
i = str(input("Apk Identifier : "))
cmd = 'objection -g '+i+' explore -s "android sslpinning disable"'
os.system(cmd)
