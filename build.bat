call .\venv\Scripts\activate & pyinstaller -F app.py

xcopy .\realesrgan-ncnn-vulkan-20220424-windows dist\manga-ai-repairer-backend\realesrgan-ncnn-vulkan-20220424-windows /Y /E /H /C /I
copy ".\注册表修复（安装）.bat" ".\dist\manga-ai-repairer-backend\注册表修复（安装）.bat" /Y
move /y ".\dist\app.exe" ".\dist\manga-ai-repairer-backend\app.exe" 

tar.exe -a -c -f manga-ai-repairer-backend.zip "dist\manga-ai-repairer-backend"
pause