import subprocess #สำหรับ รัน terminal command


if __name__ == "__main__":
    ##basic
    #subprocess.run(["ls","-l"])
    #for i in [2,5,6,8]:
        #subprocess.run(["python3","python_101.py","9","--x",f"{i}","--yval", "2"])

    ##use output of subprocess
    #pro = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pro.communicate()
    #print(out)    27

    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ   #เป็น python3 เพราะ ใน ubuntu ลง python3 ไว้
    for i in [2,5,6,8]:
        pro = subprocess.Popen(["python3","python_101.py","9","--x",f"{i}","--yval", "2"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = pro.communicate()
        text = str(out,'utf-8')
        text = text.rstrip("\n")
        print(text[22:27]) 
        
        