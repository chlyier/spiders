#-*- coding:utf-8 -*-

import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge('msedgedriver.exe')

info = [{'title': '第一题  启示录的概论', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488574&amp;amp;idx=1&amp;amp;sn=b9d33bb71778c42103fbcc11afc50885&amp;amp;chksm=fcca637acbbdea6c1dc7b9e83316713480c23c70fae2a2fe5fd50970003f0e738653260cae0f&amp;amp;scene=21#wechat_redirect'}, {'title': '第二题  启示录特加的序言', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=3&amp;amp;sn=d1975a4db42da89aa61cfbe9e4acc788&amp;amp;chksm=fcca7e3fcbbdf72958d89120f02f5c890a95cb2b620d86c47c461f59b3fe084d0091726e50ab&amp;amp;scene=21#wechat_redirect'}, {'title': '第三题  启示录书的开端格式（一）神圣的祝福', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=4&amp;amp;sn=83bf0410f1c276c9aa6151533b1c546e&amp;amp;chksm=fcca7e3fcbbdf729629119b014ff67c7ee5b2fb847cafb165270c71c4fe1ce5ad16d56a4a7cc&amp;amp;scene=21#wechat_redirect'}, {'title': '第四题  启示录书的开端格式（二）感恩和颂赞', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=5&amp;amp;sn=73a541eaedbc8eb81d1f33b9adde12e6&amp;amp;chksm=fcca7e3fcbbdf729230860af3faf5c3f809d0512a4c8dc8c68e4eea7ec8e5ab37c2f3080bd19&amp;amp;scene=21#wechat_redirect'}, {'title': '第五题  启示录书的开端格式（三）两个重大宣告', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=6&amp;amp;sn=e41c75e783c2c36c6f79c762df0fa97c&amp;amp;chksm=fcca7e3fcbbdf729b48da3a86e72527186b6cd87f95664319de747f79870a29d7f12faf73451&amp;amp;scene=21#wechat_redirect'}, {'title': '第六题    基督荣耀显现的异象（一）──约翰的自荐和见异象的地点时间', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=7&amp;amp;sn=e2622da9df52650ac436ca47d178d2b5&amp;amp;chksm=fcca7e3fcbbdf7293b3b56eeb9da2b6e2dc7003b905545d891ec72246cdb8d73b1a00138ebda&amp;amp;scene=21#wechat_redirect'}, {'title': '第七题  基督荣耀显现的异象（二）──基督的荣耀现显', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=1&amp;amp;sn=ba17ac30cef51353cb08ca657bda60e3&amp;amp;chksm=fcca7ed3cbbdf7c57e16a63e58e7150b62c43bd7ecdb5df578e1163e8c452e866e6eec2f7d09&amp;amp;scene=21#wechat_redirect'}, {'title': '第八题  基督荣耀显现的异象（三）──基督对约翰的慰勉和指示', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=2&amp;amp;sn=cb2cbe7d72244c7ca27d117955bfbc7f&amp;amp;chksm=fcca7ed3cbbdf7c5517a54c48b2b4f350c5ad25e2d77fa7ae8d87efae74bf4b19620180a626b&amp;amp;scene=21#wechat_redirect'}, {'title': '第九题  基督给七教会书信的总论', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=3&amp;amp;sn=87ea0d7c253063c30e653f6e73850965&amp;amp;chksm=fcca7ed3cbbdf7c55a858b5ffd5c41dfefe9bd14e1e40547151b68b8ae9bee2e57e509048bd3&amp;amp;scene=21#wechat_redirect'}, {'title': '第十题  基督给以弗所教会的书信', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=4&amp;amp;sn=d0308659314ce0f2645c31ec159f7660&amp;amp;chksm=fcca7ed3cbbdf7c5e192612920ef2d0bfcda3908f22e72e289a85d586f99c3e9d86a69f15e11&amp;amp;scene=21#wechat_redirect'}, {'title': '第十一题  基督给士每拿教会的书信', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=5&amp;amp;sn=7a5b7ac522ca42811eacce365d6ba280&amp;amp;chksm=fcca7ed3cbbdf7c5d3cfe6ce66c15f65d1cc1d8fd1d2514f9e9b2c9cf32c961648da0ad4a7d4&amp;amp;scene=21#wechat_redirect'}, {'title': '第十二题  基督给别迦摩教会的书信', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=6&amp;amp;sn=dd08de7709379b5e8e5d2d5d906b5198&amp;amp;chksm=fcca7ed3cbbdf7c5acabfa271de8c626c19e688c898c56f5960f5eb2373e1e3eb081bc41c019&amp;amp;scene=21#wechat_redirect'}, {'title': '第十三题  基督给推雅推拉教会的书信', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488574&amp;amp;idx=2&amp;amp;sn=f40ca5b1991ec5098ea058b95ed87e72&amp;amp;chksm=fcca637acbbdea6cdaf627159f909e5facb2ee5b5fc5f92275577a42951280662f6badd96a12&amp;amp;scene=21#wechat_redirect'}, {'title': '第十四题  基督给撒狄教会的书信', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485847&amp;amp;idx=8&amp;amp;sn=4806a9ddc9109f875bfc11c56bb14b29&amp;amp;chksm=fcca7ed3cbbdf7c57ac4dba4036e02f14bd9dc638210835387057d8ebef8cb5c9a05d9943a61&amp;amp;scene=21#wechat_redirect'}, {'title': '第十七题  七印书卷的序幕（一） ──上帝荣耀的宝座和创造颂', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=3&amp;amp;sn=5fe12eef3b93a63b014a01594888472f&amp;amp;chksm=fcca7d06cbbdf4105e6be33da2c3431d99270d9f982768844921cc036d6ef093fdc1f72e2188&amp;amp;scene=21#wechat_redirect'}, {'title': '第十八题  七印书卷的序幕（二）──羔羊取得七印书卷和救恩颂', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=4&amp;amp;sn=d14271f6fd0fef8206e58d15c69a5057&amp;amp;chksm=fcca7d06cbbdf4103d007071f8ba99742ce2f98a473192b2bed40e5f5f4397171af5695b5e20&amp;amp;scene=21#wechat_redirect'}, {'title': '第十九题  七印书卷的内容（第一、二印） ──福音的胜利和罗马的反扑', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=5&amp;amp;sn=09f58c01ed0092daf4c6ba4b364a80ec&amp;amp;chksm=fcca7d06cbbdf41078f7dd7d201709eb96d7ce4189741817afca1f972306660792467e8e52b2&amp;amp;scene=21#wechat_redirect'}, {'title': '第二十题  七印书卷的内容（第三、四印）──政教合一及其可怕的后果', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=6&amp;amp;sn=9aca8c884cfaf942b6996d3f45d56d50&amp;amp;chksm=fcca7d06cbbdf410144b57493bbbdfa319c836d6d94398e06c1c9d0ae65ef4303f68c06e80ce&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿一题  七印书卷的内容（第五印）──『灵魂』的呼冤和主的答复', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=7&amp;amp;sn=a0454aaf352e46e97000d8f5b20b08f2&amp;amp;chksm=fcca7d06cbbdf41069d762c08e2819bc1e5ef4ab9c87d116eba59bb4cbe2badc6f87df80daf3&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿二题  七印书卷的内容（第六印）──审判大日的预兆和来临', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486018&amp;amp;idx=8&amp;amp;sn=9a836e670fe68d9f37e419d5577705ca&amp;amp;chksm=fcca7d06cbbdf41063d0282595922357b4705762127119e00d649d08f4267a767a69ec46fb44&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿三题  执掌四方的风和加速盖印的异象（一）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=1&amp;amp;sn=cc1ded9de071ce943e4e10814497fa3c&amp;amp;chksm=fcca7d1ccbbdf40a729e7c9e51431cb266694515c0f6138266ce21d7959ca9e9b8fa43db7ee6&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿三题  执掌四方的风和加速盖印的异象（二）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=2&amp;amp;sn=729753bc4a00be2c5511b485d74a5716&amp;amp;chksm=fcca7d1ccbbdf40a50334ecd1c9d0e0812b3cd2c2f00e8342a3d2fbc21044e479ec4b6434822&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿四题  未来荣耀的展望和羔羊揭开第七印', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=3&amp;amp;sn=353c0b8976f516d14fe0112db05392e0&amp;amp;chksm=fcca7d1ccbbdf40a6cfb285b5009713250a45e67dd4e54890d77b1a414ad5ebd4432651ff59a&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿五题  七号筒的序幕', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=4&amp;amp;sn=f89826f2ec80f778aee17acd8615e9af&amp;amp;chksm=fcca7d1ccbbdf40ab193725731be9d7e8b4aa1f709d5d20725afe138310f8c61c63284caa1a3&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿六题  七号筒的吹响（一至四号）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=5&amp;amp;sn=4760db91858d342d09e6628bd020367c&amp;amp;chksm=fcca7d1ccbbdf40abf24a1b750b95ae4370a46b549c2b7a2b367b480de3cb1afcbdbf00711f7&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿七题  七号筒的吹响（第五号）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=6&amp;amp;sn=c8b7857c94cd2f724e13deaba4aacf36&amp;amp;chksm=fcca7d1ccbbdf40a5427172d3e41bacd3de86696575de5745ea255f1670174ed01fffef58abc&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿八题  七号筒的吹响（第六号）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=7&amp;amp;sn=3d64873a11a67ac1ce053f7ef1a32b61&amp;amp;chksm=fcca7d1ccbbdf40a96056380f2faa8cb72f401877eb714f8a14f3345e45e79c419f4e9f6d312&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿九题  七号筒的吹响（第七号）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486040&amp;amp;idx=8&amp;amp;sn=70084fe66e4b0f8dc0e7f2005e2dcfc7&amp;amp;chksm=fcca7d1ccbbdf40a46ac6519166247b73a01eb72dabd4923cb0d7c20401ca1fb475f4517c3a9&amp;amp;scene=21#wechat_redirect'}, {'title': '第三十题  关于复临运动的预言', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=1&amp;amp;sn=b4fb7dbd7160a6fb1aac4273d2f92f71&amp;amp;chksm=fcca7deecbbdf4f8e3c679338ffae938ff9c38b39fd2207ececa2ae8e791072a26954074b4a6&amp;amp;scene=21#wechat_redirect'}, {'title': '第三一题  关于『两个见证人』的预言', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=2&amp;amp;sn=ecb978c95c2acf9dd540e0d947bf7900&amp;amp;chksm=fcca7deecbbdf4f83567cb9efe86aab6f717be5e1976cd0bf1bfa4a2cbbfd821ea61ca8067bf&amp;amp;scene=21#wechat_redirect'}, {'title': '第三二题  大龙和妇人的异象（一）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=3&amp;amp;sn=6027be473558bd5c0a3164640048ea38&amp;amp;chksm=fcca7deecbbdf4f8e812dae249e9a58b15270489e43198be88a6c49b6c0151dc6b461d76f2c5&amp;amp;scene=21#wechat_redirect'}, {'title': '第三三题  大龙和妇人的异象（二）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=4&amp;amp;sn=ed9e4d3a9c20115c6680253923c9526b&amp;amp;chksm=fcca7deecbbdf4f89679e1c9cbf046728686c956d61f0992ac3ac24b9229fbaa471361afe0e9&amp;amp;scene=21#wechat_redirect'}, {'title': '第三四题  大龙和妇人的异象（三）', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=5&amp;amp;sn=22eaf76f6d303f2549f25ad8a0badd2c&amp;amp;chksm=fcca7deecbbdf4f8c149d30d19bc3bcf99f97ec1974d78bfa3c2d974d87aaf8f584c701bf648&amp;amp;scene=21#wechat_redirect'}, {'title': '第三五题  形状像豹的兽', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486122&amp;amp;idx=6&amp;amp;sn=dc471ba169ab3dc589810ac7f06ee538&amp;amp;chksm=fcca7deecbbdf4f83901ec4d2a0a25e9c5b337882ea4621297a5fb4a1b3dfdec0af98c4f5f2e&amp;amp;scene=21#wechat_redirect'}, {'title': '第三六题  两角如同羊羔的兽', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488624&amp;amp;idx=5&amp;amp;sn=d90a69cc802f3ed89e24b6f4d81fe232&amp;amp;chksm=fcca6334cbbdea22cc990e48c74c0d08d8fbb1e4ecbd9e6245abae091eb87bb3105e2cec8a70&amp;amp;scene=21#wechat_redirect'}, {'title': '第三七题  十四万四千人的荣耀展望', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486145&amp;amp;idx=1&amp;amp;sn=1023a3f739e510f653deef9212803315&amp;amp;chksm=fcca7d85cbbdf493c63f115e080d1a58f536c9bce5b9b3711d40cf20dc4f28712be74b3e69d6&amp;amp;scene=21#wechat_redirect'}, {'title': '第三八题  永远的福音和三天使警告的关系', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486145&amp;amp;idx=2&amp;amp;sn=9b3eaecb8d58c36c591374eb7d3be9a0&amp;amp;chksm=fcca7d85cbbdf4937c1fb4f76f071d27aaeecd4e34ce45529e824826e416674a96e46560f8b5&amp;amp;scene=21#wechat_redirect'}, {'title': '第三九题  第一位天使的警告', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486145&amp;amp;idx=3&amp;amp;sn=9d1c161f4da72fa6e17277780924098c&amp;amp;chksm=fcca7d85cbbdf493f9f34d897f6b1495f8ae3a223e8fda499be03f53c9e2bda2b63532bb43d6&amp;amp;scene=21#wechat_redirect'}, {'title': '第四十题  第二位天使的警告', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488624&amp;amp;idx=6&amp;amp;sn=e04ea936c99ca0dc86789b5ff920f3c4&amp;amp;chksm=fcca6334cbbdea228c17f8e092789c012ef6c1f0d94088c24f6741f53dedca1a990f9a80eaf2&amp;amp;scene=21#wechat_redirect'}, {'title': '第四一题  第三位天使的警告', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488624&amp;amp;idx=7&amp;amp;sn=91eb4b1af11e6b7954766f25d49a3175&amp;amp;chksm=fcca6334cbbdea22f2220990ae9700ce9d9812e0f398796da147245eb55c7a9689caa48b71ef&amp;amp;scene=21#wechat_redirect'}, {'title': '第四二题  有福的应许', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486145&amp;amp;idx=6&amp;amp;sn=15598ef8fcfee2e2be97d134b4b3e2c2&amp;amp;chksm=fcca7d85cbbdf49356fff57f1921618341659ed2610f7d0360dfd1676ad3635359b7c7f73887&amp;amp;scene=21#wechat_redirect'}, {'title': '第四三题  两种收割的异象', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486145&amp;amp;idx=7&amp;amp;sn=94b6e54a772046f1a3e5ca5f630838fc&amp;amp;chksm=fcca7d85cbbdf493ad2ebe1d4c40af35d89cb9bd58624f8db106201f0a203b1ef838e9941858&amp;amp;scene=21#wechat_redirect'}, {'title': '第四四题  关于十四万四千人', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=1&amp;amp;sn=081bde3668fba830ac4a490121a19759&amp;amp;chksm=fcca7da4cbbdf4b26430014878bdb15794506497fea63c07a42b52ec6b02403952bd2d6e902a&amp;amp;scene=21#wechat_redirect'}, {'title': '第四五题  七碗的异象', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=2&amp;amp;sn=b2c520ec9ec2118635c6aac8db722443&amp;amp;chksm=fcca7da4cbbdf4b274677b5f2a381abab735771ff4c6d238b1aac96d7d96bec738a7e2cfe652&amp;amp;scene=21#wechat_redirect'}, {'title': '第四六题  大淫妇和朱红色的兽', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247488624&amp;amp;idx=8&amp;amp;sn=6124379a266b348bc980c77e81ae657f&amp;amp;chksm=fcca6334cbbdea22d459d38d05cf6e67d25dd7575a0dcb3efbf813d932f84e470f69ec9f395f&amp;amp;scene=21#wechat_redirect'}, {'title': '第四七题  另一位天使的警告', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=4&amp;amp;sn=b3644e09efef675b3fd111c2745e9cac&amp;amp;chksm=fcca7da4cbbdf4b26705326b1a08cfe6057d364080d7e627f122e0471c04c4c6524d03f31dba&amp;amp;scene=21#wechat_redirect'}, {'title': '第四八题  巴比伦大城的刑罚', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=5&amp;amp;sn=75c84f3127b8468235a574ac1a400230&amp;amp;chksm=fcca7da4cbbdf4b2e50dfc54d396348e25fd52394babeba71e1d27e6c45e46c483ffc095bdd9&amp;amp;scene=21#wechat_redirect'}, {'title': '第四九题  赎民的称颂和羔羊的婚娶', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=6&amp;amp;sn=3196cfcfc06ccc3907f9bc575a215c41&amp;amp;chksm=fcca7da4cbbdf4b2588d218b83f09ab3920efe7203b6449fd3fb2e1905a3edb06f3d03f0367e&amp;amp;scene=21#wechat_redirect'}, {'title': '第五十题  基督复临时对罪人的毁灭', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486176&amp;amp;idx=7&amp;amp;sn=e51164ad05f07396bf47a481f394cc8f&amp;amp;chksm=fcca7da4cbbdf4b280801c84bbdc9901fa19e1d3a3628a0ff695b6ef51e8ebd5f51303fce700&amp;amp;scene=21#wechat_redirect'}, {'title': '第五一题  基督复临时对撒但的捆绑', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486189&amp;amp;idx=3&amp;amp;sn=f3b2cde9a55994ddd7a0744b8efee509&amp;amp;chksm=fcca7da9cbbdf4bf9490025150838b26dcb48a68b642cdb6699dea66d2be5b219578d0dc061e&amp;amp;scene=21#wechat_redirect'}, {'title': '第五二题  基督复临时对义人的赏赐', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486189&amp;amp;idx=4&amp;amp;sn=4a812730897b71dfd3c9a4a04ff235c7&amp;amp;chksm=fcca7da9cbbdf4bf1d5d8e4e6708d1eb44755fc532dea701d3d2cfb7febe7e5765ed023699a0&amp;amp;scene=21#wechat_redirect'}, {'title': '第五三题  一千年后撒但恶人的结局', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486189&amp;amp;idx=5&amp;amp;sn=50f2acb5b19abef354c4e3c37bff0fb4&amp;amp;chksm=fcca7da9cbbdf4bffb7de1df2295b745f3f78b406d2e095bc7b8b6d5392ea564d0971b786354&amp;amp;scene=21#wechat_redirect'}, {'title': '第五四题  一千年后义人永久的家乡', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486189&amp;amp;idx=6&amp;amp;sn=191f81b5d59a175df6ff98e6af6cc476&amp;amp;chksm=fcca7da9cbbdf4bf594d6eaf1b144b1d4c45bea4319b84253b23d5f90e97bbc25435631647c2&amp;amp;scene=21#wechat_redirect'}, {'title': '第五五题  书末的证言勉言和结语', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486189&amp;amp;idx=7&amp;amp;sn=291e72322ec3e1f087af7dcaa57784e4&amp;amp;chksm=fcca7da9cbbdf4bfe9e31438289a06ff2151145b6ed1495e36ab3d4d974f4a558a9a0999819f&amp;amp;scene=21#wechat_redirect'}]


def download_audio(id, m_dict):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

    index = 1
    for i in m_dict['audio_link']:
        data = requests.get(url=i, headers=header, timeout=20).content
        path = 'D:/zz/路光圣道/启示录研究与默想/' + str(id) + m_dict['title'] + str(index) + '.mp3'
        with open(path, 'wb') as fp:
            fp.write(data)
            print(id, '下载成功')
        index = index + 1

def get_audio_link(i):
    browser.get(i['url'])
    time.sleep(1)
    btn = browser.find_elements(By.XPATH, '//*[@id="audio_play_btn"]')
    for a in btn:
        a.click()
    time.sleep(2)
    html = browser.page_source
    ex = 'autoplay="" src="(.*?)"'
    audio_link = re.findall(ex, html, re.S)

    m_dict = {}
    m_dict['title'] = i['title']
    m_dict['audio_link'] = audio_link

    return m_dict

if __name__ == "__main__":
    id = 1
    for i in info:
        name_audio_dict = get_audio_link(i)
        print(name_audio_dict)
        download_audio(id, name_audio_dict)
        id = id + 1

