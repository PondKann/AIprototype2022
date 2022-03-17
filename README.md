# AIprototype2022
## นางสาวกัณญารัตน์  พรมสุข  
## นักศึกษาชั้นปีที่ 4 สาขาสารสนเทศสถิติ มหาวิทยาลัยขอนแก่น

### 1) การใช้ Lenux บน cloud (Microsoft Azure) : 
   วิธีสมัครใช้งาน Azure ฟรีแบบนักศึกษา --> 
   https://drive.google.com/file/d/1-7q2w4l69mz5Pcznf7i5fvcL7IT13VJc/view?usp=sharing
   
      1) ดาวน์โหลด ubuntu และเปิด ubuntu 
      2) เปิด ubuntu จะขึ้นลิ้งวิธีการติดตั้งให้เราอ่าน
      3) copy code "wsl --install" ไว้ ไปวางใน administrator Windows PowerShell 
   

### 2) Cloud Virtual machine(VM) 
   วิธีใช้งาน VM บน Azure 
        
      1) Creat Resource groups
      2) Creat Virtual machines โดยเลือก Resource groups ที่ Creat ไว้ในข้อ 1 
      3) กด Connect ssh ในหน้า VM ที่สร้างไว้ 
      4) copy private key path ตรงหมายเลข 4(run the example command below to connect to your vm) ตัวอย่าง Kanny@23.0.03
      5) เปิด command line (Anaconda powershell prompt หรือ windows terminal หรือ microsoft azure cloud)
      6) พิมพ์ kanyarat:~$ ssh Kanny@23.0.03  (เลข 23.0.03 คือ Public IP address )
      7) ใส่รหัสก็สามารถเชื่อม VM และรันบนเครื่อง VM ที่เราตั้งไว้ใน Resource groups ได้

   คำสั่งต่าง ๆ
   
      ls      ดูว่าในที่ที่เราอยู่มีไฟล์อะไรอยู่บ้าง
      ls -l   แสดงข้อมูลแต่ละไฟล์อย่างละเอียด
      ls -lh  แสดงข้อมูลแต่ละไฟล์ให้คนสามารถเข้าใจได้ง่าย
      ls -lt  แสดงไฟล์แบบเรียงจาก ใหม่-เก่า
      ls -ltr แสดงไฟล์แบบเรียงจาก เก่า-ใหม่
      pwd     (print working directory) แสดง directory ที่กำลังอยู่
      clear   เคลียร์ code, output ต่าง ๆ ที่อยู่หน้าจอ
      cd      กดเข้าไปฟังโฟล์เดอร์     ex. เข้าไปในโฟล์เดอร์ code $cd code หรือ ออกจากโฟล์เดอร์ $cd .. 
      mkdir   สร้างโฟล์เดอร์           ex. mkdir + ชื่อโฟล์เดอร์
      rm      ลบไฟล์ 1 ไฟล์
      rm -R   ลบทุกไฟล์ที่อยู่ในโฟล์เดอร์นั้น   
      scp ./ชื่อไฟล์ directoryปลายทาง/.               ย้ายไฟล์เครื่อง-เครื่อง
      scp ./ชื่อไฟล์ ชื่อ vm@xx.xx:directoryปลายทาง/.   ย้ายไฟล์เครื่อง-vm      

3) วิธีรัน Notebook บน VM

      รันไฟล์ .py 
       
       kanny/code/AIprototype:$ python testsupprecess.py

      รัน Jupyter Notebook บน VM
       
       1) ติดตั้ง Jupyter Notebook ใน command line 
       2) kanny/code/AIprototype:$ Jupyter Notebook จะเด้งขึ้นเป็นหน้า Jupyter Notebook ที่สามารถพิมพ์โค้ดและรัน ด้วยทรัพยากรณ์ของ VM
       3)ถ้าไม่ได้เชื่อม VM ก็จะรันด้วยทรัพยากรณ์ของเครื่องเรา


4) Python บน command line (subprocess, python.py)
5) Git (git clone, git add, git commit, git push, git pull)
6) Google colab
7) API (Falsk)
8) Tensorflow, Pythorch
9) latex overleaf

