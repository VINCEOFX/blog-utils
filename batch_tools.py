# 导入tkinter图形化用户界面标准库；导入re正则表达式模块
import tkinter as tk
import re
import os


# 定义一个名为 process_data 的函数，并在函数体中编写要执行的代码。
def process_data():
    with open('未处理/data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    urls = []
    for line in lines:
        match = re.search(r'(https?://\S+)', line)
        if match:
            url = match.group(1)
            title = re.sub(url, '', line).strip()
            urls.append((url, title))

    with open('已处理/data_url.html', 'w', encoding='utf-8') as f:
        for url, title in urls:
            link = f'<h3>{title}</h3>\n<p><a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></p>\n'
            f.write(link)


# 定义一个名为 images_url 的函数，并在函数体中编写要执行的代码。
def images_url():
    with open('未处理/img.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    urls = []
    for line in lines:
        match = re.search(r'(https?://\S+)', line)
        if match:
            url = match.group(1)
            title = re.sub(url, '', line).strip()
            urls.append((url, title))

    with open('已处理/images_url.txt', 'w', encoding='utf-8') as f:
        for url, title in urls:
            link = f'<h3>{title}</h3>\n<div class="gallery" contenteditable="false" data-is-empty="false"' \
                   f' data-translation="添加图像" data-columns="1"><figure class="gallery__item"><a href="{url}" ' \
                   f'data-size="5120x2880"><img src="{url}"></a></figure></div>\n'
            f.write(link)


# 创建一个 Tkinter 应用程序
app = tk.Tk()
app.title("VINCE工具箱")

# 获取屏幕的宽度和高度
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# 设置窗口的大小和位置
app_width = 700
app_height = 200
x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")

# 创建一个标签控件，显示提示消息
label = tk.Label(app, text="点击按钮执行操作", font=("Arial", 12))
label.pack(pady=10)

# 创建第一个按钮，用于处理数据
button1 = tk.Button(app, text="处理网盘URL", font=("Arial", 12), command=process_data)
button1.pack(pady=10)

# 创建第二个按钮，用于处理数据
button1 = tk.Button(app, text="处理图片URL", font=("Arial", 12), command=images_url)
button1.pack(pady=10)

# 创建"已处理"文件夹
if not os.path.exists('已处理'):
    os.mkdir('已处理')

# 创建"未处理"文件夹
if not os.path.exists('未处理'):
    os.mkdir('未处理')

# 创建data.txt用来存放所需处理的文本内容
with open('未处理/data.txt', 'w', encoding='utf-8') as f:
    f.write('#请在此处输入你要处理的文本内容')

# 创建data.txt用来存放所需处理的文本内容
with open('未处理/img.txt', 'w', encoding='utf-8') as f:
    f.write('#请在此处输入你要处理的文本内容')

# 运行 Tkinter 应用程序
app.mainloop()
