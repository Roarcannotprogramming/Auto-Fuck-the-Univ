# Auto-Fuck-the-Univ

依赖:
- python 2.7
- hackhttp lastest

用法:
在目录中自己建立secrets.py文件

`secrets.py`:
``` python
username = 'your-username'
password = 'your-password'
```
运行 `python2 shot.py`
显示Success且输出时间和当前时间对的上则打卡成功

在vps上设置crontab定时任务

```
0 6,15,18 * * * "python2 /path/to/Auto-Fuck-the-Univ/shot.py > /dev/null"
```





## 更新
- Update 2020/2/19: 兼容湖北非湖北 只要打过卡 即可直接套脚本
