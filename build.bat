call .\venv\Scripts\activate
pyinstaller -F app.py

xcopy .\realesrgan-ncnn-vulkan-20220424-windows dist\realesrgan-ncnn-vulkan-20220424-windows /E /H /C /I
copy ".\ע����޸�����װ��.bat" ".\dist\ע����޸�����װ��.bat"
pause