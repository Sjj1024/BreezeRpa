import requests


def get_page_content(url):
    # url = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page=3"
    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ccsid=617-6052789-5096632; __qca=P0-3264717-1681619531246; logged_out_browsing_page_count=2; u=I27qA1F5ss332s8vplrK1DLGOOJv_Nw-_Z4Xf00dELaKGlVi; p=C3LRNqn0B2yjK1zx7fek9ZOQLd1Nc3Wd75GpF0SDDXEAQo77; likely_has_account=true; _session_id2=7e2d48883ab6a182577e85ee212e45ab; locale=en; srb_8=0_ar; csm-sid=240-7181604-6458614; jwt_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImZSNXpfWTVjYXZQMllsaXU3eks0YUNJVEJPcVBWdGtxTE9XVURfV3dGOTQifQ.eyJpc3MiOiJodHRwczovL3d3dy5nb29kcmVhZHMuY29tIiwic3ViIjoia2NhOi8vcHJvZmlsZTpnb29kcmVhZHMvQTFaTFpQVUszTk9YTFoiLCJhdWQiOiI2M2RjMjRlN2M2MTFlNmYxNzkyZjgxMzA1OGYyMTU2MGJkOGM2OTM4ZDU0YS5nb29kcmVhZHMuY29tIiwidXNlcl9pZCI6MTY0ODQ4NjA3LCJyb2xlIjoidXNlciIsIm5vbmNlIjpudWxsLCJleHAiOjE2ODE2MjA1MTAsImlhdCI6MTY4MTYyMDIxMH0.HWtttiqV6vNT8Zh2QGYfvzt7tog6IbvfAZnpMp_XqvQLYtsKj5-LL6qqhfodI_PhAKG-KYgvtrNvJEqbrgiYvLm5RFz95B6QP80By7z6h7v9574Pc93soe-nSitXwoYhW2g_SlOS1yKd_ckHfotKs-X9PAVbg5IIDZUoR41tTyh917okM8xzOranIu_Txw0Zd1R00guzvp5UlKhUffcrHkhCg7Wu7UqJXOHwtailR4sr2RYZwPEgbxUNoaHGPlNJ1D3Qog4dxs1ZdYk_qKIKlhXcZZi_2q5e_D1gCSK9FB4j5I2-X8z2_nrhJrCxHpS63aQmpBMCIb6W8w8lgNYnQA; _session_id2=7e2d48883ab6a182577e85ee212e45ab',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    if "avg rating" in response.text:
        print(f"成功: {url}")
    else:
        print(f"失败:{url}")


def run():
    print(f"开始")
    for i in range(1, 1000):
        url = f"https://www.goodreads.com/list/show/1.Best_Books_Ever?page={i}"
        get_page_content(url)


if __name__ == '__main__':
    run()
