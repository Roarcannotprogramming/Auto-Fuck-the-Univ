from secrets import *
import urllib

raw3 = '''POST /login HTTP/1.1
Host: passport.ustc.edu.cn
Connection: close
Content-Length: {2}
Cache-Control: max-age=0
Origin: https://passport.ustc.edu.cn
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Referer: https://passport.ustc.edu.cn/login?service=http%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5
Cookie: lang=zh; uc=PB16120211; JSESSIONID=3E12B894BDE1237A2C7AF975C2B83FDA

model=uplogin.jsp&service=http%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin&warn=&showCode=&username={0}&password={1}&button='''.format(urllib.quote(username),urllib.quote(password), 120 + len(urllib.quote(username)) + len(urllib.quote(password)))


