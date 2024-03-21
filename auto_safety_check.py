import requests
import json
from bs4 import BeautifulSoup

safety_check_url = 'https://safety.mju.ac.kr/Safety/LabCheckDayly/Index?LabNo=39061'
login_page_url = 'https://sso1.mju.ac.kr/login.do?redirect_uri=http://safety.mju.ac.kr/sso/LoginCheck_SSO.aspx'
user_check_url = 'https://sso1.mju.ac.kr/mju/userCheck.do'
ajax_login_url = 'https://sso1.mju.ac.kr/login/ajaxActionLogin2.do'
sso_login_url = 'https://sso1.mju.ac.kr/oauth2/token2.do'
session_url = 'https://safety.mju.ac.kr/sso/SSO_OK.aspx?uid=82210002'
           
login_info = {"id":"82210002", "passwrd":"Ayongho_98"}
sso_login_info = {"user_id":"82210002", "user_pwd":"Ayongho_98"}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','Referer': login_page_url}
with requests.Session() as s:
    login_page = s.get(login_page_url, headers=headers)
    cookies = {"Cookie":login_page.headers['Set-Cookie'].split(';')[0]}
    print('처음 받은 쿠키 : ',cookies)

    print('userCheck.do\n')
    user_check = s.post(user_check_url, data=login_info, headers=headers, cookies=cookies)

    print('ajaxActionLogin2.do\n')

    ajax_login = s.post(ajax_login_url, data=login_info, headers=headers, cookies=cookies,
    allow_redirects=False)
    
    print('token2.do\n')
    sso_login = s.post(sso_login_url, data=sso_login_info, headers=headers, cookies=cookies,
    allow_redirects=False)
    token = {"Cookie":sso_login.headers['Set-Cookie'].split(';')[0]}

    print('Get Session\n')
    final_login = s.get(session_url, cookies=token, allow_redirects=False)
    print(final_login.headers['Set-Cookie'].split(';')[0])

    session = {'Cookie': sso_login.headers['Set-Cookie'].split(';')[0] + 
                final_login.headers['Set-Cookie'].split(';')[0]}

    safety_check = s.get('https://safety.mju.ac.kr/Safety/LabCheckDayly/Index?LabNo=39061', 
    cookies = session, allow_redirects=False)
    html = safety_check.text
    soup = BeautifulSoup(safety_check.text, 'html.parser')
    print(soup.input)
    
    check_cookies = {'Cookie':final_login.headers['Set-Cookie'].split(';')[0]+'headerLastSelectLabNo=39061'}
    check_data = {
        'LabNo': '39061',
'LabCheckNo': '0',
'AskDay': '2021-03-11 오전 12:00:00',
'Proper_1': 'on',
'ElementNo': '81',
'Proper': '1',
'Proper_1_81': '1',
'Comment': '',
'ElementNo': '82',
'Proper': '1',
'Proper_1_82': '1',
'Comment': '',
'ElementNo': '83',
'Proper': '1',
'Proper_1_83': '1',
'Comment': '',
'ElementNo': '84',
'Proper': '1',
'Proper_1_84': '1',
'Comment': '',
'ElementNo': '85',
'Proper': '1',
'Proper_1_85': '1',
'Comment': '',
'ElementNo': '86',
'Proper': '1',
'Proper_1_86': '1',
'Comment': '',
'Proper_2': 'on',
'ElementNo': '87',
'Proper': '1',
'Proper_2_87': '1',
'Comment': '',
'ElementNo': '88',
'Proper': '1',
'Proper_2_88': '1',
'Comment': '',
'ElementNo': '89',
'Proper': '1',
'Proper_2_89': '1',
'Comment': '',
'ElementNo': '90',
'Proper': '1',
'Proper_2_90': '1',
'Comment': '',
'Proper_3': 'on',
'ElementNo': '91',
'Proper': '1',
'Proper_3_91': '1',
'Comment': '',
'ElementNo': '92',
'Proper': '1',
'Proper_3_92': '1',
'Comment': '',
'ElementNo': '93',
'Proper': '1',
'Proper_3_93': '1',
'Comment': '',
'Proper_4': 'on',
'ElementNo': '94',
'Proper': '1',
'Proper_4_94': '1',
'Comment': '',
'ElementNo': '95',
'Proper': '1',
'Proper_4_95': '1',
'Comment': '',
'ElementNo': '96',
'Proper': '1',
'Proper_4_96': '1',
'Comment': '',
'ElementNo': '97',
'Proper': '1',
'Proper_4_97': '1',
'Comment':''
    }
    test = s.post('https://safety.mju.ac.kr/Safety/LabCheckDayly/CreateOnLineAjx', data=check_data,
    cookies=check_cookies)

    print(test.headers)
    print(test.status_code)
    print(test.text)
