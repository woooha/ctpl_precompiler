#!/bin/sh

COMPILE = ""
ASP_ROOT = "/home/yangfan/envs/ecom/asp"
TPL_ROOT = "$ASP_ROOT/data/template"
ASP_RELOAD = "$ASP_ROOT/bin/reload"

for tpl_dir in "$TPL_ROOT/*";do
    if [ -d $tpl_dir ];then
        if [ -f "$tpl_dir/index.html" ];then
            $COMPILE "$tpl_dir/index.html" -o "$tpl_dir/page.html"
        fi
    fi
done

$ASP_RELOAD -p 8301
