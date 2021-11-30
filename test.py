import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

checks = ["qwer","radio", "GMM"]

proc = subprocess.Popen(['adb','logcat'],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  for check in checks:      
    if str(line).find(check) != -1:
        print("##############################",end="")
        print(bcolors.OKCYAN+check+bcolors.ENDC, end="")
        print("##############################")
        print("yes:", line.rstrip())
        filename = "logcat/"+str(check) + ".txt"
        open(filename, "a").write(str(line.rstrip())+"\n")
