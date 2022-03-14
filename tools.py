import requests
import re
import sys
from config import *
from lxml import etree


def GetCooike():
	user = Config()
	userName = user.Name()
	userPassword = user.Password()
	userAnswer = user.Answer()
	userProblem = user.problem
	userBot = user.bot

	cookies = {
	    'UTH_sid': 'TkPkyZ',
	}

	headers = {
	    'Host': 'www.t00ls.cc',
	    'Content-Length': '223',
	    'Cache-Control': 'max-age=0',
	    'Sec-Ch-Ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'Sec-Ch-Ua-Mobile': '?0',
	    'Upgrade-Insecure-Requests': '1',
	    'Origin': 'https://www.t00ls.cc',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-User': '?1',
	    'Sec-Fetch-Dest': 'document',
	    'Referer': 'https://www.t00ls.cc/login.html',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'zh-CN,zh;q=0.9',
	    'Connection': 'close',
	}

	# data = 'username=1148202106%40qq.com&password=0c76d11516d2367dac0b406070044e46&questionid=5&answer=Lenovo&formhash=60de9e9a&loginsubmit=%E7%99%BB%E5%BD%95&redirect=https%3A%2F%2Fwww.t00ls.cc%2Farticles-64795.html&cookietime=2592000'
	data = f'username={userName}&password={userPassword}&questionid={userProblem}&answer={userAnswer}&formhash=60de9e9a&loginsubmit=%E7%99%BB%E5%BD%95&redirect=https%3A%2F%2Fwww.t00ls.cc%2Farticles-64795.html&cookietime=2592000'

	response = requests.post('https://www.t00ls.cc/login.html', headers=headers, cookies=cookies, data=data,allow_redirects=False)
	# cookies = requests.utils.dict_from_cookiejar(response.cookies)
	cookies = response.headers['Set-Cookie'].replace('httponly,','')
	# print(response)
	print('读取到Cookies：',cookies)
	txt(cookies)

def txt(cookies):
	st = cookies.replace(';','\n').replace('=',':').replace(' ','')
	Packing(st)

def Packing(st):
	form = {}
	#正则获取k,v列表
	r = re.findall(r'(.*?):(.*?)\n', st)
	for i in r:
		#移除k,v前后空格
		form[i[0].strip()] = i[1].strip()
	print(form)
	print(type(form))
	fw = ['UTH_pmnum', 'UTH_activationauth', 'UTH_loginuser', 'domain', 'SameSite', 'path', 'expires']
	for i in fw:
		form.pop(i)
	cookies = form
	print('cookies封装完成：',cookies)
	hashform(cookies)

def hashform(cookies):
	headers = {
		'Host': 'www.t00ls.cc',
		'Connection': 'close',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'Accept': '*/*',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua-mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://www.t00ls.cc/members-profile-14558.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
	}

	response = requests.get('https://www.t00ls.cc/checklogin.html', headers=headers, cookies=cookies).text
	data = etree.HTML(response)
	href = data.xpath('/html/body/li[4]/a/@href')[0]
	hashform = href.replace('logging.php?action=logout&formhash=','')
	print('成功读取Hashform：',hashform)
	Sing(cookies, hashform)


def Sing(cookies,hashform):

	headers = {
	    'Host': 'www.t00ls.cc',
	    'Content-Length': '34',
	    'Sec-Ch-Ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Sec-Ch-Ua-Mobile': '?0',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Origin': 'https://www.t00ls.cc',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://www.t00ls.cc/members-profile-14558.html',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'zh-CN,zh;q=0.9',
	    'Connection': 'close',
	}

	data = f'formhash={hashform}&signsubmit=apply'

	response = requests.post('https://www.t00ls.cc/ajax-sign.json', headers=headers, data=data, cookies=cookies).text
	print('请求成功返回报文如下：',response)
	Send(response)

def Send(trx):

	sms = f'报告大王，Tools每日签到，已经轻松搞定啦，以下是响应报文，请大王过目\n\n{trx}\n'

	cookies = {
	    '__yjs_duid': '1_219cb8d82e6690e6221e848080c5ec711646630581910',
	}

	headers = {
	    'Host': 'api.bot.wgpsec.org',
	    'Sec-Ch-Ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'Sec-Ch-Ua-Mobile': '?0',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Sec-Fetch-Site': 'none',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-User': '?1',
	    'Sec-Fetch-Dest': 'document',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'zh-CN,zh;q=0.9',
	}

	params = (
	    ('txt', sms),
	)
	api = Config().bot
	url = f'https://api.bot.wgpsec.org/push/{api}'
	response = requests.get(url, headers=headers, params=params, cookies=cookies)




if __name__ == '__main__':
	GetCooike()