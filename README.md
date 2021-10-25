# Hollis 的马院考试助手

&emsp;&emsp;适用于黑龙江科技大学马克思主义学院智能化学习考试系统的简易搜题 Web API。

## 使用文档

&emsp;&emsp;为了使用马院考试助手，您的电脑需要装有 `Python 3`。以下操作均在 Windows 平台上脚本所在目录进行。

&emsp;&emsp;使用 `Fiddler` 抓取试题数据（具体方法不阐述，要一步一步讲明白太费劲儿了）并整理——提取 `text` 部分，使用 `"` 替换 `\"`，使用 `\` 替换 `\\`，去除试题以外的信息，并将单选、多选、判断等多种类型的试题聚合在一起，以 `UTF-8` 编码保存为 `input_学科.json` 文件，存放于 `inputs` 子目录下。您可以参考本代码库下的文件以帮助自己理解格式要求。运行 `python .\tool.py` 命令， 工具脚本将自动生成适用于马院考试助手的 `data.json` 题库文件。

&emsp;&emsp;在启动马院考试助手之前，先安装 `Microsoft Visual C++ 14.0`，然后运行 `pip install -r requirements.txt` 以安装依赖项。为了在您自己的服务器上使用，请将 `myzxks_assistant.py` 文件中 `# @app.route('/myzxks-assistant/search', methods=['GET'])` 和 `# app.run(host='0.0.0.0', port=5000)` 两行取消注释，并将 `@app.route('/projects/myzxks-assistant/search', methods=['GET'], subdomain='apps')` 和 `app.config['SERVER_NAME'] = 'hollisdevhub.com:5000'` 两行注释掉。

&emsp;&emsp;运行 `python .\myzxks_assistant.py` 命令来启动马院考试助手，马院考试助手将加载题库文件并监听 HTTP GET 请求，完整的 URL 是 `http://您的主机:5000/myzxks-assistant/search?title=题目`。为了正常使用马院考试助手，您需要提供欲查找答案的试题的题目作为前文中提到的 `title` 参数。由于使用了 `fuzzywuzzy` 库，马院考试助手支持模糊搜索，因此具有一定的容错性，可在 `title` 参数具有少量拼写错误的情况下查找到正确答案，但您仍应提供合适的参数——只包含完整的题目——以获得最佳的匹配效果。

## 捷径

&emsp;&emsp;马院考试助手仅仅为一个简易搜题 Web API，配合 `FV悬浮球` 的“自定义任务”功能使用更加直观、方便和快捷。在 `FV悬浮球` 的 `任务分享平台` 搜索并安装 `USTH 马院考试搜题` 自动任务即可。

&emsp;&emsp;**换句话说，直接走这一步，您他妈基本上不用看前面那一整坨又臭又长的废话！我说“基本上”是因为您还是应该保证自动任务截取的内容只包含完整的题目。**

&emsp;&emsp;不过哪天我搭建的服务不再可用的话，您还是需要参考前面的内容，搭建一个您自己的服务，同时修改 `USTH 马院考试搜题` 自动任务的请求地址为您自己的地址。
