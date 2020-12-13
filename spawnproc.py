import ctypes
from ctypes.wintypes import	HANDLE,DWORD,LPWSTR,WORD,LPBYTE

k_handle = ctypes.WinDLL("kernel32.dll")

#StructureforProcessInformation
class PROCESS_INFORMATION(ctypes.Structure):
	_fields_=[
	("hProcess",HANDLE),
	("hThread",HANDLE),
	("dwProcessId",DWORD),
	("dwThreadId",DWORD),
	]


#StructureforStartupInfo
class STARTUPINFO(ctypes.Structure):
	_fields_=[
	("cb", DWORD),
	("lpReserved", LPWSTR),
	("lpDesktop", LPWSTR),
	("lpTitle",LPWSTR),
	("dwX",DWORD),
	("dwY",DWORD),
	("dwXSize",DWORD),
	("dwYSize",DWORD),
	("dwXCountChars",DWORD),
	("dwYCountChars",DWORD),
	("dwFillAttribute",DWORD),
	("dwFlags",DWORD),
	("wShowWindow",WORD),
	("cbReserved",WORD),
	("lpReserved2",LPBYTE),
	("hStdInput",HANDLE),
	("hStdOutput",HANDLE),
	("hStdError",HANDLE),
	]

lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
lpCommandLine = None
lpProcessAttributes	= None
lpThreadAttributes	= None
lpEnvironment = None
lpCurrentDirectory = None	

dwCreationFlags	= 0x00000010
bInheritHandle	= False
lpProcessInformation = PROCESS_INFORMATION()	
lpStartupInfo = STARTUPINFO()
lpStartupInfo.wShowWindow = 0x1
lpStartupInfo.dwFlags = 0x1


response = k_handle.CreateProcessW(
	lpApplicationName,
	lpCommandLine,
	lpProcessAttributes,
	lpThreadAttributes,
	bInheritHandle,
	dwCreationFlags,
	lpEnvironment,
	lpCurrentDirectory,
	ctypes.byref(lpStartupInfo),
	ctypes.byref(lpProcessInformation))


if response > 0:
	print("Proc is running")
else:
	print("Failed, Error Code: {0}".format(k_handle.GetLastError()))
