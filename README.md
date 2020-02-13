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
显示Success则打卡成功

在vps上设置定时任务
(`shot.py`文件中raw的POST数据结合自己情况修改 默认的是在武汉的)
