import requests

class RequestUtils:
    sess = requests.session()
    def all_send_request(self,**kwargs):
        res = RequestUtils.sess.request(**kwargs)
        try:
            print("响应json", res.json())
        except:
            print("响应非json", res.text)
        return res