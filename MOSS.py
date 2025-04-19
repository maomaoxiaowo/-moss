                                                                                                        
import time  # 导入time模块，用于后续可能的时间处理
import turtle  # 导入turtle模块，用于图形绘制
import os
import random



def cuowu():
    """
    此函数用于处理错误输入情况。
    它会打印一条错误消息，并调用另一个函数xuniji()。
    """
    print('请检查输入是否正确！')  # 打印错误提示信息，提醒用户检查输入
    xuniji()  # 调用xuniji函数，以进行进一步的操作或初始化

def mimacuowu():
    """
    处理密码错误的情况

    此函数旨在处理用户登录时因输入错误密码而导致的错误情况。
    它通过调用登录函数来引导用户重新登录或进行其他错误处理流程。
    """
    denglu()

def zhuyecuowu():
    """
    主页错误提示函数。

    该函数用于在主页操作出现错误时提示用户，并在1秒后返回主页。
    """
    print('请检查输入是否正确！')  # 提示用户输入错误，需要检查
    time.sleep(1)  # 暂停1秒，让用户有时间阅读错误提示
    zhuye()  # 调用主页函数，返回主页

def xuniji():
    """
    询问用户是否启动虚拟机，并根据用户的选择进行相应操作。
    如果用户选择启动虚拟机，则启动虚拟机并调用qidong函数。
    如果用户选择不启动或输入无效，则调用cuowu函数。
    """
    print('是否启动虚拟机(y,n)?')
    hd=input('_')
    if hd=='y':
        print('正在启动550W')
        qidong()
    elif hd!='y' and hd!='n':
        cuowu()

def qidong():
    global yh, keyn, jiamifh, jiami, hd, shijian
    with open(r'D:\key.txt', 'r', encoding='utf-8') as file:
        key_n = file.readline()  # 修改: 使用 readline() 读取第一行

    with open(r'D:\yh.txt', 'r', encoding='utf-8') as file:
        yh_n = file.readline()  # 修改: 使用 readline() 读取第一行
    # 定义用户列表，存储用户信息
    yh = yh_n
    # 定义密码列表，存储用户密码信息
    keyn = key_n
    # 定义加密标志变量，用于指示是否进行加密，初始为True
    jiamifh = True
    # 定义加密变量，初始为False，用于后续可能的加密逻辑
    jiami = False
    # 定义用户输入的密码变量hd，初始值为'0'
    hd = '0'
    # 定义时间变量shijian，初始值为0，用于记录时间
    shijian = 0
    """
    模拟计算机启动过程并最终调用登录函数。
    
    该函数通过打印一系列启动信息来模拟计算机启动的过程，每个步骤之间使用time.sleep(0.1)到time.sleep(2)不等的时间间隔，
    以模拟各个组件启动的时间。启动过程包括CPU、GPU等硬件组件的初始化以及UEFI、MOSS等软件环境的加载。
    
    最后调用denglu()函数，假设进行系统登录操作。
    """
    # 模拟开机启动过程中的各个步骤
    time.sleep(0.1)
    print('正在开机')
    
    # 模拟CPU启动
    time.sleep(0.1)
    print('on cpu green joy sejnbv cjhci-fwehfg[ok]')
    
    # 模拟内存初始化
    time.sleep(0.1)
    print('on mijhhfjduhsajhajhdbcbx[ok]')
    
    # 模拟主板芯片组激活
    time.sleep(0.1)
    print('uifbhjdj jdfbbk-sdfs[ok]')
    
    # 模拟UEFI启动
    time.sleep(0.1)
    print('on open uefi')
    
    # 模拟磁盘初始化
    time.sleep(0.1)
    print('mk djhhfh md- cjdhfbv')
    
    # 模拟进入C盘MOSS目录
    time.sleep(0.1)
    print('cd c/mncik/mookm-moss')
    
    # 模拟MOSS系统加载
    time.sleep(0.1)
    print('moss jdkksj ospd-jfgfj jgdfjdje=fhfu2883[ooe]')
    
    # 模拟网络接口初始化
    time.sleep(0.1)
    print('mljjsif jhfn djfn-fhfgfrkegh[ok]')
    
    # 模拟GPU和其他外设启动
    time.sleep(0.1)
    print('on gpu/fd/piwi/550W/WIFI-PPIO[ok]')
    
    # 模拟特定路径的加载
    time.sleep(0.1)
    print('c/iruej/550w/Moss')
    time.sleep(0.1)
    print('c/iodie/wed/oeppe/cjcnds')
    time.sleep(0.1)
    print('d/pwuue/hfkj/oie')
    
    # 模拟系统准备就绪
    time.sleep(0.1)
    print('pei-ejf[ok]')
    time.sleep(0.5)
    print('c/iode/jfhhdj-dbhdu.poi')
    
    # 模拟加载关键系统文件
    time.sleep(0.3)
    print('c/moss/jjdi/opwi/kdur-ejdefu.llk')
    time.sleep(0.3)
    print('c/moss/jjdi/opwi/kdur-ppeufcs.llk')
    time.sleep(0.3)
    print('c/moss/jdud/jdfndj/jdljus/louw.mol')
    time.sleep(0.3)
    print('c/moss/jiou/java/mossa-moaa/lios-ppoi.jav[True]')
    
    # 模拟系统完全启动
    time.sleep(1)
    print('moss is open on tress miij')
    
    # 调用登录函数，假设进行系统登录
    denglu()

