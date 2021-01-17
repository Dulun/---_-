import requests

proxies = {
    "http": "http://192.168.1.156:7890",
    "https": "https://192.168.1.156:7890"
}

def auto_checkin():
    
    session = requests.session()
    
    session.headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    url1 = "https://jike0.com/auth/login"
    
    data = {
        "email": "test@gmail.com",
        "passwd": "test",
        "code": ""
    }
    res_1 = session.post(url1, data=data)
    
    url3 = "https://jike0.com/user#"
    url4 = "https://jike0.com/user/checkin"
    response = session.get(url3)
    res_2 = session.post(url4)
    print(res_2.content.decode('unicode_escape'))

if __name__ == '__main__':

    auto_checkin()
