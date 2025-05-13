from cx_Freeze import setup, Executable

# ADD FILES
files = ['ui/icon.ico', 'ui/themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="ui/icon.ico"
)

# SETUP CX FREEZE
setup(
    name="SQL注入工具",
    version="1.0",
    description="基于PyQt的自动化SQL注入工具",
    author="dudu233,nini233,Astrid233,jingchuan",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
