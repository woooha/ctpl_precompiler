ctpl_precompiler
================

ctpl 的语法实在是太他妈的坑爹啦！
主要有两条：
+ 对 include 的坑爹支持;
+ 不能自动的压缩去除多余的空格神马的，不能自动去除注释；

尼玛啊！为了让自己更爽一点，我必须赶紧吃点语法糖啊！！

尼玛尼玛尼玛！！！


##下载

首先 `git clone https://github.com/woooha/ctpl_precompiler.git` 的到程序, 

或者下载 zip 包并解压：https://github.com/woooha/ctpl_precompiler/archive/master.zip

##安装
执行

    python ctpl_precompiler/tools/install.py -d "ASP_ROOT"

进行安装，会将几个脚本安装到 ASP_ROOT/bin 目录下, ASP_ROOT 为 ASP 程序根目录的路径。


##使用
安装后 ASP_ROOT/bin 目录下会多三个文件，reload.py, compile.py, Template.py

####reload.py
reload.py 是用来在开发时自动编译模板的工具,平常使用这个就可以。
reload.py 功能主要有：
+ 将 ASP_ROOT/data/template 下所有模板中的 index.html 预处理为 page.html
+ 从 ASP_ROOT/conf/asp.conf 得到RELOAD PORT
+ RELOAD 的模板
因此，执行过reload.py后，就会自动的执行编译和重载的过程，对开发来说应该是透明的。

####compile.py
compile.py 是具体执行将模版文件进行预处理并输出到指定位置的问题。
用法为：

    compile.py template_1.html[ template_2.html ...] [-o output.html]

compile.py会依次处理template_1.html 和 template_2.html，并最终输出到 output.html, 若不是用 -o 选项，则输出到 stdout 或者屏幕。


##支持什么？
安装成功后，即可在模板中使用 $include header.html$ 形式的语法，将 header.html 放到模板当前路径中去即可,在由 compile.py 预处理后，会自动将 header.html 的内容包含进去。