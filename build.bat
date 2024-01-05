call .\venv\Scripts\activate
pyinstaller -F app.py

xcopy .\realesrgan-ncnn-vulkan-20220424-windows dist\realesrgan-ncnn-vulkan-20220424-windows /E /H /C /I
copy ".\注册表修复（安装）.bat" ".\dist\注册表修复（安装）.bat"
pause