# battlin_self_site

Static archive site for topic pages, with simple Python utilities for:
- merging paginated source HTML into one valid page
- generating the root topic index page

## Project layout

- `html_list/`
  # battlin_self_site（中文说明）

  这是一个用于保存论坛帖子静态归档的小工具仓库，包含两个主要功能：
  - 将分页的帖子 HTML 合并为单页文档（用于离线阅读或保存）
  - 根据归档的帖子目录生成可搜索的首页索引

  ## 目录结构说明

  - `html_list/`：每个帖子一个文件夹，目录名为标题或摘要，内部包含 `index.html` 与 `resources/`（图片、CSS、JS）
  - `html_merge/readin/`：放置抓取下来的分页 HTML（例如 `1.html`, `2.html`, ...），供合并脚本使用
  - `html_merge/merge.py`：合并分页为单页的脚本（可配置输入目录、输出路径与标题）
  - `html_merge/generate.py`：扫描 `html_list/` 并生成根目录 `index.html`（带摘要与搜索）
  - `index.html`：生成后的站点首页，供静态部署使用

  ## 运行环境

  - Python 3.9 及以上（无需额外第三方库）

  ## 快速使用指南（在仓库根目录执行）

  1) 将分页 HTML 放入 `html_merge/readin/`，运行合并：

  ```bash
  python html_merge/merge.py \
    --input-dir html_merge/readin \
    --output-file html_merge/after_merge.html \
    --title "Combined Topic Title"
  ```

  说明：
  - `--input-dir`（或 `-i`）：包含分页 HTML 的目录
  - `--output-file`（或 `-o`）：合并后输出文件路径
  - `--title`（或 `-t`）：合并后页面的 HTML 标题

  2) 将合并后的单页和对应 `resources/` 拷贝到 `html_list/` 下的新文件夹（命名随意），然后生成根索引：

  ```bash
  python html_merge/generate.py \
    --root-dir html_list \
    --output-file index.html \
    --sort-by name \
    --title "Page Links"
  ```

  说明：
  - `--root-dir`（或 `-r`）：帖子文件夹所在根目录
  - `--output-file`（或 `-o`）：要生成的首页路径（通常为仓库根的 `index.html`）
  - `--sort-by`（或 `-s`）：可选 `name` / `mtime` / `date`

  3) 本地预览（在仓库根运行临时静态服务器）：

  ```bash
  python -m http.server 8000
  # 然后在浏览器打开 http://localhost:8000/index.html
  ```

  ## 注意事项与建议

  - 资源路径请使用正斜杠 `/`（不是 `\\`），以确保在不同平台和静态服务器上都能正确加载。
  - 目前每个帖子目录都包含一份 `resources/`，可能会造成重复存储。若想节省空间，可以考虑统一放置共享资源目录并修改 HTML 中的引用路径。
  - 归档内容可能包含用户个人信息、头像及互动数据。公开部署前请确认版权与隐私合规性，必要时增加免责声明或移除机制。

  ## 后续改进方向（可选）

  - 将重复 CSS/JS 去重，建立全局 `static/` 目录并统一引用
  - 增强首页搜索：高亮匹配、按标签筛选、分页加载（当条目变多时）
  - 提供一个脚本自动化把 `merge.py` 输出与 `resources/` 打包并放入 `html_list/` 的新主题目录

  如果你希望，我可以把这些改进按优先级逐步实现并提交到仓库。当前我已更新并生成了可视化首页预览，文件： [index.html](index.html#L1)。

  - each topic folder contains `index.html` and `resources/`
