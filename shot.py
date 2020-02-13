import hackhttp
from request_message import *
import re
hh = hackhttp.hackhttp()
code, head, html, redirect, log_ = hh.http('https://passport.ustc.edu.cn/login', raw = raw3)

xsrf_token = re.findall(r'Set-Cookie: (XSRF-TOKEN=.*?;)', head)
l_session = re.findall(r'Set-Cookie: (laravel_session=.*?;)', head)
_token = re.search(r'<input type="hidden" name="_token" value="(.*?)">', html).group(1)

c_len = 475 - 40 + len(_token)

raw = '''POST /2020/daliy_report HTTP/1.1
Host: weixine.ustc.edu.cn
Content-Length: {3}
Cache-Control: max-age=0
Origin: http://weixine.ustc.edu.cn
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://weixine.ustc.edu.cn/2020/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cookie:  {0} {1}
Connection: close

_token={2}&now_address=1&gps_now_address=&now_province=420000&gps_province=&now_city=420100&gps_city=&now_detail=&body_condition=1&body_condition_detail=&now_status=2&now_status_detail=&last_touch_sars=0&last_touch_sars_date=&last_touch_sars_detail=&last_touch_hubei_date=&last_touch_hubei_detail=&last_cross_hubei_date=&last_cross_hubei_detail=&return_dest=2&return_dest_detail=%E5%8C%97%E4%BA%AC%E4%BF%A1%E5%B7%A5%E6%89%80&other_detail='''.format(''.join(xsrf_token), ''.join(l_session).strip(';'), _token, c_len)

code, head, html, redirect, log_ = hh.http('http://weixine.ustc.edu.cn/2020/daliy_report', raw=raw)

if code == 200:
    print('Success')
