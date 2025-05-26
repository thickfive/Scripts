import requests
import execjs
from tqdm import tqdm

# 设置请求头: User-Agent 是必须的
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "origin": "https://www.douyin.com",
    "priority": "u=1, i",
    "range": "bytes=0-893456",
    "referer": "https://www.douyin.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}

def get_video_list():
    cookies = {
        "ttwid": "1%7CLYXfYUxzHPhL93-ZGIguyfpnwJ5EqWVCt5M-X00aecE%7C1708169703%7C425d801394ca6a3a517ac11d55025916f26cb45ec619f22f9eb197dd4f8cc758",
        "UIFID_TEMP": "f49b3a3d04522b6a12606cca90038531deb642c80ee0a8590fa7a5baabafd5dc9e9861d1110a655f59c2e042f3eb340b4392768409299b5f4e617aa4fb16381753a4211b926c817bf409c7bf7752c59b",
        "fpk1": "U2FsdGVkX185aJ4bOvKt64fKQbpvRNqqe6x5V4lgR1R2YteT0mw3Ye+qRM4rYjkmMHs5jzivKfGPIcnZlBydiQ==",
        "fpk2": "a8e10e23d98aa94a479ea34bd2af3cd2",
        "UIFID": "f49b3a3d04522b6a12606cca90038531deb642c80ee0a8590fa7a5baabafd5dcd648527d4ab7f32cb379c5962f9bea026dbdc68d8a704032fc645a1cf9c5c2dd2560a4ebc50ff1c09bc9e6c47fa2cf9ade56ca51c614fd457914d65e7485bebf29ca35bd3818029ff805f8c00fbc1c2081b5864f329fc4bdf76042d7d3f6b63b36f0499b1fad066dc5845999628735ce7c7091657d3b7071a7df253af0d18eb5",
        "xgplayer_user_id": "284604433553",
        "hevc_supported": "true",
        "bd_ticket_guard_client_web_domain": "2",
        "live_use_vvc": "%22false%22",
        "xgplayer_device_id": "77263178721",
        "d_ticket": "b61ef4beffe6c82292e6d13b4356a0c40e233",
        "passport_assist_user": "Cj0ogbT5CfcYyhq1dwTbCWCELSuXHTIvQQeY1m74xmGE_v3Pqt-G4B-4IElC0HDbjSNVGo6dH6Q0QAf84SmmGkoKPGUYgaX7lgo5J02IVGFbRYViEa85AgHjMDsyRuE9Upegw5PPInrvtkdWHBnbnYoG-ITfZ55zR3xGYA2gtBDWoukNGImv1lQgASIBA64ilZE%3D",
        "n_mh": "RqG1FAkrgei4XOZjUSXm7ftOzp_vdQJ0z6js_n4_qNQ",
        "login_time": "1739272152121",
        "uid_tt": "582969b9b9deeb272f0cffe7886b9f1e",
        "uid_tt_ss": "582969b9b9deeb272f0cffe7886b9f1e",
        "sid_tt": "4a5c04f2cfabd830dd3bde16f3a9bfc5",
        "sessionid": "4a5c04f2cfabd830dd3bde16f3a9bfc5",
        "sessionid_ss": "4a5c04f2cfabd830dd3bde16f3a9bfc5",
        "is_staff_user": "false",
        "SelfTabRedDotControl": "%5B%5D",
        "store-region": "cn-gd",
        "store-region-src": "uid",
        "SEARCH_RESULT_LIST_TYPE": "%22single%22",
        "s_v_web_id": "verify_m9cdtg4h_7rZImDdB_F0xZ_4bU1_Bc9X_afkoNTmvEaKG",
        "__security_mc_1_s_sdk_crypt_sdk": "40de3e9f-4b98-a86e",
        "passport_csrf_token": "1d692267163edc1b2dc79d9f3a87b600",
        "passport_csrf_token_default": "1d692267163edc1b2dc79d9f3a87b600",
        "__security_mc_1_s_sdk_cert_key": "5ab11ec6-416a-a789",
        "__security_mc_1_s_sdk_sign_data_key_web_protect": "bf0045f8-4318-b9ad",
        "__live_version__": "%221.1.3.646%22",
        "_bd_ticket_crypt_cookie": "58504ae00ff7c5c63264e00dd844d2ab",
        "sid_guard": "4a5c04f2cfabd830dd3bde16f3a9bfc5%7C1746864602%7C5184000%7CWed%2C+09-Jul-2025+08%3A10%3A02+GMT",
        "sid_ucp_v1": "1.0.0-KGQ4NWYzZWE5NDIxYmQ4Mzk4NThjYTFkMzQwOGZjZjcwZTZkMGU2MGMKGQjChM-umgMQ2pP8wAYY7zEgDDgGQPQHSAQaAmxxIiA0YTVjMDRmMmNmYWJkODMwZGQzYmRlMTZmM2E5YmZjNQ",
        "ssid_ucp_v1": "1.0.0-KGQ4NWYzZWE5NDIxYmQ4Mzk4NThjYTFkMzQwOGZjZjcwZTZkMGU2MGMKGQjChM-umgMQ2pP8wAYY7zEgDDgGQPQHSAQaAmxxIiA0YTVjMDRmMmNmYWJkODMwZGQzYmRlMTZmM2E5YmZjNQ",
        "dy_swidth": "1512",
        "dy_sheight": "982",
        "is_dash_user": "1",
        "publish_badge_show_info": "%220%2C0%2C0%2C1747851459518%22",
        "h265ErrorNumNew": "-1",
        "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAy2o0Zy5y-V2VjAxHCJ4csJnOqY71-1ZEwdF0fdaegRg%2F1748188800000%2F0%2F1748172011181%2F0%22",
        "download_guide": "%223%2F20250525%2F0%22",
        "douyin.com": "",
        "device_web_cpu_core": "8",
        "device_web_memory_size": "8",
        "strategyABtestKey": "%221748238777.603%22",
        "biz_trace_id": "b2aa4188",
        "volume_info": "%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D",
        "xg_device_score": "7.338377468011834",
        "__ac_nonce": "068340ac50065a65a7f4d",
        "__ac_signature": "_02B4Z6wo00f010WcpuwAAIDCbJg4kCsiO09FvKJAALlecwRxYf4mOPr40p3QcpkQdnUU22DdiONLUdQz8DQnKVAOEcDMqDUsepVcOhnB3n.xz600uW6QVQ.PPDlluvtmctS973DDtSo3.bSC8f",
        "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAAy2o0Zy5y-V2VjAxHCJ4csJnOqY71-1ZEwdF0fdaegRg%2F1748275200000%2F0%2F0%2F1748242295098%22",
        "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1512%2C%5C%22screen_height%5C%22%3A982%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22",
        "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSlEyNUlFWStZdDk4M1E1VFJwNUxVT0o2Vkx5VzFodmNjZ2NnOFBLci9LeWRidWRuSndsbkV1Wkpub1BwbjVxeWZCb0ZUWkhCRjdCWUFzb3pBRmNTdm89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
        "odin_tt": "e734f4fc0db92671a097b25de3e019165b92044a304387632e5f241aa7ad94669005aeb67ee6cd9dcbe8122dee3ad1000d93f191c674c8e6978fbc22e12e7189",
        "passport_fe_beating_status": "false",
        "IsDouyinActive": "true",
        "home_can_add_dy_2_desktop": "%220%22"
    }
    url = "https://www.douyin.com/aweme/v1/web/aweme/post/"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "sec_user_id": "MS4wLjABAAAAEKnfa654JAJ_N5lgZDQluwsxmY0lhfmEYNQBBkwGG98",
        "max_cursor": "0", # 控制分页
        "locate_query": "false",
        "show_live_replay_strategy": "1",
        "need_time_list": "1",
        "time_list_query": "0",
        "whale_cut_token": "",
        "cut_version": "1",
        "count": "10", # 控制数量
        "publish_video_strategy_type": "2",
        "from_user_page": "1",
        "update_version_code": "170400",
        "pc_client_type": "1",
        "pc_libra_divert": "Mac",
        "support_h265": "1",
        "support_dash": "1",
        "cpu_core_num": "8",
        "version_code": "290100",
        "version_name": "29.1.0",
        "cookie_enabled": "true",
        "screen_width": "1512",
        "screen_height": "982",
        "browser_language": "zh-CN",
        "browser_platform": "MacIntel",
        "browser_name": "Edge",
        "browser_version": "135.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "135.0.0.0",
        "os_name": "Mac OS",
        "os_version": "10.15.7",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
        "webid": "7336532942959478299",
        "uifid": "f49b3a3d04522b6a12606cca90038531deb642c80ee0a8590fa7a5baabafd5dcd648527d4ab7f32cb379c5962f9bea026dbdc68d8a704032fc645a1cf9c5c2dd2560a4ebc50ff1c09bc9e6c47fa2cf9ade56ca51c614fd457914d65e7485bebf29ca35bd3818029ff805f8c00fbc1c2081b5864f329fc4bdf76042d7d3f6b63b36f0499b1fad066dc5845999628735ce7c7091657d3b7071a7df253af0d18eb5",
        "verifyFp": "verify_m9cdtg4h_7rZImDdB_F0xZ_4bU1_Bc9X_afkoNTmvEaKG",
        "fp": "verify_m9cdtg4h_7rZImDdB_F0xZ_4bU1_Bc9X_afkoNTmvEaKG",
        "msToken": "5hSdEp9tHuIH2C0XHB3vcXO2sREpI0BxZq97CQm8ooXWK-7prPu41GXiBmvdN-nK2Icf8VSMOapeXtlqg1g8F0aUOugen2tYnBVVfSmuL5lgEPloNmGGEe8H6bnhNYemkNlgAEiTw7KWuHvY2cr80pujv_6f7ydh2FBSdmi49zac12kpC6oI",
        "a_bogus": "E74fgty7Yo/VFdMtucawH7dl2tVANBuyMBiKRxMTHPKsGXMcGmP72rtuaxLy42VERmBTwF37qfM/bEVcOTXkZK9pqmkDuY765U/cIysL/H7dTPJZ7qRsCEbxui4OUCGP//nWiVEXl0UHIocfZrIDAMO9HAeN5Km8sHpcd-WhCxu15SDqq118urGZxXiqPD=="
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    # print("📚 [response.text]", response.text)
    aweme_list = response.json()["aweme_list"]
    return aweme_list

def download_file(filename, url):
    print("🚥 开始下载文件...")
    params = {}
    response = requests.get(url, headers=headers, params=params, stream=True)
    if response.status_code in (200, 206):
        print("🚥 文件写入中...")
        filename = f"output/{filename}.mp4"
        # 获取文件总大小（如果服务器提供 Content-Length 头）
        total_size = int(response.headers.get('content-length', 0))
        # 使用 tqdm 创建进度条
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as progress_bar:
            with open(filename, mode='wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        progress_bar.update(len(chunk))
        print("✅ 文件已成功写入!")
    else:
        print("❌ 请求失败, 状态码:", response.status_code)

if __name__ == "__main__":
    video_list = get_video_list()
    for item in video_list:
        id = item["aweme_id"]
        url = item["video"]["play_addr"]["url_list"][0]
        download_file(id, url)
