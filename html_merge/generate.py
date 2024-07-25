import os

# 定义根目录
root_directory = 'html_list'  # 替换为实际的根目录

# 定义输出HTML文件的名称
output_file = 'index.html'

# 获取根目录中的所有文件夹
subfolders = [f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))]

# 按ASCII顺序排序文件夹
subfolders_sorted = sorted(subfolders, key=lambda x: str(x))

# 创建HTML文件并写入内容
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write('<!DOCTYPE html>\n')
    outfile.write('<html lang="en">\n')
    outfile.write('<head>\n')
    outfile.write('    <meta charset="UTF-8">\n')
    outfile.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    outfile.write('    <title>Page Links</title>\n')
    outfile.write('</head>\n')
    outfile.write('<body>\n')
    outfile.write('    <h1>Page Links</h1>\n')
    outfile.write('    <ul>\n')

    # 逐个添加链接
    for folder in subfolders_sorted:
        outfile.write(f'        <li><a href="{root_directory}/{folder}/index.html">{folder}</a></li>\n')

    outfile.write('    </ul>\n')
    outfile.write('</body>\n')
    outfile.write('</html>\n')

print(f'HTML file {output_file} has been created with links to subfolders.')
