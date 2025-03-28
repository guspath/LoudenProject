from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="Louden Project",
    version="1.0",
    description="Louden app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables,
)
