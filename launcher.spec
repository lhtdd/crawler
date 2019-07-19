# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['launcher.py',
                'E:\\workspace_py\\mo\\config\\crawler_params.py',
                'E:\\workspace_py\\mo\\crawler\\qiushibaike_crawler.py',
                'E:\\workspace_py\\mo\\crawler\\kaixinyixiao_crawler.py',
                'E:\\workspace_py\\mo\\crawler\\base_crawler.py',
                'E:\\workspace_py\\mo\\db\\lyao_db.py',
                'E:\\workspace_py\\mo\\db\\leisure.py'
                ],
             pathex=['E:\\workspace_py\\mo'],
             binaries=[],
             datas=[],
             hiddenimports=['apscheduler'],
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
          name='launcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