def denglu():
    """
    实现用户登录功能。
    该函数首先记录当前时间，然后提示用户输入用户名和密码。
    如果用户名和密码与预定义的值匹配，则登录成功，否则无进一步操作。
    """
    global yh, keyn, shijian  # 修改: 添加 keyn 为全局变量
    # 记录用户登录时间
    shijian = time.time()  # 修改: 调用time.time()获取当前时间戳
    print(shijian)
    # 欢迎信息
    print('欢迎使用moss25m2')
    # 提示用户输入用户名
    print('请输入用户名：')
    user = input('_')
    print(user)
    print(yh)
    yh = yh.replace('\n', '')
    keyn = keyn.replace('\n', '')
    # 检查用户名是否匹配
    if user != yh:
        print('用户名错误，请重新输入！')
        mimacuowu()
    else:
        # 提示用户输入密码
        print('请输入密码：')
        pwd = input('_')
        # 检查用户是否匹配
        if user == yh and pwd == keyn:
            # 登录成功，显示欢迎信息
            print('欢迎登录！')
            # 调用主页函数，显示系统信息选项
            zhuye()
        else:
            # 登录失败，显示错误信息
            print('密码错误，请重新输入！')
            mimacuowu()
def zhuye():
    """
    主页函数，显示系统信息选项并根据用户选择执行对应操作。
    """
    print('欢迎使用moss')
    print('1.查看系统时间')
    print('2.查看系统日期')
    print('3.查看系统版本')
    print('4.查看系统信息')
    print('5.查看系统目录')
    print('6.查看系统文件')
    print('7.查看系统进程')
    print('8.查看系统内存')
    print('9.查看系统硬盘')
    print('10.查看系统网卡')
    print('11.查看系统网关')
    print('12.查看系统DNS')
    print('13.查看系统IP')
    print('14.查看系统MAC')
    print('15.查看系统CPU')
    print('16.查看系统GPU')
    print('17.查看系统WIFI')
    print('18.查看系统蓝牙')
    print('19.查看系统摄像头')
    print('20.查看系统打印机')
    print('21.查看系统键盘')
    print('22.查看系统鼠标')
    print('23.查看系统鼠标指针')
    print('24.查看系统鼠标滚轮')
    print('25.查看系统鼠标键')
    print('26.查看系统鼠标键位')
    print('27.设置')
    print('28.退出')
    print('29.关机')
    print('30.重启')
    print('31.注销')
    print('32.文件资源管理器')
    print('33.以管理员权限运行命令提示符')
    print('34.开始菜单(bata)')
    hd=input('_')
    
    # 根据用户选择显示系统时间
    if hd=='1':
        print('当前系统时间：')
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        zhuye()
    
    # 根据用户选择显示系统日期
    if hd=='2':
        print('当前系统日期：')
        print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        zhuye()

    # 根据用户选择显示系统版本
    if hd=='3':
        print('当前系统版本：')
        print('550W-24h1')
        zhuye()
    
    # 根据用户选择显示系统信息
    if hd=='4':
        print('当前系统信息：')
        print('550W')
        zhuye()
    
    # 根据用户选择显示系统目录
    if hd=='5':
        print('当前系统目录：')
        print('c:/')
        zhuye()
    
    # 根据用户选择显示系统文件
    if hd=='6':
        print('当前系统文件：')
        print('c:/moss/')
        zhuye()
    
    # 根据用户选择显示系统进程
    if hd=='7':
        print('当前系统进程：')
        print('moss')
        zhuye()

    # 根据用户选择显示系统内存
    if hd=='8':
        print('当前系统内存：')
        print('c:/=1024GB d:/=1024GB e:/=1024GB f:/=1024GB')
        zhuye()

    # 根据用户选择显示系统硬盘
    if hd=='9':
        print('当前系统硬盘：')
        print('c:/ d:/ e:/ f:/')
        zhuye()
    
    # 根据用户选择显示系统网卡
    if hd=='10':
        print('当前系统网卡：')
        print('wifi-10')
        zhuye()

    # 根据用户选择显示系统网关
    if hd=='11':
        print('当前系统网关：')
        print('10.10.10.10')
        zhuye()

    # 根据用户选择显示系统DNS
    if hd=='12':
        print('当前系统DNS：')
        print('10.10.109.10')
        zhuye()
    
    # 根据用户选择显示系统IP
    if hd=='13':
        print('当前系统IP：')
        print('109.101.10.10')
        zhuye()
    
    # 根据用户选择显示系统MAC
    if hd=='14':
        print('当前系统MAC：')
        print('10-10-10-10-10-10')
        zhuye()

    # 根据用户选择显示系统CPU
    if hd=='15':
        print('当前系统CPU：')
        print('internal-cpu-i5')
        zhuye()

    # 根据用户选择显示系统GPU
    if hd=='16':
        print('当前系统GPU：')
        print('internal-gpu-gtx-10')
        zhuye()

    # 根据用户选择显示系统WIFI
    if hd=='17':
        print('当前系统WIFI：')
        print('wifi-10')
        zhuye()

    # 根据用户选择显示系统蓝牙
    if hd=='18':
        print('当前系统蓝牙：')
        print('bluetooth-10')
        zhuye()

    # 根据用户选择显示系统摄像头
    if hd=='19':
        print('当前系统摄像头：')
        print('camera-10')
        zhuye()

    # 根据用户选择显示系统打印机
    if hd=='20':
        print('当前系统打印机：')
        print('printer-10')
        zhuye()

    # 根据用户选择显示系统键盘
    if hd=='21':
        print('当前系统键盘：')
        print('keyboard-10')
        zhuye()

    # 根据用户选择显示系统鼠标
    if hd=='22':
        print('当前系统鼠标：')
        print('mouse-10')
        zhuye()
    
    # 根据用户选择显示系统鼠标指针
    if hd=='23':
        print('当前系统鼠标指针：')
        print('mouse-pointer-10')
        zhuye()

    # 根据用户选择显示系统鼠标滚轮
    if hd=='24':
        print('当前系统鼠标滚轮：')
        print('mouse-wheel-10')
        zhuye()

    # 根据用户选择显示系统鼠标键
    if hd=='25':
        print('当前系统鼠标键：')
        print('mouse-key-10')
        zhuye()

    # 根据用户选择显示系统鼠标键位
    if hd=='26':
        print('当前系统鼠标键位：')
        print('mouse-key-10')
        zhuye()

    # 根据用户选择进入设置界面
    if hd=='27':
        print('当前系统设置：')
        print('1.设置用户名')
        print('2.设置密码')
        print('3.设置系统版本')
        print('4.设置系统信息')
        print('5.设置系统目录')
        print('6.设置系统文件')
        print('7.设置系统进程')
        print('8.设置系统内存')
        print('9.设置系统硬盘')
        print('10.添加用户')
        print('11.删除用户')
        hd=input('_')
        
        # 设置用户名
        if hd=='1':
            print('请输入用更改后的用户名：')
            usen=input('_')
            # 修改: 打开 D:\新建文本文档.txt 文件并修改第一行
            with open(r'D:\yh.txt', 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    lines[0] = usen + '\n'
                else:
                    lines.append(usen+'\n')
                file.seek(0)
                file.writelines(lines)
            print('用户名设置成功！')
            zhuye()
        
        # 设置密码
        if hd=='2':
            print('请输入要更改的密码用户原密码：')
            pwd=input('_')
            if pwd==keyn:

                print('请输入密码：')
                key=input('_')
                print('请再次输入密码：')
                kkey=input('_')
                if key==kkey:
                    with open(r'D:\key.txt', 'r+', encoding='utf-8') as file:
                        lines = file.readlines()
                        if lines:
                            lines[0] = key + '\n'
                        else:
                            lines.append(key + '\n')
                        file.seek(0)
                        file.writelines(lines)
                    print('密码设置成功！')
                    print('五秒后从新启动程序！')
                    time.sleep(5)
                    os.system('&python D:\python\python.exe D:\python\python.py')
                    
            else:
                print('密码错误！')
                zhuye()
            
            
        # 设置系统版本
        if hd=='3':
            print('无权限')
            zhuye()

        # 设置系统信息
        if hd=='4':
            print('无权限')
            zhuye()
            
        # 设置系统目录
        if hd=='5':
            print('无权限')
            zhuye()

                # 检查用户输入的hd值是否为6、7、8或9，这些值表示用户没有权限
        if hd=='6':
            # 当hd为6时，打印无权限提示信息
            print('无权限')
            zhuye()

        
        if hd=='7':
            # 当hd为7时，打印无权限提示信息
            print('无权限')
            zhuye()

        
        if hd=='8':
            # 当hd为8时，打印无权限提示信息
            print('无权限')
            zhuye()

        
        if hd=='9':
            # 当hd为9时，打印无权限提示信息
            print('无权限')
            zhuye()


    # 根据用户输入执行对应的操作
    if hd=='28':
        # 退出系统操作
        print('正在退出系统...')
        time.sleep(1)
        print('退出成功！')
        xuniji()

    if hd=='29':
        # 关机操作
        print('正在关机...')
        time.sleep(1)
        xuniji()

    if hd=='30':
        # 重启操作
        print('正在重启...')
        time.sleep(1)
        qidong()

    if hd=='31':
        # 注销操作
        print('正在注销...')
        time.sleep(1)
        denglu()

    if hd=='32':
        # 文件资源管理器操作
        print('文件资源管理器')
        print('4个目录')
        print('1.c:/')
        print('2.d:/')
        print('3.e:/')
        print('4.f:/')
        hd=input('_')
        if hd=='1':
            # 打开C盘操作
            print('正在打开c:/...')
            time.sleep(1)
            print('打开成功！')
            print('7个对象')
            print('1.c:/users')
            print('2.c:/windows')
            print('3.c:/system32')
            print('4.c:/program files')
            print('5.c:/program files (x86)')
            print('6.c:/program files/internet explorer')
            print('7.c:/program files/internet explorer/iexplore.exe')
            hd=input('_')
            if hd=='1':
                # 打开C盘用户目录操作
                print('1.text')
                print('正在打开c:/users...')
                print('打开成功！')
                print('10个对象')
                print('1.c:/users/administrator')
                print('2.c:/users/administrator/desktop')
                print('3.c:/users/administrator/documents')
                print('4.c:/users/administrator/downloads')
                print('5.c:/users/administrator/my documents')
                print('6.c:/users/administrator/my music')
                print('7.c:/users/administrator/my pictures')
                print('8.c:/users/administrator/my video')
                print('9.c:/users/administrator/my videos')
                print('10.c:/users/administrator/my videos/my video')
                er=int(input('_'))
                if er==1:
                    zhuye()
                else:zhuye()
            if hd=='2':
                # 打开C盘Windows目录操作
                print('1.text')
                print('正在打开c:/windows...')
                print('打开成功！')
                print('0个对象')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()
            if hd=='3':
                # 打开C盘System32目录操作
                print('1.text')
                print('正在打开c:/system32...')
                print('打开成功！')
                print('5个对象')
                print('1.c:/system32/cmd.exe')
                print('2.c:/system32/explorer.exe')
                print('3.c:/system32/notepad.exe')
                print('4.c:/system32/winlogon.exe')
                print('5.c:/system32/winmm.dll')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()
            if hd=='4':
                # 打开C盘Program Files目录操作
                print('1.text')
                print('正在打开c:/program files...')
                print('打开成功！')
                print('0个对象')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()
            if hd=='5':
                # 打开C盘Program Files (x86)目录操作
                print('1.text')
                print('正在打开c:/program files (x86)...')
                print('打开成功！')
                print('0个对象')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()

            if hd=='6':
                # 打开C盘Program Files/Internet Explorer目录操作
                print('1.text')
                print('正在打开c:/program files/internet explorer...')
                print('打开成功！')
                print('0个对象')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()
            if hd=='7':
                # 打开C盘Program Files/Internet Explorer/iexplore.exe操作
                print('1.text')
                print('正在打开c:/program files/internet explorer/iexplore.exe...')
                print('打开成功！')
                print('0个对象')
                er=int(input('_'))
                if er==1 :zhuye()
                else:zhuye()
        if hd=='2':
            # 打开D盘操作
            print('1.text')
            print('正在打开d:/...')
            time.sleep(1)
            print('打开成功！')
            print('个对象')
            er=int(input('_'))
            if er==1 :zhuye()
            else:zhuye()
        if hd=='3':
            # 打开E盘操作
            print('1.text')
            print('正在打开e:/...')
            time.sleep(1)
            print('打开成功！')
            print('0个对象')
            er=int(input('_'))
            if er==1 :zhuye()
            else:zhuye()
        if hd=='4':
            # 打开F盘操作
            print('1.text')
            print('正在打开f:/...')
            time.sleep(1)
            print('打开成功！')
            print('0个对象')
            er=int(input('_'))
            if er==1 :zhuye()
            else:zhuye()

    # 显示模块选择界面
    if hd=='33':
        print('module')
        print('1.os(cmd)')
        print('2.time')
        print('3.random')
        hd=input('_')
    
        # 用户选择os模块
        if hd=='1':
            print('os')
            print('1.os.system(cmd)')
            print('2.os.getcwd')
            print('3.os.listdir')
            print('4.os.mkdir')
            print('5.os.rmdir')
            print('6.os.rename')
            print('7.os.remove')
            print('8.os.path.exists')
            print('9.os.path.getsize')
            print('10.os.path.getatime')
            hd=input('_')
        
            #   根据用户选择执行os模块的不同功能
            if hd=='1':
                print('os.system')
                print('1.退出')
                print('请输入要执行的命令：')
                while True:
                    hd=input('_')
                    if hd=='1':
                        print('退出')
                        time.sleep(1)
                        zhuye()
                    else:
                        os.system(hd)
                        
                        

            if hd=='2':
                print('os.getcwd')
                print('当前目录为：')
                print(os.getcwd())
                time.sleep(1)
                zhuye()

            if hd=='3':
                print('os.listdir')
                print('请输入要查看的目录：')
                hd=input('_')
                print(os.listdir(hd))
                time.sleep(1)
                zhuye()
        
            if hd=='4':
                print('os.mkdir')
                print('请输入要创建的目录：')
                hd=input('_')
                os.mkdir(hd)
                time.sleep(1)
                zhuye()

            if hd=='5':
                print('os.rmdir')
                print('请输入要删除的目录：')
                hd=input('_')
                os.rmdir(hd)
                os.rmdir(hd)

                time.sleep(1)
                zhuye()
        
            if hd=='6':
                print('os.rename')
                print('请输入要重命名的目录：')
                hd=input('_')
                print('请输入重命名后的目录：')
                hd1=input('_')
                os.rename(hd,hd1)
                time.sleep(1)
                zhuye()
        
            if hd=='7':
                print('os.remove')
                print('请输入要删除的文件：')
                hd=input('_')
                os.remove(hd)
                time.sleep(1)
                zhuye()

            if hd=='8':
                print('os.path.exists')
                print('请输入要判断的文件或目录：')
                hd=input('_')
                if os.path.exists(hd):
                    print('存在')
                else:
                    print('不存在')
                time.sleep(1)
                zhuye()
        
            if hd=='9':
                print('os.path.getsize')
                print('请输入要判断的文件：')
                hd=input('_')
                print(os.path.getsize(hd))
                time.sleep(1)
                zhuye()

            if hd=='10':
                print('os.path.getatime')
                print('请输入要判断的文件：')
                hd=input('_')
                print(os.path.getatime(hd))
                time.sleep(1)
                zhuye()

        # 用户选择time模块
        if hd=='2':
            print('time')
            print('1.time.sleep')
            print('2.time.strftime')
            hd=input('_')
            if hd=='1':
                print('time.sleep')
                print('请输入要休眠的时间：')
                hd=input('_')
                time.sleep(hd)
                zhuye()
            if hd=='2':
                print('time.strftime')
                zhuye()

        # 用户选择random模块
        if hd=='3':
            print('random')
            print('1.random.randint')
            hd=input('_')
            if hd=='1':
                print('random.randint')
                print('请输入要生成的最小值：')
                hd=int(input('_'))
                print('请输入要生成的最大值：')
                hd1=int(input('_'))
                print(random.randint(hd,hd1))
                time.sleep(1)
                zhuye()

    if hd==34:
        wenjian=[]
        def read_and_print_files(directory, num_files):
            
    
            """
            读取指定目录下的文件，并按顺序输出前面指定数量的文件名。

            :param directory: 目录路径
            :param num_files: 要输出的文件数量
            """
            try:
                # 获取目录下的所有文件和子目录
                files = os.listdir(directory)
                # 按顺序输出指定数量的文件名
                for i, file in enumerate(files[:num_files], start=1):
                    print(f"{i}: {file}")
                    wenjian.append(f"{i}: {file}")

            except FileNotFoundError:
                print(f"目录 {directory} 不存在")
            except PermissionError:
                print(f"没有权限访问目录 {directory}")

        # 输出全局变量 a 的值



        # 调用新函数读取并输出指定数量的文件名
        directory_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
        num_files_to_display = 1000000  # 指定要输出的文件数量
        read_and_print_files(directory_path, num_files_to_display)
        #print (wenjian)
        hd=int(input('_'))

        print(wenjian[hd])

        file_name = wenjian[hd]  # 提取文件名
        file_path = os.path.join(directory_path, file_name)  # 构建完整文件路径
        try:
            os.open(file_path, 'r')
        except FileNotFoundError:
            print(f"文件 {file_name} 不存在")
        except PermissionError:
            print(f"没有权限访问文件 {file_name}")
        except Exception as e:
            print(f"读取文件 {file_name} 时发生错误: {e}")

    zhuye()
    # 用户选择超出预期范围
    if hd>='34':
        zhuyecuowu()
# 检查's.txt'文件是否存在，如果不存在则创建并写入'1'
if os.path.exists('D:\s.txt'):
    print()
else:
    with open(r'D:\s.txt', 'w', encoding='utf-8') as key_file:
        key_file.write('1')

# 检查'yh.txt'文件是否存在，如果不存在则创建并写入'moss'
if os.path.exists('D:\yh.txt'):
    print()
else:
    with open(r'D:\yh.txt', 'w', encoding='utf-8') as key_file:
        key_file.write('moss')

# 检查'key.txt'文件是否存在，如果不存在则调用xuniji()函数或创建并写入'874748'
if os.path.exists('D:\key.txt'):
    with open(r'D:\key.txt', 'r', encoding='utf-8') as file:
        key_n = file.readline()  # 修改: 使用 readline() 读取第一行

    with open(r'D:\yh.txt', 'r', encoding='utf-8') as file:
        yh_n = file.readline()  # 修改: 使用 readline() 读取第一行
    # 定义用户列表，存储用户信息
    yh = yh_n
    # 定义密码列表，存储用户密码信息
    keyn = key_n
    # 定义加密标志变量，用于指示是否进行加密，初始为True
    jiamifh = True
    # 定义加密变量，初始为False，用于后续可能的加密逻辑
    jiami = False
    # 定义用户输入的密码变量hd，初始值为'0'
    hd = '0'
    # 定义时间变量shijian，初始值为0，用于记录时间
    shijian = 0
    xuniji()
else:
    with open(r'D:\key.txt', 'w', encoding='utf-8') as key_file:
        key_file.write('874748')
    print('检测到您没有创建该文件所需的文件已自动帮您创建文件')
with open(r'D:\key.txt', 'r', encoding='utf-8') as file:
        key_n = file.readline()  # 修改: 使用 readline() 读取第一行

with open(r'D:\yh.txt', 'r', encoding='utf-8') as file:
    yh_n = file.readline()  # 修改: 使用 readline() 读取第一行
# 定义用户列表，存储用户信息
yh = yh_n
# 定义密码列表，存储用户密码信息
keyn = key_n
# 定义加密标志变量，用于指示是否进行加密，初始为True
jiamifh = True
# 定义加密变量，初始为False，用于后续可能的加密逻辑
jiami = False
# 定义用户输入的密码变量hd，初始值为'0'
hd = '0'
# 定义时间变量shijian，初始值为0，用于记录时间
shijian = 0
xuniji()
 #ghgfdgfhkgyvhjkygvgut
#基础决定高度hi                                                                                                                                     