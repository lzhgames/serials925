# -*- mode: python -*-

block_cipher = None


a = Analysis(['serials3.py'],
             pathex=['C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\Jason\\Desktop\\project\\python\\pyqt5\\serials3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='serials3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Jason\\Desktop\\project\\python\\pyqt5\\serials3\\res\\icon\\myicon.ico')
