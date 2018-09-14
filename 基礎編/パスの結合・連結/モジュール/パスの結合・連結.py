

import os


PROJECT_DIR = 'C:\python-izm'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))








PROJECT_DIR = 'python-izm'

print(os.path.join('C:', PROJECT_DIR, 'settings_dir', SETTINGS_FILE))

# ↑「(アルファベット一文字):」のみだと、区切りを入れて貰えない？




