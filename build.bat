call .\venv\Scripts\activate & pyinstaller -F app.py -n manga_ai_repairer_backend

xcopy .\realesrgan-ncnn-vulkan-20220424-windows dist\manga-ai-repairer-backend\realesrgan-ncnn-vulkan-20220424-windows /Y /E /H /C /I
copy ".\ע����޸�����װ��.bat" ".\dist\manga-ai-repairer-backend\ע����޸�����װ��.bat" /Y
copy ".\pyproject.toml" ".\dist\manga-ai-repairer-backend\pyproject.toml" /Y
move /y ".\dist\manga_ai_repairer_backend.exe" ".\dist\manga-ai-repairer-backend\manga_ai_repairer_backend.exe" 

cd dist
tar.exe -a -c -f manga-ai-repairer-backend.zip "manga-ai-repairer-backend"
pause