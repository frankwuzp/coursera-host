# coursera-host

## 👀 背景

国内访问 coursera 网站奇慢，视频根本打不开，怀疑是 DNS 污染。

手动修改 hosts 文件后可以顺畅访问，于是就想：能否每天自动抓取 hosts ？最好每天自动更新 hosts 文件？

在交友网站一番查找，真有解决办法！

本项目基于 [github-host](https://github.com/jianboy/github-host) 的轮子，感谢！

## 🚀 修改 hosts 文件

### hosts 文件位置

各系统的 `hosts`文件位置不一，参考：

- Windows 系统：`C:\Windows\System32\drivers\etc\hosts`
- Linux 系统：`/etc/hosts`
- Mac（苹果电脑）系统：`/etc/hosts`
- Android（安卓）系统：`/system/etc/hosts`
- iPhone（iOS）系统：`/etc/hosts`

### 修改方法

记事本或 `Notspad++` 编辑本地 `hosts` 文件，Linux、Mac 带上`sudo` 编辑，将本仓库根目录中的 `hosts`文件内容复制进去。enjoy it！:)

## 📟 刷新 DNS缓存

修改完 `hosts`文件，一般来说是实时生效的，如未生效，`Windows`系统使用 `cmd命令行`执行：`ipconfig /flushdns`，Linux 下需执行 `sudo /etc/init.d/networking restart` 重启网络。

## 👨‍💻 进阶：自动更新

最近发现的开源神器 `SwitchHosts`，进入[网站主页](https://swh.app/zh/)按照说明安装即可，功能丰富，强烈安利！

本仓库的 `hosts`文件每日自动更新，将以下链接填入 `SwitchHosts`设置界面，即可同步更新！（建议刷新时间设为 1 小时）

`hosts` 文件：`https://raw.githubusercontent.com/frankwuzp/coursera-host/main/hosts`

## 💌 Ref

- [github-host](https://github.com/jianboy/github-host)
- [GitHub520](https://github.com/521xueweihan/GitHub520#readme)

## 📖 Changelog

- 211010 米斯特乌初稿

