import requests
cookie = {}
raw_cookies = 'd_c0="AGDC4PeycQuPTglECFbiiHOkS9My5xJDTfQ=|1489388778"; _zap=d92c79dc-b976-4c3f-9e76-c9255fe75154; q_c1=40da86a4c65941aa803702749da1fcef|1504083657000|1489388778000; q_c1=40da86a4c65941aa803702749da1fcef|1506750265000|1489388778000; aliyungf_tc=AQAAALCXnFJpSgEA+drPPAWlS1enUjRJ; capsion_ticket="2|1:0|10:1507819159|14:capsion_ticket|44:MzJlNGQxNmM2YzRhNDAwNDk3MTI4MDJjYTc3MGY0NTQ=|047e870793034de99bee3bbb74e279644f49c497fa0c818d875cf517f38074ef"; r_cap_id="MzU1ZTlkMGExZDQ0NDRiNDljMzM3ZWZhZmQ3MGY5Yjc=|1507819186|1464c65022241546f62d4b09a85735979a8a3393"; cap_id="NTA4NzQyZmY1YTJmNGU1YWI4ODNlNzY1MDQwM2VhMjM=|1507819186|8666819409d1af682d2628bff067fdded12b30d4"; __utma=51854390.703952029.1498698300.1507548497.1507819757.17; __utmb=51854390.0.10.1507819757; __utmc=51854390; __utmz=51854390.1507819757.17.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|2=registration_date=20160726=1^3=entry_date=20170313=1; z_c0=Mi4xY3J4SkF3QUFBQUFBWU1MZzk3SnhDeGNBQUFCaEFsVk5BZzRIV2dBS0JTYVItQ0pFZHV5U2NNMTBNUEpCZHctdm1n|1507819778|83b5765005f9210e98c09784c92e05dde15da7af; _xsrf=2cbcf303-5dc1-4637-b6b8-deff9f05df3e'
for line in raw_cookies.split(';'):
    key,value = line.split("=", 1)
    cookie[key] = value
page = requests.get('https://www.zhihu.com/',cookies=cookie)
print(page.text)