import os
import requests
import time
import random
import string
from requests_toolbelt import MultipartEncoder

def getUserInfo():
    header={"Cookie":"_kh_d_guid=892466748f4544f5e6fcfea6074bf76b; lotus=CfDJ8Dq0dlIYuJNOgmJyXTgyxclwVdrWqIfgqvG-42_w84Nyx-9cLLKI_hhdtkOkvBFOkoh-OkHTb8FTkV0715e4AYup0EIL_hITIwxDPfUyBLyp0kXKz_xQkhR1lZl3HrepLWPfrpR5zpWFz9nOAoaKxXCMbfSvAw3Z_o2USsXzNYQlcPIcJZc2XMNbyERY02yx2R7C4seYq0LKhvHLqiSLukZE7A3gNdVjXOnzXe-vzjdrdXQhMuXcgHDbZzKGG6ZHVXJF_W_5k-OVB3_qAXOkDRF6n2WgXljTMUILlbk23sD_BKGB9DKw4ViDnveHJzpcf3Y-BA-wp14hRdeOp8RFsUYmqJEaDCXgB9uibtKjLeHWhfyifJRASWkD18Yg0DkDiSDNl2KwWgxPlZgJHPcZsxGVBtCo_J5DKQcPME-3r3cX7v_nFTCmb5IQbZsjp5_fKCbyBTJtoVWtG33hMMGw8oozxByYGe9YkUIlWljKog6OHwApz6fCC0HiNeHBPiAK3NBK6c_Wu9DAbN3pct3MFcC7EkUetp3ZrGft7qOiX4mMytWofr7wI4T4IUIA9PNDMDGE6WCqWxYvCp1EpV0uvlf4SNGWMp29XW8aJ3bm3JMu1mxHy7CA6F5IkpKkxddCvoYu6VLb3dPfHNJmEIdzHQf7OqxRU1vciUzvvHUU4suncQPcoqomnZq9Zoswf54N-eMXIPi28M_4KRzX8bNcAjN-uihmPITW3oMkPr2AA3QVEUlK3LDS8SZfPwCvZmnlGyJKmqQXnExQ3YoDkdWHpmg5BoXuD1Pr5LZpBKM5ORbcoZI2KagZj2JYVDCWAJx-5xCBmg5qdQbKlgqdZPFx8VHeiV9q3nz_KhFHYgqiT8t93EaW4pPPnZonVeXqCapugWX_g_Km1nxrcJIVDqTVuQXyEXVriY2haIpwDszt1zA__xvXnw2mBzIiNszzblbaJy3bXzGSeTYUiV2MO5ExOf-xnZH1uxwr1OR7Ry4U0BZJz4tP9kVhaGQcR3suhzuekoxdfm3-sRcqiic_QUiHQvVFpzTNgvmEp-PnceN6301HQA7Eo4W8xMlTymUBsrZlBytJlIC_uXTWUq_ULEcNmMveWX30DWxyt0WuH3jDqm34py8AC7D5pK4Ih0URPa5nVxh1xW6UY16nOQ0aYCJPVvb-_9QK4TxoevPtMzSmxf1XL1BnD0aFQt8HzSyvp3frvojcySKC7hZfD6Pa7miV_V3Y6-TRM4wbYOV4UKHX39PVM2DmLuHv-zTHcMrQbAFW_xMMXRYyu4RM_QzjUXAZqhq5_G5TFbaYuIdYRIb3xu69EirqOqwnNATS_4w_tPZ9Hlf1yI_to1i4ZnjKvHmLtpcdXdshCRuh03qXfwwkYNsf_6j8G7i7b3DFaFGpHHpJ_9M5vmQ52PT-liztubVZa0bcR1NElfdnoZV3kTx8ocA8IXXXUwl35ztr_Ybo3e-mBf1LBZ3gh98zEad8M6lYxORNkJ8LQtAvHgV-xm-eWWtafpTWVtekRb42tRINnibbP_0gKeFJxe6hX2oh4Sqf9WISB67isnFWXULTwurC6YkcqkHXoh0n_F9GxujwUZ_CMDUIjWspozPS3uNdL-EL6YiF9p5P7QkvXVht0NbkzrXq; _lt_sd=PwdfIiFSBSsbFh4VKQk8UDlRRGtFKFElQD8FWRM/PBEYWxxzS0RXJlgECgtnbHATeBYTIgIUaTldUlFbcWJiBWQCX2JXVAZgDkFYQXN0fhMnURUiDglYOV1SUVsjMGICZgJTYgYHAGlfFAlMdW4zBTUDAjdRVwcxXEZcQHVmYgFkBVFjAgcGZQhHXB1nKw==; __admUTMtime=1598859448; _kh_t_e_a_s=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnYXRld2F5MSIsImF1ZCI6WyJ3ZWJraW5naHViIiwid2Via2luZ2h1YiJdLCJyb2xlIjoibWVtYmVyIiwiZXhwIjoxNTk4ODYwMDczLCJpYXQiOiIyMDIwLTA4LTMxIDE0OjM3In0.glZaFd_fcxlRQKPNt4EvewRhyfInMgHxYksy2BAtaGM"}
    response = requests.post("https://lotus.vn/w/authenticate/getuserinfo",headers=header)
    metadata = response.json()["data"]
    #print(metadata)
    return {"user_id":metadata["user_id"],"sessionid":metadata["sessionid"],"type":metadata["type"]}

