title: 3days ONS 移植版
slug: pages/3days
allow_comment: True
jinja: true

<div>{% filter md %}{% include 'transplant.inc' %}{% endfilter %}</div>

首发：
[机锋](http://bbs.gfan.com/viewthread.php?tid=637440)
[智器](http://bbs.zhiqifans.com/thread-34893-1-1.html)

防止被HX，在自己这里留个备份……

---

3days 〜満ちてゆく刻の彼方で〜 是LASS在2004年发售的一款以猎奇为噱头以轮回为特点的纯爱系18XGalgame.（咳咳……我是不是太絮叨了……）（P.S.:11eyes是LASS继承3days的世界观制作的续作，也许更出名些……）

移植ONS版，菜B一只，蛋疼的随手作品，不知道发哪里好，所以就跟随炮神脚步了XD

注：ONS指onscripter，是galgame引擎nscripter的开源重制版，最大的优点是其可移植性，无论你是使用windows, linux, android, wm, ce, psp, pda, iphone, etc... 甚至诺亚舟学习机，都可以用它来跑游戏。

![血腥模式警告][血腥模式警告]

---

使用3月编译的新版ONS+最新3days脚本的时候，文字会消失，在向natdon君索要了新版ons源码测试后初步认定是新版ONS对textbtnwait也触发了erasetextwindow，如果你在使用新版ONS(3月22日及之后)，可以通过将脚本60.txt中

    amsp layer_pagebtn, %1, %2:vsp layer_pagebtn, 1

这句(请利用文本编辑器的查找功能)紧接着的下一行的`erasetextwindow 1`移动到`textbtnwait %BtnRes`(离的很近，当然仍然推荐查找功能)这句的下一行即可。

旧脚本放在下面的历史脚本更新中了。

---

## 故事简介

男主角 高梨亮 在10月16日早晨起床，在和青梅竹马女主角 藤见环 上学的路上发现了学校里出名的学姐的尸体，随后听说她是被无固定目标杀人犯分尸杀死；

10月17日两人又再次目睹同校女生跳楼自杀；

到10月18日晚上，在俩人缠绵之时，头戴面具的黑衣男子突然出现，亮的眼中最后目睹到的是，自己青梅竹马被残忍杀死的样子……

突然男主角惊醒，看到日历的日期是，10月16日……

是梦，还是真实？不断轮回的三日中，为了跳出悲惨的结末，男主角奋力寻找拯救她们的办法，最终将会在一次次死亡轮回中，凑齐打开真实之门的关键，揭开背后的真相……

---

## 游戏下载

* 主程序（炮神原帖里那个，现在已经有更新了，需要新版的请追[炮神原帖](http://bbs.gfan.com/android-327827-1-1.html)）[面包工坊的版本](http://portal.bakerist.info/node/251)是最新的。

* [脚本文件](http://pan.baidu.com/share/link?shareid=6972&uk=1124565063/)(2012/08/26 0.1314159版)

* [图像](http://pan.baidu.com/netdisk/singlepublic?fid=807912_3823193133)（168M）

* [字体文件](http://pan.baidu.com/netdisk/singlepublic?fid=807561_3474499221)（我的疏忽……一开始忘记了……虽然其实随便找一个中文字体改名为default.ttf就可以用的）：

    在SD卡上ons目录下新建一个目录（名字随便），将脚本文件解压进去，将图像文件复制进去，然后复制字体文件进去即可游戏。

* [音乐](http://pan.baidu.com/netdisk/singlepublic?fid=807912_2358954209)（50M）

* [语音](http://pan.baidu.com/netdisk/singlepublic?fid=807912_2452522568)（400M）

    如果需要音乐和人物语音，请将这两个文件命名为arc1.nsa, arc2.nsa放入游戏目录。

* [OP](http://pan.baidu.com/netdisk/singlepublic?fid=807912_511493750)（100M）

    PC上使用ONS运行时如果需要播放OP，请将这个文件放入游戏目录，实际上这个文件就是PC原版的OP文件。

    旧版Android版ONS不能播放mpeg所以拷了也没用……

    但是个人非常喜欢OP音乐，如果3days的BGM给50分的话，这个OP我给90分……

    这个OP的播放位置是最初的三天轮回结束的时候，可以玩完第一个三天后自己打开OP播放一下……

如果想在Windows上玩，请下载以下两个压缩文件中的任意一个，解压到游戏目录中，运行其中的exe文件即可：

[NScripter2.94chs](http://pan.baidu.com/netdisk/singlepublic?fid=807912_4285520317)
[ONScripter20100919(2.94)](http://pan.baidu.com/netdisk/singlepublic?fid=807912_1848000979)

如果想要800x600版，与顶楼不同的是[图片文件，请下载后重命名为`arc.nsa`](http://pan.baidu.com/netdisk/singlepublic?fid=807912_4266462850)和[脚本文件](http://pan.baidu.com/share/link?shareid=6971&uk=1124565063/)，其他的声音视频等是共通的。

800x600版主要目的是给PC的（还原PC版效果），也不排除大屏高分辨率Android平板使用。

祝各位good luck，有bug欢迎汇报，版本号0.131415中……

---

## 使用说明

（摘自[炮神原帖](http://bbs.gfan.com/android-327827-1-1.html)）

把游戏目录放到SD卡的ons目录下

右边的E代表ESC按键，S代表skip，O是啥不知道

摁E可以调出游戏的菜单

保存进度：用游戏菜单里的保存进度

退出：用游戏菜单里的退出， 或者摁home返回主屏幕再杀掉

---

## 移植说明

1. 原汉化版中有几个比较伤感的错误，1是存档可能读不了，2是进入真实之门后剧情不翻页……这也是我做这个的动力之一，这个ONS移植版不会有这种问题了……

2. 另外是不断轮回的三天中显然会有重复剧情，萌到翻的辉神评价：“以skip为主要流程”……所以为了方便轮回，我加入了skip段落功能，点击主界面的Setting按钮可以切换开启/关闭，开启后效果如下：

    ![跳过章节][跳过章节]

3. 这个游戏想玩通一个Good End至少需要死9次……如果想玩通全部GE，或者收集全CG那就更不知道要死几次了……百度百科里有攻略（P.S.:据说写攻略的家伙就是某个死了300多次才开启了真实之门的贴吧吧友……），没有耐心的朋友可以参考，我在我的测试机子上依照它和上面的skip功能完成了全结局……（注意，该攻略中“断末魔”结局的选项和汉化版有出入，攻略中“叫住”那项汉化版里翻译的是“大喊”）

参考：
[炮神原帖](http://bbs.gfan.com/android-327827-1-1.html)

感谢米炮的GBK版ONS，信米炮啥都有啊XD！

---

## 对比PC版截图

![时钟破碎对比](http://ldouhg.bay.livefilestore.com/y1pVOEtJrcnb1bLYQml5_NhbVovx7CdbBTsaK0xMb1m11yMBjp5BLAMCdHwL5XxPRoCNPgt5vtaCkoHqqDzPk1RyC6uqcmKbbhj/Screenshot-compare2.jpg?psid=1)

![美柚回想](http://public.bay.livefilestore.com/y1pyrd6Y4aY6lS-otR2aRga6EAYbeab894M2g_JgGgYj2uWnqttD4pHR792GXzbjEh2H17WukFkpf9UK-Ir1Zvb5Q/screenshot4.jpg?psid=1)

![ED](http://public.bay.livefilestore.com/y1pFVtmYvwn2jkxSLIErfvR9E2f5BrI1jz3whuTAPZvzgIMpZ0CPy_t1bOiy1u5MjeK2sV0OsQ1Prz-62iQWsRaFQ/screenshot11.png?psid=1)

![CGMode](http://public.bay.livefilestore.com/y1pPd0FlfPWIVsStBxf32ePAoM_txp0T_Q40q33uEMffhkfP3YQfshq58cwkElNYgicn9xuNlh3yPlXzthPI3OMEw/screenshot19.jpg?psid=1)

![右键菜单对比](http://public.bay.livefilestore.com/y1pUAa-KAUJJ6Wi4-jLVy2dZloe3dGWFExTWu9kJPPsYQRTFxxgFmEQ2Qzg2Ato4dFeQulAa_7zYLMVDSxLWZs_Fg/Screenshot.jpg?psid=1)

![存档对比](http://public.bay.livefilestore.com/y1puAXfdzJrMNFDeHoqGyb_lX6ON7Hi6LUMiNWlJqvFB91SUyPIYm9MKYnPNYIMCHHJ4Kux-0X0kY9xSVr_gzg1_g/Screenshot-3.jpg?psid=1)

---

## 历史脚本

[2月10日0.09b脚本](http://pan.baidu.com/netdisk/singlepublic?fid=807912_2788888868)

[2月20日0.11脚本](http://pan.baidu.com/netdisk/singlepublic?fid=807912_3901102827)

如果需要知道脚本是怎样生成的，以及改分辨率重新打包等问题，也许可以参考
[这里](http://pan.baidu.com/netdisk/singlepublic?fid=807912_1517196851)
（是0.09版本时候的了，也许不完全对新版有效，但参考价值还是有的……）

---

## 更新记录

已经补充上了字体文件，因为缺字体自动退出打不开游戏的朋友不好意思，可以看一下下载部分的更新（感谢archer1202君的提醒）。

2月9日更新，修正部分立绘错误，但因为会导致存档不兼容（每次更新都会如此），如果已玩一定时间，请斟酌……目前发现由此导致的错误点有一处，在10.txt中搜索`t_ko_01.img #07`，将#07改成#01即可。

2月10日更新，修正杀戮者章节的一个跳出错误，如果使用老版本发生这个错误，可以跳过该章节，或者查找10.txt中“越来越刺眼”这句话，把那行中多出的N多空格删掉。

2月20日更新脚本添加即时选择系统特效，添加选择对话框效果，添加时钟效果（感谢百度3days吧米老鬼君的提醒），调整立绘显示部分。

2月22日更新脚本添加Save/Load界面，完善右键菜单，修正一些细微的bug，流程图变为存档相关（即原PC版效果），完成EDStaff滚动动画，改善对nscripter的兼容度。
另，由于在一定程度上已比较接近于PC版原版效果，基本停止功能更新，主要以修复bug为主。

2月25/26日更新脚本完善文本框界面，对scene图标微调，对一些全屏光线效果模拟。

2月27日修正汉化版中后宫End处乱码bug，感谢百度3days吧whaleboss君的提醒。

3月1日细微调整至PC版效果。

2012/08/26 修正路线bug，感谢PyMO版移植者Smileの寂寞。


[血腥模式警告]: http://public.bay.livefilestore.com/y1pB-U87Rxp156uOm8ncxnkwLbKHgNMJlSM6fNlq3kv9r8UK-kjX0-MrY1JPwV8jKU_1238_IWGJEdyvI7fQ9b9Dw/screenshot2.jpg?psid=1
[跳过章节]: http://public.bay.livefilestore.com/y1prCFhnQzy7zyrgcKo0DApgTh_FNDMqDxjrGbHS-H9l-tmfmO6tq5AGyXi5jwM5sKFupwDT9Q14rxvugk1_QxK8g/screenshot17.jpg?psid=1
