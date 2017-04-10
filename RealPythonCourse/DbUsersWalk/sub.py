import subprocess

cmd = "cat dbusers.py"
ret = subprocess.call(cmd, shell=True)
print ret
