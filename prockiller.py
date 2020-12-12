import ctypes


k_handle = ctypes.WinDLL("kernel32.dll")
u_handle = ctypes.WinDLL("user32.dll")


PROCESS_ALL_ACCESS =  (0x000F0000 | 0x00100000 | 0xFFF)


lpWindowName = ctypes.c_char_p(input("Enter Windows Name To Kill: ").encode('utf-8'))
hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
	print("Error Code: {0} - Could Not Grab Handle".format(k_handle.GetLastError()))
	exit(1)
else:
	print("Got Handle...")

lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
	print("Error Code: {0} - Could Not Grab PID".format(k_handle.GetLastError()))
	exit(1)
else:
	print("Got the PID!")


dwDesiredAccess = PROCESS_ALL_ACCESS
bInheitHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheitHandle, dwProcessId)

if hProcess <=0:
	print("Error Code: {0} - Could not grap priv handle".format(k_handle.GetLastError()))
else:
	print("Got our handle!")

uExitCode = 0x00100000
response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:
	print("Error Code: {0} - Could not  Terminate Process".format(k_handle.GetLastError()))
else:
	print("Process killed!")

'''
FindWindowA
GetWindowThreadProcessId
OpenProcess
TerminateProcess
'''