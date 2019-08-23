# coding: utf8
import sys,os
sys.path.append('../')
from src.image_emotion_gender_demo import exe_c
from src.age import age
from src.detect import detection

import os, base64
from flask import Flask, render_template, request
import json
from flask_cors import *
#flask和templates文件的分离，
#其实只要修改template_folder的路径既可
#其他falsk的原理文章：
#https://blog.csdn.net/qq_33910169/article/details/90729119
#https://blog.csdn.net/f704084109/article/details/80802822
app = Flask(__name__,static_folder='../flask-image-clipper-demo/static', template_folder='../flask-image-clipper-demo/templates')
CORS(app, resources=r'/*')
#文件上传文件夹, 相对于项目根目录, 请勿改动static/部分
IMAGE_FOLDER     = '../images/upload/'
UPLOAD_FOLDER    = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_FOLDER)

@app.route("/")
def index():
    return render_template("index-touch-clip.html")

#对头像图片上传进行响应
@app.route('/upload/', methods=['POST','OPTIONS'])
def upload():
    if request.form.get("action") == "add":

        data = request.form.get("picStr")
        action = request.form.get("moudle")
        imgdata=base64.b64decode(data)
        if action == "emotion":
           imgfile=os.path.join(UPLOAD_FOLDER, "emotion/upload.png")
        elif action == "age":
           imgfile = os.path.join(UPLOAD_FOLDER, "age/upload.png")
        elif action == "yolov3":
           imgfile = os.path.join(UPLOAD_FOLDER, "detect/upload.png")
        elif action == "emotion":
           imgfile = os.path.join(UPLOAD_FOLDER, "emotion/upload.png")

        file=open(imgfile, 'wb')
        file.write(imgdata)  
        file.close()

        if action == "emotion":
             Jsons=exe_c('../images/upload/emotion/upload.png')               #调用exe_c函数，返回json数据。

        # 判断字典是否为空
        # 在python里，{},[],()，等都等价于False！,
             data=""
             if Jsons[0]:
                 data=str(Jsons)
             else:
                 data='no _result'

             print(str(Jsons))
             #print(Jsons)
             return json.dumps(Jsons, ensure_ascii=False)

        elif action == "age":
            Jsons = age("../images/upload/age")  # 调用exe_c函数，返回json数据。
            data = ""
            if(Jsons[0]):
                data = str(Jsons)
            else:
                data = 'no _result'

            print(str(Jsons))
            # print(Jsons)
            return json.dumps(Jsons, ensure_ascii=False)

        elif action == "yolov3":
            Jsons = detection()  # 调用exe_c函数，返回json数据。
            data = ""
            if(Jsons[0]):
                data = str(Jsons)
            else:
                data = 'no _result'

            print(str(Jsons))
            # print(Jsons)
            return json.dumps(Jsons, ensure_ascii=False)

    #旧版可以使用jsonify新版本必须使用json.dumps(Jsons[0]['bound_box']['x']) ,ensure_ascii为中文
    #flask可以传字符串，还有字典，元组等类型
    #numpy的int64格式 必须转为本地int否则会抱错
    #json参数格式https://www.jianshu.com/p/cfbcd9f8691c

if __name__ == "__main__":
    app.run(host='192.168.2.106', port=5001, debug=True)