# Hollis 的马院考试助手

&emsp;&emsp;适用于黑龙江科技大学马克思主义学院智能化学习考试系统的简易搜题 Web API。

## 使用文档

&emsp;&emsp;为了使用马院考试助手，您的电脑需要装有 `Python 3`。以下操作均在 Windows 平台上脚本所在目录进行，如果您用的是其他平台，那您指定能研究明白，不用我多哔哔了。

&emsp;&emsp;使用 `Fiddler` 抓取试题数据（具体方法不阐述，要一步一步讲明白太费劲儿了）并整理——提取 `text` 部分，使用 `"` 替换 `\"`，使用 `\` 替换 `\\`，去除试题以外的信息，并将单选、多选、判断等多种类型的试题聚合在一起，以 `UTF-8` 编码保存为 `input_学科.json` 文件，存放于 `inputs` 子目录下。您可以参考本代码库下的文件以帮助自己理解格式要求。运行 `python .\tool.py` 命令， 工具脚本将自动生成适用于马院考试助手的 `data.json` 题库文件。

&emsp;&emsp;在启动马院考试助手之前，先安装 `Microsoft Visual C++ 14.0`（下载地址参看 [疑难杂症](https://github.com/bianyukun1213/MYZXKSAssistant#%E7%96%91%E9%9A%BE%E6%9D%82%E7%97%87) 部分），然后运行 `pip install -r requirements.txt` 以安装依赖项。为了在您自己的服务器上使用，请将 `myzxks_assistant.py` 文件中 `# @app.route('/myzxks-assistant/search', methods=['GET'])` 和 `# app.run(host='0.0.0.0', port=5000)` 两行取消注释，并将 `@app.route('/projects/myzxks-assistant/search', methods=['GET'], subdomain='apps')` 和 `app.config['SERVER_NAME'] = 'hollisdevhub.com:5000'` 两行注释掉。

&emsp;&emsp;运行 `python .\myzxks_assistant.py` 命令来启动马院考试助手，马院考试助手将加载题库文件并监听 HTTP GET 请求，完整的 URL 是 `http://您的主机:5000/myzxks-assistant/search?title=题目`。为了正常使用马院考试助手，您需要提供欲查找答案的试题的题目作为前文中提到的 `title` 参数。由于使用了 `fuzzywuzzy` 库，马院考试助手支持模糊搜索，因此具有一定的容错性，可在 `title` 参数具有少量拼写错误的情况下查找到正确答案，但您仍应提供合适的参数——只包含完整的题目——以获得最佳的匹配效果。

## 啰嗦！根本不用那么费事儿

&emsp;&emsp;马院考试助手仅仅为一个简易搜题 Web API，**Android 平台**下配合 `FV悬浮球` 的“自定义任务”功能使用更加直观、方便和快捷。在 `FV悬浮球` 的 `任务分享平台` 搜索并安装 `USTH 马院考试搜题` 自定义任务即可。

&emsp;&emsp;对于 **iOS 平台**，使用 [USTH 马院考试搜题](https://www.icloud.com/shortcuts/818a16f6fefc432780de5c6a37c68d36) 快捷指令。快捷指令相较于自定义任务少了悬浮球、光学识别功能，使用时需手动输入题目。

&emsp;&emsp;**换句话说，直接走这一步，您他妈基本上不用看前面那一整坨又臭又长的废话！我说“基本上”是因为您还是应该保证自定义任务截取的内容只包含完整的题目；如果是 iOS 快捷指令，为了方便，可按顺序输入数个关键词，效果也不错。**

&emsp;&emsp;不过哪天我搭建的服务不再可用的话，您还是需要参考前面的内容，搭建一个您自己的服务，同时修改 `USTH 马院考试搜题` 自定义任务或快捷指令的请求地址为您自己的地址。

## 疑难杂症

### 安装 `python-Levenshtein` 时报错

&emsp;&emsp;先安装 `Microsoft Visual C++ 14.0`，然后再次尝试。如果仍然报错，安装 `Windows 10 SDK`（可与 `Microsoft Visual C++ 14.0` 一同在 [Visual Studio 2022 生成工具](https://visualstudio.microsoft.com/zh-hans/downloads/) 里安装），然后按照 [这里](https://blog.csdn.net/kaever/article/details/106526610) 记录的操作复制两个文件，再次尝试。

### `USTH 马院考试搜题` 无法成功识别屏幕中的文字

&emsp;&emsp;这是一个已知问题。`USTH 马院考试搜题` 使用了 `FV 悬浮球` 自带的光学识别功能，有些时候，它就是不好使（我也不知道为什么），因此我添加了手动输入题目的对话框，您输入题目关键字即可。

&emsp;&emsp;如果光学识别功能**始终**不好使，请检查 `FV 悬浮球` 的 `设置`——`截图`——`自动文字识别` 项，确保 `类型` 设置为 `本地` 并启用了简体中文的文字识别库。

### 助手没有返回答案，是不是服务器挂了

&emsp;&emsp;有可能。

&emsp;&emsp;如果是 **`FV 悬浮球` 的自定义任务**，编辑它并修改 `useAlternate` 变量为 `布尔值`——`真` 以切换至备用服务器，但不要指望备用服务器时刻都能用，因为那是我家里的设备（还请不要攻击，包括主服务器，那是阿里云便宜学生机）。

&emsp;&emsp;如果是 **iOS 平台的快捷指令**，~~**自求多福**。新冠病毒祸害人，我们已经封校大概一学期了，而我的 `二手 iPhone SE | 破损不堪` 此刻正静静地躺在家里的抽屉中，等我下学期再有马院考试的时候才会更新。~~ 修改请求地址为 `http://bianyukun1213.tpddns.cn:5000/myzxks-assistant/search?title=`。这是临时的解决方案，以后会更新快捷指令。

#### 可它两个服务器全都不好使

&emsp;&emsp;那一定是我跑路了。这个问题非常好解决——只要我不是删了代码库跑路，您就能 [自己搭一个](https://github.com/bianyukun1213/MYZXKSAssistant#%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3)，非常简单不是么？

### 在知到考试，可以用 `USTH 马院考试搜题` 吗

&emsp;&emsp;从原理上考虑是可以用的，但我不保证没有反作弊检测。

&emsp;&emsp;如果需要从知到导入题库（我假设您有能力执行接下来的操作），先登录智慧树网站，在 Cookie 中找到包含 `exitRecod_` 字样的项目，`_` 后面的字符串即为您的 `UUID`，先记下来，然后进入您要导出题库的课程，从 Url 获取 `courseId`，接下来运行 `tool_zhihuishu.py`，第一个参数为 `UUID`，第二个参数为 `courseId`，程序会自动爬取并在 `from_zhihuishu` 目录下生成 `output_<COURSEID>.json` 文件，拷贝这个文件到 `inputs` 目录并重命名为 `input_zhihuishu_学科.json`，运行 `tool.py` 生成题库文件。

&emsp;&emsp;实际上，对知到抓包可难多了，我用的所有手段都不怎么好使，最后能抓到 Url 也是碰巧，我无法保证以后还能导出知到的题库。😔
