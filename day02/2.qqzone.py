# pgv_pvi=4126914560; RK=eGdvPs6qPo; tvfe_boss_uuid=de7e0cf0c33f3df4; ue_ts=1517483658; ue_uk=dbdca3fe0ef52c1ea169147957f8caf1; ue_uid=0395781fdf1b9e69bd011cade3683553; ue_skey=87a92f684763c7d92f91e72de64d3edf; LW_pid=cfd045befdcee22e3825846fd7b9213b; ptcz=e7377b9a7fb09b87f6c8d0074112b1e38b6ee533c41b83c14b9dff545abc2661; pgv_pvid=1895250863; pgv_pvid_new=_5bdc5163e8; o_cookie=1642899961; pac_uid=1_1642899961; QZ_FE_WEBP_SUPPORT=1; pt_235db4a7=uid=FUZ9wZst/a7BdUk5P7KFlw&nid=1&vid=Et9E0E9SLTXgYgZiH8FxVA&vn=1&pvn=1&sact=1535633067353&to_flag=0&pl=k8UJAw4nMQYqZb6bAZlRfA*pt*1535633027114; eas_sid=L1j5e4H1I9n9E0V187n1h7Y787; LW_uid=b1x5w4k2Z9V4M584O679y2l0j6; LW_sid=K125k4m9V5J4W2n1P3G6g7h5X2; __Q_w_s__QZN_TodoMsgCnt=1; uin=o1642899961; skey=@LRAWUfSwM; ptisp=ctc; p_uin=o1642899961; pt4_token=hkU2RkFX0zXy*78BQZj0Y4I9wE2upZWwjAfdz7M5-B0_; p_skey=HYYeKx8YUIoy3etyojFUYFk0XCPns2mF67dEMUebyg8_; Loading=Yes; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qz_screen=1536x864; pgv_info=ssid=s5824693181; qzmusicplayer=qzone_player_1642899961_1554174764498; cpu_performance_v8=29
from http import  cookiejar
import  urllib.request

cookies = cookiejar.CookieJar()
#
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

# http = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(cookie_handler)
hearders = {
    "Cookie":"x-stgw-ssl-info=7729ff9ad018eb24226a236058e7d5d9|0.110|1554204846.229|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|19000|h2|0; 1642899961_todaycount=0; 1642899961_totalcount=5216; pgv_pvi=4126914560; RK=eGdvPs6qPo; tvfe_boss_uuid=de7e0cf0c33f3df4; ue_ts=1517483658; ue_uk=dbdca3fe0ef52c1ea169147957f8caf1; ue_uid=0395781fdf1b9e69bd011cade3683553; ue_skey=87a92f684763c7d92f91e72de64d3edf; LW_pid=cfd045befdcee22e3825846fd7b9213b; ptcz=e7377b9a7fb09b87f6c8d0074112b1e38b6ee533c41b83c14b9dff545abc2661; pgv_pvid=1895250863; pgv_pvid_new=_5bdc5163e8; o_cookie=1642899961; pac_uid=1_1642899961; QZ_FE_WEBP_SUPPORT=1; pt_235db4a7=uid=FUZ9wZst/a7BdUk5P7KFlw&nid=1&vid=Et9E0E9SLTXgYgZiH8FxVA&vn=1&pvn=1&sact=1535633067353&to_flag=0&pl=k8UJAw4nMQYqZb6bAZlRfA*pt*1535633027114; eas_sid=L1j5e4H1I9n9E0V187n1h7Y787; LW_uid=b1x5w4k2Z9V4M584O679y2l0j6; LW_sid=K125k4m9V5J4W2n1P3G6g7h5X2; __Q_w_s__QZN_TodoMsgCnt=1; Loading=Yes; qz_screen=1536x864; uin=o1642899961; skey=@Qib6R8yPG; ptisp=ctc; p_uin=o1642899961; pt4_token=lWndMUTMU7Iwk1jUFtlBIhrgeF31*WJtSVF1m7yjYiM_; p_skey=FWVj-JYOdz2ItTqss*ZUiF4UxfzUPWkGVHapJYVYOkg_; qzmusicplayer=qzone_player_1642899961_1554204850162; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s3156366213; cpu_performance_v8=22",
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

}
url = "https://user.qzone.qq.com/1642899961/infocenter"
req = urllib.request.Request(url,headers=hearders)
response = opener.open(req)
print(response.read().decode())