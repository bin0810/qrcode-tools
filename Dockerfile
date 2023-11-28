# 导入基础镜像
From python:latest
# 声明工作目录
WORKDIR /qr_scan
# 复制资源至容器
COPY requirements.txt app.py ./
COPY static ./static
COPY templates ./templates
# 安装依赖
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 申请端口
EXPOSE 5000
# 启动Flask
CMD ["python", "app.py"]
