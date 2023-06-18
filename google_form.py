from selenium import webdriver
import datetime
  
# ct stores current time
ct = datetime.datetime.now()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='/Users/hlin/Documents/GitHub/Python_scripts/chromedriver', options=option)

# School form
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeKVa6AhY955GZrcL4cTq_rqAMBCNSvfGSlS1t3u7bniIrVdw/viewform")

# test form
# browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdG5yRhq_oQTvVHRRM6NSgx8TlyswB26cDD5cpRs_Oj7NvVng/viewform")

text_boxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radio_buttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelText")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submit_button = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# print("text:", text_boxes)
# print("radio: ", radio_buttons)
# print("submit:", submit_button)

text_boxes[0].send_keys("Jayden Lin")
text_boxes[1].send_keys("Henry Lin")
radio_buttons[0].click()

radio_buttons[2].click()
text_boxes[2].send_keys("henrylin2008@gmail.com")
text_boxes[3].send_keys("Henry Lin")
print("script has been executed successfully at:", ct)

submit_button.click()
browser.close()
