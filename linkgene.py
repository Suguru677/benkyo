# -*- coding: utf-8 -*-

import pyperclip
link = input()

s_target = 'file/d/'
e_target = '/view'

s_idx = link.find(s_target) + len(s_target)
e_idx = link.find(e_target)

id = link[s_idx:e_idx]

code = f"<img src = \"http://drive.google.com/uc?export=view&id={id}\">"
pyperclip.copy(code)
print('クリップボードにコピーしました')
print(code)