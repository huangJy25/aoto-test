import json
from common.request_utils import RequestUtils
import pytest
import requests
import time

class TestApi:
    def test_create_new_pet(self):
        url = "https://petstore.swagger.io/v2/pet/"
        headers = {
            "Content-Type": "application/json"
        }
        datas = {
            "id": 256,
            "category": {
                    "id": 256, "name": "dog"},
            "name": "wusong",
            "photoUrls": ["https://wx3.sinaimg.cn/mw690/008kPtkmgy1hw1qp8wa1cj31401hc7bf.jpg"],
            "tags": [{"id": 256, "name": "songzi"}],
            "status": "available"
            }
        res = RequestUtils().all_send_request(method = "post", url = url, json = datas)
        time.sleep(3)
        # print(res.json())


    def test_find_pet_by_id(self):
        url = "https://petstore.swagger.io/v2/pet/2"
        res = RequestUtils().all_send_request(method = "get", url = url)
        result = res.json()
        assert res.status_code == 200
        # print(res.json())

    def test_find_pet_by_status(self):
        url = "https://petstore.swagger.io/v2/pet/findByStatus"
        datas = {"status" : "sold"}
        res = RequestUtils().all_send_request(method = "get", url = url, params = datas)
        result = res.json()
        # assert res.status_code == 200
        # print(res.json())

    def test_upload_pet_img(self):
        url = "https://petstore.swagger.io/v2/pet/256/uploadImage"
        datas = {"file" : open("D:\\test\\Python_test\\1.png","rb")}
        res = RequestUtils().all_send_request(method = "post", url = url , files=datas)
        result = res.json()
        print(res.json())

    def test_update_existing_pet(self):
        url = "https://petstore.swagger.io/v2/pet"
        datas = {
            "id": 256,
            "category": {
                    "id": 256, "name": "dog"},
            "name": "wusong123",
            "photoUrls": ["https://wx3.sinaimg.cn/mw690/008kPtkmgy1hw1qp8wa1cj31401hc7bf.jpg"],
            "tags": [{"id": 256, "name": "songzi"}],
            "status": "available"
            }
        res = RequestUtils().all_send_request(method = "put", url= url, json = datas)
        print(res.status_code)
        assert res.status_code == 200

    def test_update_pet(self):
        url = "https://petstore.swagger.io/v2/pet/"
        headers = {
            "Content-Type": "application/json"
        }
        datas = {
            "id": 256,
            "name": "wusong12345",
            "status": "sold"
            }
        res = RequestUtils().all_send_request(method = "post", url = url, json = datas)
        assert res.status_code == 200

    def test_delete_pet(self):
        pet_id = 256
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
        headers = {
            "api_key" : "special-key",}
        res = RequestUtils().all_send_request(method = "delete", url = url, headers = headers)
        assert res.status_code in [200, 204, 404]





