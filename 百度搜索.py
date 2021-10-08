from selenium import webdriver
import time

driver = webdriver.Chrome()
#获取网址
driver.get("http://www.baidu.com")

#窗口最大化
driver.maximize_window()

#输入搜索关键字
driver.find_element_by_xpath("//*[@id = 'kw']").send_keys("java")

#点击搜索按钮
driver.find_element_by_xpath("//*[@id = 'su']").click()

#暂停5秒关闭
time.sleep(5)
driver.close()