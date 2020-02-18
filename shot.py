# -- coding:UTF-8 --
import hackhttp
import urllib
from request_message import *
import requests
import re
hh = hackhttp.hackhttp()
code, head, html, redirect, log_ = hh.http('https://passport.ustc.edu.cn/login', raw = raw3)


xsrf_token = re.search(r'Set-Cookie: (XSRF-TOKEN=.*?;)', head).group(1).strip(';')
l_session = re.search(r'Set-Cookie: (laravel_session=.*?;)', head).group(1).strip(';')
_token = re.search(r'<input type="hidden" name="_token" value="(.*?)">', html).group(1)
now_address = re.search(r'<input type="radio" name="now_address" checked value="(.*?)">', html).group(1)
gps_now_address = re.search(r'<input type="hidden" name="gps_now_address" id="gps_now_address" value="(.*?)">', html).group(1)
now_province = re.search(r'<input type="hidden" id="now_province_hidden" value="(.*?)">', html).group(1)
gps_province  = re.search(r'<input type="hidden" name="gps_province" id="gps_province" value="(.*?)">', html).group(1)
now_city = re.search(r'<input type="hidden" id="now_city_hidden" value="(.*?)">', html).group(1)
gps_city = re.search(r'<input type="hidden" name="gps_city" id="gps_city" value="(.*?)">', html).group(1)
now_detail = re.search(r'<textarea class="form-control" name="now_detail" id="now-detail" placeholder="请详细填写您所在的国家的位置，具体到国家、州、城市" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
body_condition = re.search(r'<select name="body_condition" id="body-condition" rel="#body-detail" class="form-control selectpicker">(.*?)</select>', html, re.DOTALL).group(1)
body_condition = re.search(r'<option value="(\d*?)" selected>', body_condition, re.DOTALL).group(1)
body_condition_detail = re.search(r'<textarea class="form-control" id="body-detail" name="body_condition_detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
now_status = re.search(r'<select name="now_status" id="body-status" rel="#body-status-detail" class="form-control selectpicker">(.*?)</select>', html, re.DOTALL).group(1)
now_status = re.search(r'<option value="(\d*?)" selected>', now_status, re.DOTALL).group(1)
now_status_detail = re.search(r'<textarea class="form-control" name="now_status_detail" id="body-status-detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
has_fever = re.search(r'<input type="radio" name="has_fever" value="(.*?)" checked>', html).group(1)
last_touch_sars = re.search(r'<input type="radio" name="last_touch_sars" value="(.*?)" checked>', html).group(1)
last_touch_sars_date = re.search(r'<input type="text" id="last1-date" name="last_touch_sars_date" value="(.*?)" class="datetimepicker form-control" placeholder="请选择日期">', html).group(1)
last_touch_sars_detail = re.search(r'<textarea class="form-control" id="last1-detail" name="last_touch_sars_detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
if now_province != '420000':
    last_touch_hubei = re.search(r'<input type="radio" name="last_touch_hubei" value="(.*?)" checked>', html).group(1)
    last_touch_hubei_date = re.search(r'<input type="text" id="last2-date" name="last_touch_hubei_date" class="datetimepicker form-control" value="(.*?)" placeholder="请选择日期">', html).group(1)
    last_touch_hubei_detail = re.search(r'<textarea class="form-control" id="last2-detail" name="last_touch_hubei_detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
    last_cross_hubei = re.search(r'<input type="radio" name="last_cross_hubei" value="(.*?)" checked>', html).group(1)
    last_cross_hubei_date = re.search(r'<input type="text" id="last3-date" name="last_cross_hubei_date" class="datetimepicker form-control" value="(.*?)" placeholder="请选择日期">', html).group(1)
    last_cross_hubei_detail = re.search(r'<textarea class="form-control" name="last_cross_hubei_detail" id="last3-detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
else:
    last_touch_hubei = ''
    last_cross_hubei = ''
    last_touch_hubei_date = ''
    last_touch_hubei_detail = ''
    last_cross_hubei_date = ''
    last_cross_hubei_detail = ''
return_dest = re.search(r'<input type="radio" name="return_dest" value="(.*?)" checked>', html).group(1)
return_dest_detail = re.search(r'<textarea class="form-control" name="return_dest_detail" id="mudidi-detail" rows="5">(.*?)</textarea>', html, re.DOTALL).group(1)
other_detail = re.search(r'<textarea class="form-control" name="other_detail" rows="5" placeholder="请输入其他情况说明">(.*?)</textarea>', html, re.DOTALL).group(1)

# print('xsrf_token: ' + xsrf_token)
# print('l_session: ' + l_session)
# print('_token: ' + _token)
# print('now_address: ' + now_address)
# print('gps_now_address: ' + gps_now_address)
# print('now_province: ' + now_province)
# print('gps_province: ' + gps_province)
# print('now_city: ' + now_city)
# print('gps_city: ' + gps_city)
# print('now_detail: ' + now_detail)
# print('body_condition:' + body_condition)
# print('body_condition_detail: ' + body_condition_detail)
# print('now_status: ' + now_status)
# print('now_status_detail: ' + now_status_detail)
# print('has_fever: ' + has_fever)
# print('last_touch_sars: ' + last_touch_sars)
# print('last_touch_sars_date: ' + last_touch_sars_date)
# print('last_touch_sars_detail: ' + last_touch_sars_detail)
# if now_province != '420000':
#     print('last_touch_hubei: ' + last_touch_hubei)
# print('last_touch_hubei_date: ' + last_touch_hubei_date)
# print('last_touch_hubei_detail: ' + last_touch_hubei_detail)
# if now_province != '420000':
#     print('last_cross_hubei: ' + last_cross_hubei)
# print('last_cross_hubei_date: ' + last_cross_hubei_date)
# print('last_cross_hubei_detail: ' + last_cross_hubei_detail)
# print('return_dest: ' + return_dest)
# print('return_dest_detail: ' + return_dest_detail)
# print('other_detail: ' + other_detail)


dic = {
    'xsrf_token': xsrf_token,
    'l_session': l_session,
    '_token': _token,
    'now_address': now_address,
    'gps_now_address': gps_now_address,
    'now_province': now_province,
    'gps_province': gps_province,
    'now_city': now_city,
    'gps_city': gps_city,
    'now_detail': now_detail,
    'body_condition': body_condition,
    'body_condition_detail': body_condition_detail,
    'now_status': now_status,
    'now_status_detail': now_status_detail,
    'has_fever': has_fever,
    'last_touch_sars': last_touch_sars,
    'last_touch_sars_date': last_touch_sars_date,
    'last_touch_sars_detail': last_touch_sars_detail,
    'last_touch_hubei_date': last_touch_hubei_date,
    'last_touch_hubei_detail': last_touch_hubei,
    'last_cross_hubei_date': last_cross_hubei_date,
    'last_cross_hubei_detail': last_cross_hubei_detail,
    'return_dest': return_dest,
    'return_dest_detail': return_dest_detail,
    'other_detail': other_detail,
    'last_cross_hubei': last_cross_hubei,
    'last_touch_hubei': last_touch_hubei,
}

url_dic = {k: urllib.quote(v) for k, v in dic.iteritems()}


s = '''_token={_token}&now_address={now_address}&gps_now_address={gps_now_address}&now_province={now_province}&gps_province={gps_province}&now_city={now_city}&gps_city={gps_city}&now_detail={now_detail}&body_condition={body_condition}&body_condition_detail={body_condition_detail}&now_status={now_status}&now_status_detail={now_status_detail}&has_fever={has_fever}&last_touch_sars={last_touch_sars}&last_touch_sars_date={last_touch_sars_date}&last_touch_sars_detail={last_touch_sars_detail}&last_touch_hubei_date={last_touch_hubei_date}&last_touch_hubei_detail={last_touch_hubei_detail}&last_cross_hubei_date={last_cross_hubei_date}&last_cross_hubei_detail={last_cross_hubei_detail}&return_dest={return_dest}&return_dest_detail={return_dest_detail}&other_detail={other_detail}'''.format(**url_dic)
url_dic['c_len'] = str(len(s))
url_dic['xsrf_token'] = xsrf_token
url_dic['l_session'] = l_session

if now_province == '420000':
    raw = '''POST /2020/daliy_report HTTP/1.1
Host: weixine.ustc.edu.cn
Content-Length: {c_len}
Cache-Control: max-age=0
Origin: http://weixine.ustc.edu.cn
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://weixine.ustc.edu.cn/2020/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cookie: {xsrf_token};{l_session}
Connection: close

_token={_token}&now_address={now_address}&gps_now_address={gps_now_address}&now_province={now_province}&gps_province={gps_province}&now_city={now_city}&gps_city={gps_city}&now_detail={now_detail}&body_condition={body_condition}&body_condition_detail={body_condition_detail}&now_status={now_status}&now_status_detail={now_status_detail}&has_fever={has_fever}&last_touch_sars={last_touch_sars}&last_touch_sars_date={last_touch_sars_date}&last_touch_sars_detail={last_touch_sars_detail}&last_touch_hubei_date={last_touch_hubei_date}&last_touch_hubei_detail={last_touch_hubei_detail}&last_cross_hubei_date={last_cross_hubei_date}&last_cross_hubei_detail={last_cross_hubei_detail}&return_dest={return_dest}&return_dest_detail={return_dest_detail}&other_detail={other_detail}'''.format(**url_dic)

else:
    raw = '''POST /2020/daliy_report HTTP/1.1
Host: weixine.ustc.edu.cn
Content-Length: {c_len}
Cache-Control: max-age=0
Origin: http://weixine.ustc.edu.cn
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://weixine.ustc.edu.cn/2020/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cookie: {xsrf_token};{l_session}
Connection: close

_token={_token}&now_address={now_address}&gps_now_address={gps_now_address}&now_province={now_province}&gps_province={gps_province}&now_city={now_city}&gps_city={gps_city}&now_detail={now_detail}&body_condition={body_condition}&body_condition_detail={body_condition_detail}&now_status={now_status}&now_status_detail={now_status_detail}&has_fever={has_fever}&last_touch_sars={last_touch_sars}&last_touch_sars_date={last_touch_sars_date}&last_touch_sars_detail={last_touch_sars_detail}&last_touch_hubei={last_touch_hubei}&last_touch_hubei_date={last_touch_hubei_date}&last_touch_hubei_detail={last_touch_hubei_detail}&last_cross_hubei={last_cross_hubei}&last_cross_hubei_date={last_cross_hubei_date}&last_cross_hubei_detail={last_cross_hubei_detail}&return_dest={return_dest}&return_dest_detail={return_dest_detail}&other_detail={other_detail}'''.format(**url_dic)

code, head, html, redirect, log_ = hh.http('http://weixine.ustc.edu.cn/2020/daliy_report', raw=raw)

if code == 200:
    print('Success')
