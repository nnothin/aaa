from selenium import webdriver
import time

driver = webdriver.Chrome()
#获取文件
driver.get(r"D:\桌面\python自动化\day01\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()

#填写信息
driver.find_element_by_xpath("//*[@id = 'accountID']").send_keys("nnothin")
driver.find_element_by_xpath("//*[@id = 'passwordID']").send_keys("123456")
driver.find_element_by_xpath("//*[@id = 'areaID']").send_keys("北京市")
driver.find_element_by_xpath("//*[@id = 'sexID1']").click()
driver.find_element_by_xpath("//*[@value = 'spring']").click()
driver.find_element_by_xpath("//*[@value = 'winter']").click()

#上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\壁纸\70887.jpg")
time.sleep(5)

#弹窗
driver.find_element_by_xpath("//*[@id='buttonID']").click()
time.sleep(3)
driver.switch_to.alert.accept()

#暂停3秒关闭
time.sleep(3)
driver.close()


