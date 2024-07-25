import os
import re

# 定义HTML文件目录
directory = '.\\html_merge\\readin'  # 替换为实际的文件目录

# 定义合并后HTML文件的名称
output_file = 'combined.html'

# 获取目录中的所有HTML文件
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# 按文件名中的数字顺序排序
files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

# 创建或清空合并后的HTML文件
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write('<html>\n<head>\n<title>Combined HTML</title>\n</head>\n<body>\n')

    # 逐个读取HTML文件并写入合并后的文件
    for filename in files:
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
            content = infile.read()
            # 添加分隔符或标题来区分不同文件的内容
            outfile.write(f'<h2>{filename}</h2>\n')
            outfile.write(content + '\n')
    
    outfile.write('</body>\n</html>')

print(f'All HTML files have been combined into {output_file}')
