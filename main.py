from DrissionPage import ChromiumPage #自动化模块 https://www.drissionpage.cn/get_start/installation
import requests
import ddddocr
from io import BytesIO


username = input("请输入你的教务系统学号：")
password = input("请输入你的教务系统密码：")
#数据库概论
#数据挖掘基础
classid = "M04396"
url='http://jwxt.cumt.edu.cn/jwglxt/jxrwbmgl/jxrwxmbm_cxJxrwxmbmIndex.html?gnmkdm=N2511&layout=default'
reason='对此门课程信息较为感兴趣，同时有一定基础'
#开浏览器
page = ChromiumPage()

######1
# #####进入教务系统教育项目报名
page.get(url)
# #####输入账号密码
page.ele('@@class=form-control@@name=yhm').input(username)
page.ele('@@class=form-control@@name=mm').input(password)
page.ele('@@class=form-control@@id=yzm').click()
# #####输入验证码
# #####截图验证码
img = page.ele('@name=yzmPic')
img.get_screenshot()
bytes_str = img.get_screenshot(as_bytes='png')
# ######用ddddocr识别
ocr = ddddocr.DdddOcr(beta=True)
img = BytesIO(bytes_str).read()
result = ocr.classification(img)
# #######输入验证码
page.ele('@id=yzm').input(result)
page.actions.click('@text()=登 录')

######2
######登录后

######点击重修补选类的报名
page.actions.click('@data-jxxmlbdm=1002')
#弹出报名说明，点击确定
page.actions.click('@data-loading-text=确 定')
#弹出报名选项 输入课程号
page.ele('@placeholder=按课程代码或课程名称查询').input(classid)
#点击搜索
page.ele('@style=float:right;').click()
#输入报名原因
page.ele('@id=bmyy').input(reason)
########自己选择课程
