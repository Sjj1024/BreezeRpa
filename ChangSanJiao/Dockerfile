#基于的基础镜像
FROM python:3.9
 
#代码添加到code文件夹
ADD ./ /usr/src/app
 
# 设置app文件夹是工作目录
WORKDIR /usr/src/app
 
# 安装支持
RUN pip install --no-cache-dir -r requirements.txt 
 
CMD [ "python", "/usr/src/app/app.py" ]