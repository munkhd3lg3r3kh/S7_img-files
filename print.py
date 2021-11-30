import subprocess

#checks =["ATTACH","RAU","GMM","DETACH", "radio", "message"]
checks = ["RADIO","GMM","ioctl"]
proc = subprocess.Popen(['adb','shell','su -c dmesg -w'],stdout=subprocess.PIPE)



while True:
  line = proc.stdout.readline()
  if not line:
    break
  for check in checks:
    if str(line).find(check) != -1:
        print("##############################",end="")
        print(check, end="")
        print("##############################")
        print("yes:", line.rstrip())
        filename = "dmesg/"+str(check) + ".txt"
        open(filename, "a").write(str(line.rstrip())+"\n")
