import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
#from selenuim.webdriver.chrome.options import Options

def get_data_group(group_name):
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }
    group_uri = server+group_name
    response = requests.get(group_uri, headers=headers)
    try:_resp = json.loads(response.text)
    except:print("lol:error")
    val=[]
    val.append(_resp['m2m:cin']['lt'])
    val.append(_resp['m2m:cin']['con'])
    val.append(group_name)
    data.append(val)
    return response.status_code, _resp

if __name__ == "__main__":
    # plt.ion()
    data=[]
    ymax=[]
    ymin=[]
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    print("running the program")
    driver = webdriver.Firefox(options=opts)
    driver.get("http://onem2m.iiit.ac.in:443/webpage/welcome/index.html?context=/~&cseId=in-cse")
    sleep(3)
    driver.find_element_by_tag_name("button").click()
    sleep(5)
    driver.find_element_by_xpath("//li/ul/li[38]").click()
    sleep(4)
    driver.find_element_by_xpath("//li/ul/li[38]/ul/li[2]").click()
    sleep(6)
    ele1 = driver.find_elements_by_xpath("//li/ul/li[38]/ul/li[2]/ul/*")
    print(len(ele1))
    lst1=[]
    for i in ele1:
       lst1.append(i.text)
    server="http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team36_TDS_monitering_for_drinking_water/node_1/"
    for i in lst1:
        get_data_group(i)
    values=[]
    with open('temp.txt','w') as f:
        f.truncate()
        # for k in range(100):
            # j= data[len(data)-100+k]
        for j in data:
            if(j[1] != "test_instance"):
                f.write("%s\n" % j[1])
                t = float(j[1])
                values.append(t)
    fig=plt.figure()
    plt.plot(values)
    plt.show()

        # sleep(10)
        
        # sleep(10)
        # plt.close()
        # print("ssss")
    # fig.savefig(out)
