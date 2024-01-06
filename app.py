import time
from flask import Flask, request, send_file
import tempfile
import base64
from PIL import Image
from io import BytesIO
import os
import sys
import datetime
import subprocess
import logging
import threading
import tomllib

def get_current_exe_path():
    if getattr(sys, "frozen", False):  # 检查是否使用了pyinstaller打包
        # 获取当前exe所在的目录路径
        exe_path = sys.executable
        exe_dir = os.path.dirname(exe_path)
        return exe_dir
    else:
        # 如果没有使用pyinstaller打包，则返回当前脚本所在的目录路径
        return os.path.dirname(os.path.realpath(__file__))


try:
    with open(os.path.join(get_current_exe_path(),"pyproject.toml"), "rb") as f:
        data = tomllib.load(f)
        print('漫画网站画质AI修复脚本 后端程序')
        print("当前版本号："+data.get('tool').get('poetry').get('version'))
except Exception as e:
    pass



def run_exe_command(command):
    # 使用subprocess.Popen执行FFmpeg命令
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )

    # 等待命令执行完成
    process.wait()

    # 检查命令的输出和错误信息
    stdout, stderr = process.communicate()

    # 输出结果
    print(stdout.decode("gbk"))
    print(stderr.decode("gbk"))


temp_dir = os.path.join(tempfile.gettempdir(), "my_manga_repairer")

def delete_temp(token):
    o_img_path = os.path.join(temp_dir, token + ".jpg")
    dist_img_path = os.path.join(temp_dir,token+'.jpg_dist.jpg')
    os.remove(o_img_path)
    os.remove(dist_img_path)


if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
app = Flask(__name__)


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")


@app.route("/")
def hello():
    return "pong"


@app.route("/get_img")
def get_img():
    token = request.args.get("token")
    dist_img_path = os.path.join(temp_dir, f"{token}.jpg_dist.jpg")

    timer = threading.Timer(1, delete_temp, args=[token])
    timer.start()
    return send_file(dist_img_path, mimetype="image/jpeg")


@app.route("/handle_img", methods=["POST"])
def handle_img():
    json = request.get_json()
    data = json["data"]
    scale = int(json.get("scale", 4))
    data = data.split(",")[1]
    if not data:
        return "缺少数据"

    image_data = base64.b64decode(data)

    token = str(datetime.datetime.now().timestamp())

    filename = token + ".jpg"
    image = Image.open(BytesIO(image_data))
    o_img_path = os.path.join(temp_dir, filename)
    # 保存图像到指定路径
    image.save(o_img_path)
    exe_path = os.path.join(
        get_current_exe_path(),
        "realesrgan-ncnn-vulkan-20220424-windows",
        "realesrgan-ncnn-vulkan.exe",
    )
    dist_img_path = o_img_path + "_dist.jpg"
    esrgan_command = (
        f'"{exe_path}" -i {o_img_path} -o {dist_img_path} -s {scale} -f ext/jpg'
    )
    run_exe_command(esrgan_command)

    # dist_data = image_to_base64(dist_img_path)

    # os.remove(dist_img_path)
    # os.remove(o_img_path)

    return token


log = logging.getLogger("werkzeug")
log.setLevel(logging.WARNING)


if __name__ == "__main__":
    app.run(port=31485)
