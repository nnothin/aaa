from selenium import webdriver
import time

driver = webdriver.Chrome()
#获取网址
driver.get("http://www.jd.com")

#窗口最大化
driver.maximize_window()

#输入搜索商品
driver.find_element_by_xpath("//*[@id = 'key']").send_keys("外星人")

#点击搜索按钮
driver.find_element_by_xpath("//*[@class ='button']").click()


# driver.switch_to_window(driver.window_handles[1])
# # driver.title
# driver.switch_to_window(driver.window_handles[2])
# # driver.title
#
# search_windows = driver.current_window_handle

# driver.find_element_by_link_text("外星人").click()
# driver.find_element_by_link_text("ALIENWARE 锐龙版m15 R5 15.6英寸高端游戏本8核R7 16G 512G RTX3050Ti 165Hz 高刷屏笔记本电脑1252B").click()


#网速过慢停10秒再进行跳转
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[1]/div/div[3]/ul/li[1]/div/div[3]/a/em").click()


# all_handles = driver.window_handles
#
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to_window(handle)
#         print('now register window!')
# /html/body/div[5]/div[3]/div/div[1]/div/div[3]/ul/li[1]/div/div[3]/a/em

# 暂停5秒关闭
time.sleep(5)
driver.close()