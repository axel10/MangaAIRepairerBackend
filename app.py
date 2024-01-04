from flask import Flask,request
import tempfile
import base64
from PIL import Image
from io import BytesIO
import os
import sys
import datetime
import subprocess

def get_current_exe_path():
    if getattr(sys, 'frozen', False):  # 检查是否使用了pyinstaller打包
        # 获取当前exe所在的目录路径
        exe_path = sys.executable
        exe_dir = os.path.dirname(exe_path)
        return exe_dir
    else:
        # 如果没有使用pyinstaller打包，则返回当前脚本所在的目录路径
        return os.path.dirname(os.path.realpath(__file__))

def run_exe_command(command):
    # 使用subprocess.Popen执行FFmpeg命令
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
    # 等待命令执行完成
    process.wait()
    
    # 检查命令的输出和错误信息
    stdout, stderr = process.communicate()
    
    # 输出结果
    print(stdout.decode('utf-8'))
    




temp_dir = os.path.join(tempfile.gettempdir(),"my_manga_repairer")
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")

@app.route('/handle_img',methods=['POST'])
def handle_img():
    json = request.get_json()
    data = json["data"]
    level = int(json.get('level',2))
    data = data.split(',')[1]
    if not data:
        return "缺少数据"
    
    image_data = base64.b64decode(data)
    filename = str(datetime.datetime.now().timestamp())+'.jpg'
    image = Image.open(BytesIO(image_data))
    o_img_path = os.path.join(temp_dir,filename)
    # 保存图像到指定路径
    image.save(o_img_path)
    exe_path = os.path.join(get_current_exe_path(),"realesrgan-ncnn-vulkan-20220424-windows","realesrgan-ncnn-vulkan.exe")
    dist_img_path = o_img_path+"_dist.jpg"
    ffmpeg_command = f'{exe_path} -i {o_img_path} -o {dist_img_path} -s {level}'
    run_exe_command(ffmpeg_command)
    dist_data = image_to_base64(dist_img_path)
    
    os.remove(dist_img_path)
    os.remove(o_img_path)
    
    return dist_data

if __name__ == "__main__":
    app.run(port=31485)
