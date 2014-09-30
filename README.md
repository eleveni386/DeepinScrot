DeepinScrot
===========

修改小邪兽的DeepinScrot


##截图工具的截图

![](http://eleveni386.7axu.com/image/deepin-scrot.png)

##说明

深度公司的原员工  **小邪兽**  的作品. 

感叹于QQ的截图工具的便利性, 苦于Linux desktop下没有一款能与之匹敌工具.

该工具做到了与QQ截图工具一样的便利性.


特性
------- 

1. 区域截图, 
2. 截图修改, 
3. 本地保存, 以及 保存到 黏贴板 

以上为 原版 功能, 本人新增了一项功能 图床分享

4. 图床分享, 默认为 本人的图床   

##安装要求

1. \>= python2.6
2. python-xlib
3. python-requests
4. xsel


##更改图床

用你喜欢的 编辑器 编辑 `src/sharepic.py` 文件

修改 `pic_bed = 'http://eleveni386.7axu.com/Image/'  ` 

为你自己的图床地址

