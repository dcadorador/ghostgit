# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['file_copier.py'],
    pathex=[],
    binaries=[],
    datas=[('ghostgit.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='file_copier',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ghostgit.icns'],
)
app = BUNDLE(
    exe,
    name='file_copier.app',
    icon='ghostgit.icns',
    bundle_identifier=None,
)
