#this makes my plots pretty! but it is totally not mandatory to do it
import json
os.system("curl -O https://raw.githubusercontent.com/fedhere/UInotebooks/master/fbb_matplotlibrc.json")
os.system("mv " + "fbb_matplotlibrc.json " + os.getenv("PUIDATA"))
s = json.load( open(os.getenv ('PUIDATA')+"/fbb_matplotlibrc.json") )
plt.rcParams.update(s)
