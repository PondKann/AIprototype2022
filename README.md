# AIprototype2022
## นางสาวกัณญารัตน์  พรมสุข  
## นักศึกษาชั้นปีที่ 4 สาขาสารสนเทศสถิติ มหาวิทยาลัยขอนแก่น

### 1) การใช้ Linux บน cloud : 
   วิธีสมัครใช้งาน Azure ฟรีแบบนักศึกษา --> 
   https://drive.google.com/file/d/1-7q2w4l69mz5Pcznf7i5fvcL7IT13VJc/view?usp=sharing
   
   1) ดาวน์โหลด ubuntu และเปิด ubuntu 
   2) เปิด ubuntu จะขึ้นลิ้งวิธีการติดตั้งให้เราอ่าน
   3) copy code "wsl --install" ไว้ ไปวางใน administrator Windows PowerShell 
   

### 2) Cloud Virtual machine(VM) 
   วิธีใช้งาน VM บน Microsoft Azure
        
   1) Creat Resource groups
   2) Creat Virtual machines โดยเลือก Resource groups ที่ Creat ไว้ในข้อ 1 
   3) กด Connect ssh ในหน้า VM ที่สร้างไว้ 
   4) copy private key path ตรงหมายเลข 4(run the example command below to connect to your vm) ตัวอย่าง Kanny@23.0.03
   5) เปิด command line (Anaconda powershell prompt หรือ windows terminal หรือ microsoft azure cloud)
   6) พิมพ์ kanyarat:~$ ssh Kanny@23.0.03  (เลข 23.0.03 คือ Public IP address )
   7) ใส่รหัสก็สามารถเชื่อม VM และรันบนเครื่อง VM ที่เราตั้งไว้ใน Resource groups ได้

#### คำสั่งบน command line
   คำสั่งทั่วไป 
   
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
      code    คำสั่งเพื่อเปิดไฟล์หรือสร้างไฟล์.py ซึ่งจะเป็นการเปิด visual studio code เพื่อแก้ไขไฟล์.py นั้น (.py / .csv )
      
   คำสั่งย้ายไฟล์
   
      scp ./ชื่อไฟล์ directoryปลายทาง/.               ย้ายไฟล์เครื่อง-เครื่อง
      scp ./ชื่อไฟล์ ชื่อ vm@xx.xx:directoryปลายทาง/.   ย้ายไฟล์เครื่อง-vm
  
   คำสั่ง Git 
     
      สร้างบัญชี Github (Pondkann คือชื่อ Github)
      git config --global user.name "Pondkann"  
      git config --global user.email Pondkann@example.com
   
      git clone     การโคลน/คัดลอก Github เพื่อมาใช้งานบน command line  
                    ($ git clone ลิงค์ Github แบบ HTTPS) 
                    ถ้าเป็น Github เราเอง สามารถแก้ไขไฟล์ คอมมิต ได้ทั้งหมด  
                    ถ้าเป็น Github คนอื่น ใช้ในกรณีที่นำโค้ดมารันเลย ไม่มีการแก้ไข
                    ถ้าต้องการแก้ไข Github คนอื่น ต้อง Fork ให้เป็นชื่อ Github เราก่อนค่อย clone
      git add       การ add ไฟล์ที่จะคอมมิต (--all, -A เพื่อ add ไฟล์ทั้งหมดในโฟล์เดอร์ที่เราอยู่)
      git commit    การ commit ไฟล์ที่ add แล้วเข้าไปใน Github 
                    (-m เพื่อเพิ่มข้อความ, --all, -a เพื่อ commit ไฟล์ทั้งหมดที่เรา add)
      git push      การ push ไฟล์ที่ commit แล้วเข้าไปใน Github เป็นขั้นตอนสุดท้ายแล้ว จะให้ใส่ user&password จาก Github Developer 
                    (--all เพื่อ push ไฟล์ทั้งหมดที่เรา commit)
      git pull      การ pull ไฟล์ทั้งหมดที่อยู่ใน Github ลงมาบน command line (เหมือนเป็นการอัพเดตไฟล์ข้อมูล)
      
   คำสั่ง conda 
        
      conda insatll - c anaconda git            เชื่อม conda กับ git
      conda insatll numpy, opencv-python        การ install แพ็กเกจต่างๆ a
      conda create - n testpy3.7 python=3.7     การสร้าง environment ชื่อ testpy3.7 เพื่อใช้งาน python ver 3.7
      conda create - n tf tensorflow            การสร้าง environment ชื่อ tf เพื่อไว้ใช้งาน tensorflow
      conda activate หรือ deactivate testpy3.7   การ activate/deactivate environment ชื่อ testpy3.7 
      
      conda list    การแสดง packages ใน environment
      conda info
      
      
      

### 3) วิธีรัน Notebook บน VM

   รันไฟล์ .py 
      
       kanny/code/AIprototype:$ python testsupprecess.py

   รัน Jupyter Notebook บน VM
       
   1) ติดตั้ง Jupyter Notebook ใน command line 
   2) kanny/code/AIprototype:$ Jupyter Notebook จะเด้งขึ้นเป็นหน้า Jupyter Notebook ที่สามารถพิมพ์โค้ดและรัน ด้วยทรัพยากรณ์ของ VM
   3) ถ้าไม่ได้เชื่อม VM ก็จะรันด้วยทรัพยากรณ์ของเครื่องเรา


### 4) Python บน command line (subprocess, python.py)   [code](https://github.com/PondKann/AIprototype2022/blob/main/testsubprocess.py)
   subprocess คือ ฟังก์ชันที่ใช้ควบคุมคำสั่งบน command line 
   
   1) คำสั่ง kanny/code/AIprototype:$ ls จะแสดงไฟล์ทั้งหมดที่อยู่ใน AIprototype 
   2) ถ้าใช้ฟังก์ชัน subprocess จะเป็น subprocess.run('ls') บันทึกในไฟล์ testsubprocess.py 
      เมื่อรันจะได้ output เป็นไฟล์ทั้งหมดที่อยู่ใน AIprototype เหมือนข้อ 1 


