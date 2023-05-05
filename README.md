# Hollis 的马院考试助手

&emsp;&emsp;适用于黑龙江科技大学马克思主义学院智能化学习考试系统的简易搜题 Web API。

## 使用文档

### Windows 部署

前置条件：

- Python；
- Microsoft Visual C++ 14.0（见 [疑难杂症](https://github.com/bianyukun1213/MYZXKSAssistant#%E5%AE%89%E8%A3%85-python-levenshtein-%E6%97%B6%E6%8A%A5%E9%94%99)）；
- Git；
- 网络代理（非必需）。

步骤：

1. 克隆本仓库代码：`git clone https://github.com/bianyukun1213/MYZXKSAssistant.git`；
2. 安装依赖项：`pip install -r requirements.txt`；
3. 启动助手：`python .\myzxks_assistant.py`。

&emsp;&emsp;查询 Url 是 `http://<主机>:8972/search?title=<题目>`。

### 容器部署

前置条件：

- 容器平台（以 Docker 为例）；
- 网络代理（非必需）。

步骤：

1. 拉取镜像：`docker push heyhollis/myzxks-assistant:latest`；
2. 运行容器：`docker run -v /<主机数据路径>:/ma_data -v /<主机日志路径>:/ma_log -p <主机监听端口>:8972 -e HTTP_PROXY=<网络代理地址>`。

&emsp;&emsp;此外，还可附加 `PUID`、`PGID`、`TZ` 等参数，具体见 `docker/Dockerfile`。

&emsp;&emsp;查询 Url 是 `http://<主机>:<主机监听端口>/search?title=<题目>`。

### 题目抓取、导入（Windows）

微信小程序：

1. 使用 Fiddler 抓取数据，具体方法不阐述；
2. 提取数据中的 `text` 部分，删去用户信息仅保留题目，将单选题、多选题及判断题合并为一个 JSON 文件，命名为 `input_<科目>.json`，具体数据格式见 `tools/inputs` 下的示例；
3. 运行 `tool.py` 整理数据（假设你已将工作目录切换至 `tools`）：`python .\tool.py`；
4. 将生成的 `output.json` 复制到 `ma_data` 目录并重命名为 `data.json`。

智慧树（知到）：

1. 登录智慧树网站，找到你的 `UUID`：在 Cookie 中找到包含 `exitRecod_` 字样的项目，`_` 后面的字符串就是 `UUID`；
2. 进入相应课程，从 Url 获取 `courseId`；
3. 运行 `tool_zhihuishu.py` 整理数据（假设你已将工作目录切换至 `tools`）：`python .\tool_zhihuishu.py <courseId> <UUID>`；
4. 将生成的 `from_zhihuishu/output_<courseId>.json` 复制到 `inputs` 目录并重命名为 `input_zhihuishu_<科目>.json`；
5. 同样运行 `tool.py` 整理数据，步骤不再阐述。

### Android 端使用

&emsp;&emsp;马院考试助手仅仅为一个简易搜题 Web API，Android 平台下的交互部分由“FV 悬浮球”的“自定义任务”功能使实现。

&emsp;&emsp;在 FV 悬浮球的任务分享平台搜索并安装 `USTH 马院考试搜题` 自定义任务，再安装 [简体中文识别库](https://github.com/bianyukun1213/MYZXKSAssistant#%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BB%BB%E5%8A%A1%E6%97%A0%E6%B3%95%E8%AF%86%E5%88%AB%E5%B1%8F%E5%B9%95%E4%B8%8A%E7%9A%84%E6%96%87%E5%AD%97) 即可。

&emsp;&emsp;使用前需填入查询 Url。

## 疑难杂症

### 安装 python-Levenshtein 时报错

&emsp;&emsp;先安装 Microsoft Visual C++ 14.0，然后再次尝试。如果仍然报错，安装 Windows 10 SDK（可与 Microsoft Visual C++ 14.0 一同在 [Visual Studio 2022 生成工具](https://visualstudio.microsoft.com/zh-hans/downloads/) 里安装），然后按照 [这里](https://blog.csdn.net/kaever/article/details/106526610) 记录的操作复制两个文件，再次尝试。

### 自定义任务无法识别屏幕上的文字

&emsp;&emsp;有些手机系统如 MIUI 会阻止 FV 悬浮球等第三方应用程序针对微信截图或共享屏幕，请放行。

&emsp;&emsp;除此之外，这是一个已知问题。USTH 马院考试搜题使用了 FV 悬浮球自带的光学识别功能，有些时候，它就是不好使（我也不知道为什么），因此我添加了手动输入题目的对话框，您输入题目关键字即可。

&emsp;&emsp;如果光学识别功能**始终**不好使，请检查 FV 悬浮球的 `设置`——`截图`——`自动文字识别` 项，确保 `类型` 设置为 `本地` 并启用了简体中文的文字识别库。
