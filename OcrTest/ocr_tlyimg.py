import ddddocr
import requests

ocr = ddddocr.DdddOcr(beta=True)
with open("fly2.png", "rb") as f:
    res = ocr.classification(f.read())
    print(res)