def gtk():
    header={"Cookie":"_kh_d_guid=892466748f4544f5e6fcfea6074bf76b; lotus=CfDJ8Dq0dlIYuJNOgmJyXTgyxclwVdrWqIfgqvG-42_w84Nyx-9cLLKI_hhdtkOkvBFOkoh-OkHTb8FTkV0715e4AYup0EIL_hITIwxDPfUyBLyp0kXKz_xQkhR1lZl3HrepLWPfrpR5zpWFz9nOAoaKxXCMbfSvAw3Z_o2USsXzNYQlcPIcJZc2XMNbyERY02yx2R7C4seYq0LKhvHLqiSLukZE7A3gNdVjXOnzXe-vzjdrdXQhMuXcgHDbZzKGG6ZHVXJF_W_5k-OVB3_qAXOkDRF6n2WgXljTMUILlbk23sD_BKGB9DKw4ViDnveHJzpcf3Y-BA-wp14hRdeOp8RFsUYmqJEaDCXgB9uibtKjLeHWhfyifJRASWkD18Yg0DkDiSDNl2KwWgxPlZgJHPcZsxGVBtCo_J5DKQcPME-3r3cX7v_nFTCmb5IQbZsjp5_fKCbyBTJtoVWtG33hMMGw8oozxByYGe9YkUIlWljKog6OHwApz6fCC0HiNeHBPiAK3NBK6c_Wu9DAbN3pct3MFcC7EkUetp3ZrGft7qOiX4mMytWofr7wI4T4IUIA9PNDMDGE6WCqWxYvCp1EpV0uvlf4SNGWMp29XW8aJ3bm3JMu1mxHy7CA6F5IkpKkxddCvoYu6VLb3dPfHNJmEIdzHQf7OqxRU1vciUzvvHUU4suncQPcoqomnZq9Zoswf54N-eMXIPi28M_4KRzX8bNcAjN-uihmPITW3oMkPr2AA3QVEUlK3LDS8SZfPwCvZmnlGyJKmqQXnExQ3YoDkdWHpmg5BoXuD1Pr5LZpBKM5ORbcoZI2KagZj2JYVDCWAJx-5xCBmg5qdQbKlgqdZPFx8VHeiV9q3nz_KhFHYgqiT8t93EaW4pPPnZonVeXqCapugWX_g_Km1nxrcJIVDqTVuQXyEXVriY2haIpwDszt1zA__xvXnw2mBzIiNszzblbaJy3bXzGSeTYUiV2MO5ExOf-xnZH1uxwr1OR7Ry4U0BZJz4tP9kVhaGQcR3suhzuekoxdfm3-sRcqiic_QUiHQvVFpzTNgvmEp-PnceN6301HQA7Eo4W8xMlTymUBsrZlBytJlIC_uXTWUq_ULEcNmMveWX30DWxyt0WuH3jDqm34py8AC7D5pK4Ih0URPa5nVxh1xW6UY16nOQ0aYCJPVvb-_9QK4TxoevPtMzSmxf1XL1BnD0aFQt8HzSyvp3frvojcySKC7hZfD6Pa7miV_V3Y6-TRM4wbYOV4UKHX39PVM2DmLuHv-zTHcMrQbAFW_xMMXRYyu4RM_QzjUXAZqhq5_G5TFbaYuIdYRIb3xu69EirqOqwnNATS_4w_tPZ9Hlf1yI_to1i4ZnjKvHmLtpcdXdshCRuh03qXfwwkYNsf_6j8G7i7b3DFaFGpHHpJ_9M5vmQ52PT-liztubVZa0bcR1NElfdnoZV3kTx8ocA8IXXXUwl35ztr_Ybo3e-mBf1LBZ3gh98zEad8M6lYxORNkJ8LQtAvHgV-xm-eWWtafpTWVtekRb42tRINnibbP_0gKeFJxe6hX2oh4Sqf9WISB67isnFWXULTwurC6YkcqkHXoh0n_F9GxujwUZ_CMDUIjWspozPS3uNdL-EL6YiF9p5P7QkvXVht0NbkzrXq; _lt_sd=PwdfIiFSBSsbFh4VKQk8UDlRRGtFKFElQD8FWRM/PBEYWxxzS0RXJlgECgtnbHATeBYTIgIUaTldUlFbcWJiBWQCX2JXVAZgDkFYQXN0fhMnURUiDglYOV1SUVsjMGICZgJTYgYHAGlfFAlMdW4zBTUDAjdRVwcxXEZcQHVmYgFkBVFjAgcGZQhHXB1nKw==; __admUTMtime=1598859448; _kh_t_e_a_s=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnYXRld2F5MSIsImF1ZCI6WyJ3ZWJraW5naHViIiwid2Via2luZ2h1YiJdLCJyb2xlIjoibWVtYmVyIiwiZXhwIjoxNTk4ODYwMDczLCJpYXQiOiIyMDIwLTA4LTMxIDE0OjM3In0.glZaFd_fcxlRQKPNt4EvewRhyfInMgHxYksy2BAtaGM"}
    response = requests.get("https://lotus.vn/w/a/gtk",headers=header)
    metadata = response.json()["data"]
    auth_key = getAuthentication(response.headers["set-cookie"])
    metadata["auth_key"] = auth_key
    #print(metadata)
    return metadata

