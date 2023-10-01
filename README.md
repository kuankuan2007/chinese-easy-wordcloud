# 中文简易词云(chineseEasyWordcloud)

中文简易词云是一个Python库，旨在帮助初学者更轻松地制作中文词云。

**注意：** 请务必指定字体路径，否则默认字体无法正确显示中文

## 安装

你可以使用 `pip`命令来安装该库：

```
pip install chineseEasyWordcloud
```

## 使用方法

安装完成后，你可以在命令行中使用该库。运行以下命令查看可用选项：

```
chinese-wordcloud -h
```

## 示例

命令行示例：

```bash
chinese-wordcloud "你好呀，我是宽宽" -o output.png --font_path "path/to/your_chinese_font.ttf" --width 1920 --height 1080
```

**注意：** 在命令行中可以直接使用 ``-f file file file``来添加多个文件或者使用 ``-d dir ignored1 ignored2``

e.g.

```bash
chinese-wordcloud -f "path/to/your_files1.txt" "path/to/your_files2.txt" -o output.png --font_path "path/to/your_chinese_font.ttf" --width 1920 --height 1080
```

此命令会读取`path/to/your_files1.txt`和`path/to/your_files2.txt`中的内容并作为词云的输入文本

```bash
chinese-wordcloud -d "path/to/your_dir" ".git" -o output.png --font_path "path/to/your_chinese_font.ttf" --width 1920 --height 1080
```

此命令会读取`path/to/your_dir`中除去``.git``以外的所有文件并作为词云的输入文本

Python示例：

```python
import chineseEasyWordcloud

# 加载中文文本
text = "这是一段中文文本"

# 创建词云图像
chineseEasyWordcloud.generate(text, "wordcloud.png",font_path='path/to/your_chinese_font.ttf')
```

**注意：** 以下内容适合对词云有相对简单的自定义要求的朋友，小白直接运行``generate``函数或者``chinese-wordcloud``命令即可，大佬嘛。。。应该也不用看我这屎山库。

在 ``chineseEasyWordcloud.cut``中提供了一些常用的额外处理函数：

+ `cutChinese`用于中文分词
+ ``removeStopwords``用于去除停止词（过于常见但无意义的词，比如“你”，“的”等），默认使用 ``chineseEasyWordcloud.stopwords.getDefault()``的内容，也可以自定义
+ `removeWhiteSpace`用于去除空白内容，比如空字符串，空格等
+ `removeNonsenseCharacter`用于去除无意义的字符，比如标点符号，换行符等
+ `cutWordDefault`依次调用上述方法

同时，在 `chineseEasyWordcloud.easyWordcloud`中提供了一些生成词云的方法，

+ `countWords`统计词频
+ `generateWc`用于生成Wordcloud对象
+ `generate`（就是 ``chineseEasyWordcloud.generate``）用于生成Wordcloud对象并导出为文件

## 贡献

欢迎贡献！如果你发现任何问题或有改进建议，请在该项目的 GitHub 页面上提出 issue。

## 许可证

该项目基于 [MPL-2.0 协议](http://license.coscl.org.cn/MulanPSL2)。

[Gitee](https://gitee.com/kuankuan2007/chinese-easy-wordcloud) | [Github](https://github.com/kuankuan2007/chinese-easy-wordcloud) | [PyPI](https://pypi.org/project/chineseEasyWordcloud/) | [Docs](https://kuankuan2007.gitee.io/docs/docsPage/?name=chinese-easy-wordcloud)
