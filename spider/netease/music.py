import requests
import execjs
from tqdm import tqdm

# 设置请求头: User-Agent 是必须的
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Range": "bytes=0-",
    "Referer": "https://music.163.com/",
    "Sec-Fetch-Dest": "audio",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

def encryptParams(params):
    # 读取文件
    js_file = open("music.js", encoding="utf-8").read()
    # 编译代码
    js_code = execjs.compile(js_file)
    # 调用函数
    res = js_code.call("encryptParams", params)
    print("✅ 加密参数:", res)
    return res

def get_download_url(ids):
    # csrf_token 可以直接复制, 或者从 document.cookie 里截取
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=122e217e46f8efd33d1b19ef5274d135"
    encrypted = encryptParams({
        "ids": ids,
        "level": "exhigh",
        "encodeType": "aac"
    })
    params = {
        "params": encrypted["encText"],
        "encSecKey": encrypted["encSecKey"]
    }
    response = requests.post(url, headers=headers, params=params)
    print("📚 [response.text]", response.text)
    download_url = response.json()["data"][0]["url"]
    if download_url == None:
        print("❌ 下载链接:", download_url)
    else:
        print("✅ 下载链接:", download_url)
    return download_url

def download_file(url):
    print("🚥 开始下载文件...")
    params = {} # url 已经带了必要的参数, 不需要额外参数
    response = requests.get(url, headers=headers, params=params, stream=True)
    if response.status_code in (200, 206):
        print("🚥 文件写入中...")
        filename = "output/music.mp3"
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
    # 1. 获取下载链接
    url = get_download_url([453268268]) # 453268268, 2707649871
    # 2. 下载文件
    download_file(url)
