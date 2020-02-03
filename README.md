# OSINT_Spider.py
基于领英的企业用户名收集

1.访问：

https://cse.google.com/cse?oe=utf8&ie=utf8&source=uds&q=%E6%B5%8B%E8%AF%95&safe=off&sort=&cx=000470283453218169915:hcrzdwsiwrc&label=2&start=10%22

2.开启“检查元素“查看网络，输入关键字，例如查找“测试”公司：
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAdFg48Y6yXp6legJGraLCuMYW7tc0ic6N6pXv21E3Iu7SmPClUVxd7ow/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

3.得到一个链接，如下：

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZi9tW6bjm19FsMEb-XuQAsd:1576251273826&sort=&exp=csqr,cc&oq=%E6%B5%8B%E8%AF%95&gs_l=partner-generic.12...52375.53266.0.97396.4.4.0.0.0.0.376.653.1j2j0j1.4.0.gsnos%2Cn%3D13...0.887j325027j4j1...1j4.34.partner-generic..2.2.403.Fc17AmPhuQs&callback=google.search.cse.api1465
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAKjT0MhOB8LnFjicF0Ga9yhibPTmftWfwVmFTLGgn5JvwIBXWOkRKiaG3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
这里面参数q其实就是我们的关键字的URL编码，通过修改num参数的数值可以修改返回的信息数量，但是因为谷歌的限制，修改的再大一次也只能反回20条左右。

这个接口搜索的结果最多就10页。
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAXIpaJFm1kmluIkNNic9DyapyCftLS35rfuxnzDBcmSB1QLonaFsIeJQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这里经过测试，例如将num改为很大的数字，如10000，返回的条数是搜索结果的1、2两页的信息，所以如果要获取这里所有的结果只需要访问第1、3、5、7、9页，每次得到链接后都将num值改为很大的数字，再去直接访问链接即可下载对应的json信息：
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAoKryxrGMg0xsqKDc9oYUVibhIuWVL50K1V1OiawMtMUF3ZTNic0twOV3Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
复制这5个链接：

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZjRxvO1gXqnKXkr3WQB0uGx:1575988477361&sort=&exp=csqr,cc&oq=%E8%81%94%E6%83%B3&gs_l=partner-generic.12...0.0.1.620482.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0....34.partner-generic..0.0.0.&callback=google.search.cse.api12043

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&start=20&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZjRxvO1gXqnKXkr3WQB0uGx:1575988477361&sort=&exp=csqr,cc&callback=google.search.cse.api17269

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&start=40&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZjRxvO1gXqnKXkr3WQB0uGx:1575988477361&sort=&exp=csqr,cc&callback=google.search.cse.api12494

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&start=60&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZjRxvO1gXqnKXkr3WQB0uGx:1575988477361&sort=&exp=csqr,cc&callback=google.search.cse.api3259

https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-CN&source=gcsc&gss=.com&start=80&cselibv=8b2252448421acb3&cx=000470283453218169915:hcrzdwsiwrc&q=%E6%B5%8B%E8%AF%95&safe=off&cse_tok=AKaTTZjRxvO1gXqnKXkr3WQB0uGx:1575988477361&sort=&exp=csqr,cc&callback=google.search.cse.api15781

将这些链接里的num值修改为大数字，例如10000，然后进行访问即可下载对应的1到10页的搜索结果信息：
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAPCO1L6eaEIz8RAZGuSLqbbJDeBd8QhL0xztCmib33C0Cia5nFEeATMTQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
可以看到他们的大小都差不多，一个文件就是2个页面的搜索结果。
接下来要做的就是对信息的提取，通过对其中一个文件的分析，可以看到，用户的姓名都是出现在”fn”处，且不重复：
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAsjicxZicLAtNzYYp6MlKZQlBgdDssLnm9p35uxQF91U0maJKWNpYUNHw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
到这里目标就很明确了，将每个文件的”fn”后门的姓名提取出来，然后将中文转换成拼音即可得到用户名字典了。结果示例：每次下来基本300个左右。
![image](https://mmbiz.qpic.cn/mmbiz_png/tEspUSWeiaDSkFVx5lRAWGqnnFkpmHeOAc548ldQ4MUcZoKmHnXnKS6nPV06pSUnGia19MZMzgTd5wACveA5Eajw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