def getAuthUserInfo(auth_key,sessionid,user_id):
    header={"Authorization":"Bearer "+auth_key,"session-id":sessionid}
    response = requests.get("https://webpub.lotuscdn.vn/api/webkinghub/kinghub-user/get-auth-userinfo?user_id="+user_id,headers=header)
    data = response.json()
    return data

def getAuthentication(cookie):
    init  = cookie.find("=")
    end = cookie.find(";")
    return cookie[init+1:end]

def getToken(auth_key,sessionid,user_id):
    header={"Authorization":"Bearer "+auth_key,"session-id":sessionid}
    response = requests.post("https://webpub.lotuscdn.vn/api/social/token",headers=header,data={"userId":user_id})
    data = response.json()
    print(data)
    return data

def kinghubPolicy(auth_key,api_key,sessionid,filename):
    header={"Authorization":"Bearer "+auth_key,"session-id":sessionid,"API-Authorization":api_key}
    response = requests.get("https://webpub.lotuscdn.vn/api/webkinghub/kinghub-policy?filename="+filename+"&convert=true",headers=header)
    data = response.json()
    print(data)
    return data

def generateFilename():
    ts = int(time.time()*1000)
    string = get_random_string()
    return str(ts)+"-"+string

def lotusAuth():
    auth_key = gtk()["auth_key"]
    user_data = getUserInfo()
    sessionid = user_data["sessionid"]
    user_id = user_data["user_id"]
    api_key = getToken(auth_key,sessionid,user_id)["access_token"]
    filename = generateFilename()+".mp4"
    print(filename)
    policy = kinghubPolicy(auth_key,api_key,sessionid,filename)["policy"]
    return {"policy":policy["encoded_policy"],"filename":filename,"signature":policy["signature"],"sessionid":sessionid,"api_key":api_key,"auth_key":auth_key}

def uploadAPI(filename,policy,signature,file):
    data = MultipartEncoder({"filename":filename,"signature":signature,"filedata":(file,open(file,"rb"),"video/mp4"),"policy":policy})
    #postdata = {"filename":filename,"signature":signature,"filedata":open(file,"rb"),"policy":policy}
    header = {"Content-Type":data.content_type,"Content-Length":"0","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    response = requests.post("https://mps.lotuscdn.vn/_/upload",headers=header,data=data)
    print(response.json())
    return response.json()

def kinghubFileInfo(filepath,api_key,auth_key,sessionid):
    header={"Authorization":"Bearer "+auth_key,"session-id":sessionid,"API-Authorization":api_key}
    response = requests.get("https://webpub.lotuscdn.vn/api/webkinghub/kinghub-fileinfo?filename="+filepath,headers=header)
    print(response.json())
    return response.json()


def get_random_string(length=10):
    letters_and_digits = string.ascii_lowercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def upload(file):
    auth = lotusAuth()
    filename = auth["filename"]
    policy = auth["policy"]
    signature  = auth["signature"]
    sessionid = auth["sessionid"]
    api_key = auth["api_key"]
    auth_key = auth["auth_key"]
    upload_details = uploadAPI(filename,policy,signature,file)
    video_info = kinghubFileInfo(upload_details["file_path"],api_key,auth_key,sessionid)
    return video_info

