call .\venv\Scripts\activate & pyinstaller -F app.py

xcopy .\realesrgan-ncnn-vulkan-20220424-windows dist\manga-ai-repairer-backend\realesrgan-ncnn-vulkan-20220424-windows /Y /E /H /C /I
copy ".\ע����޸�����װ��.bat" ".\dist\manga-ai-repairer-backend\ע����޸�����װ��.bat" /Y
move /y ".\dist\app.exe" ".\dist\manga-ai-repairer-backend\app.exe" 

tar.exe -a -c -f manga-ai-repairer-backend.zip "dist\manga-ai-repairer-backend"
pause