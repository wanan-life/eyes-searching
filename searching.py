import sys,getopt
import re

FILEDATAOUT = []
SPILT = []

def start(argv):
    opts,args = getopt.getopt(argv,'-h-f:-o:',['help','filepath=','output='])
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            title = '''
             _____  __    __  _____        _____   _____       ___   _____    _____   _   _   _   __   
| ____| \ \  / / | ____|      /  ___/ | ____|     /   | |  _  \  /  ___| | | | | | | |  \ | | /  ___| 
| |__    \ \/ /  | |__        | |___  | |__      / /| | | |_| |  | |     | |_| | | | |   \| | | |     
|  __|    \  /   |  __|       \___  \ |  __|    / / | | |  _  /  | |     |  _  | | | | |\   | | |  _  
| |___    / /    | |___        ___| | | |___   / /  | | | | \ \  | |___  | | | | | | | | \  | | |_| | 
|_____|  /_/     |_____|      /_____/ |_____| /_/   |_| |_|  \_\ \_____| |_| |_| |_| |_|  \_| \_____/ 
            
            '''
            print(title)
            print("[*] Usage: python3 searching.py [options]")
            print("[*] Version is 1.0 ")
            print("Options:\n")
            info = '''
            -h,--help             Show basic help message and exit
            -f,--filepath=        Import target file
            -o,--output=          Export file to destination address
            '''
            print (info)
            exit()
        if opt_name in ('-f','--filepath'): #导入
            print("\n[*]------------------------[*]")
            print("[*] Filepath is :",opt_value)
            print("[*]------------------------[*]\n")
            openfile(opt_value)
            # do something
        if opt_name in ('-o','--output'): #导出
            print("\n[*]------------------------[*]")
            print("[*] OutPath is :",opt_value)
            print("[*]------------------------[*]\n")
            output(opt_value)
            exit()
            

    
def openfile(filepath):
    global FILEDATAOUT
    global SPILT
    try: 
        filedata = open(filepath,mode='r',newline='\n') #读取传入的文件参数数据
    except FileNotFoundError:
        print("输入的文件路径不存在！请检查确认文件是否存在？")
    else:
        filespilt = str(filedata.read().splitlines())
        #print(filespilt)
        pattern = re.compile(r"/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]") 
        SPILT = pattern.findall(filespilt)
        for FILEDATAOUT in SPILT:
            print(FILEDATAOUT)
        #print(spilt)
        
def output(outpath):
     try:
        if SPILT ==[]:
            print("文件内容为空，导出取消！")
            exit()
        else:
            file = open(outpath,'w',newline='\n')
            for i in SPILT:
                print(i)
                file.write(i+"\n")

                
            print("文件导出成功，路径：",outpath)
     except TypeError:
         print("error")
   
        
       

    
    
if __name__ == "__main__":
    start(sys.argv[1:])
    