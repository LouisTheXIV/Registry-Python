import winreg as reg


key_path = r"*\\shell\\Test Program"
command_key_path = r"*\\shell\\Test Program\\command"

key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

reg.SetValue(key, '', reg.REG_SZ, 'Edit with Test Program')
#reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, r'C:\yourprogram.exe') set an icon

reg.SetValue(command_key, '', reg.REG_SZ, r'C:\Users\alext\Desktop\MyPython\JIDE\JIDE.exe')
