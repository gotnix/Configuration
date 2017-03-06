# $language = "python"
# $interface = "1.0"

# -*- coding=UTF-8 -*-

# 1) Screen.Get 不等建立连接就执行了，匹配不到输出
# 2) Screen.Send 不能加 True 选项
# 3) ReadString 和 WaitForStrings 匹配中文报类型错误 "an integer is required"
#	导致表驱动法(Table-Driven Approach) 或者函数字典(Function Map)的代码都用不了。
#	匹配中文可能需要用 unichr ord 转 ANSCII 码。
# 4) 处理命令行参数用 crt.Arguments，不用 Python 内置的模块
#
# 打开 Session Options 对话框，选择 Connection -> Logon Actions，
#	Logon Script 输入该脚本路径，Arguments 输入要登陆的主机 IP。

import SecureCRT

# 跳板机的密码
JUMPER_PW = 'XXXXXX'

def login_timeout():
	# crt.Screen.WaitWaitForStrings 超时提示
	crt.Dialog.MessageBox("Time Out.")


def send_ip(ip_addr):
	if crt.Screen.WaitForString("输入IP:", 1):
		crt.Screen.Send(ip_addr + "\n")
		crt.Screen.Clear()

def login_idc(ip_addr):
	#crt.Dialog.MessageBox("login_idc: 选机房")
	crt.Screen.Send("14\n")
	
	send_ip(ip_addr)

def login_pw(ip_addr):
	#crt.Dialog.MessageBox("login_pw 跳板机口令")
	crt.Screen.Send(JUMPER_PW + "\n")
	
	login_idc(ip_addr)

def Main():
	crt.Screen.Synchronous = True

	if crt.Arguments.Count == 1:
		#crt.Dialog.MessageBox("ARG == 2")
		ssh_host = crt.Arguments[0]

	dict = {
		0: login_timeout,
		1: login_pw,
		2: login_idc
	}

	# #prompt = crt.Screen.ReadString("请输入口令:", "请选择机房:", 10)
	# prompt = crt.Screen.WaitWaitForStrings("请输入口令:", "请选择机房:", 10)
	# idx_pmt = crt.Screen.MatchIndex

	# if idx_pmt in dict:
		# dict[idx_pmt]()
	
	if crt.Screen.WaitForString("请输入口令:",1):
		dict[1](ssh_host)
	else:
		dict[2](ssh_host)

	crt.Screen.Synchronous = False


Main()
