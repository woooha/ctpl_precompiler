ctpl_precompiler
================

ctpl 的语法实在是太他妈的坑爹啦！
主要有两条：

*对 include 的坑爹支持;
*不能自动的压缩去除多余的空格神马的，不能自动去除注释；

尼玛啊！为了让自己更爽一点，我必须赶紧吃点语法糖啊！！

尼玛尼玛尼玛！！！


How to use
================
1. 下载 ctpl_preocompiler  git clone https://github.com/woooha/ctpl_precompiler.git, 或者下载 zip 包：https://github.com/woooha/ctpl_precompiler/archive/master.zip
2. 解压
3. 执行 python ctpl_precompiler/tools/install.py -d "asp 程序的根目录路径",进行安装
4. 安装成功后，即可在模板中使用 $include header.html$ 形式的语法，将 header.html 放到模板当前路径中去即可
5. 开发时使用 index.html 进行开发，需要重新加载模板时使用 ASP_ROOT/bin/reload.py 进行加载，不需要制定端口，它会自动编译所有的模板，根据配置文件找到端口，并重新加载模板。
