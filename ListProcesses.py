#in Admin eleveated CMD
# pip install wmi
# pip install pywin32

# list processes
import wmi
conn = wmi.WMI()
for process in conn.Win32_Process():
 print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
 process.ProcessId, process.HandleCount, process.Name
 )
 )

# filtering specific processes
#import wmi
#conn = wmi.WMI()
for process in conn.Win32_Process(name="chrome.exe"):
 if process.HandleCount > 1000: # only processes with handle count above 1000
    print(process.ProcessID, process.HandleCount, process.Name)