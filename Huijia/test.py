import base64

content = "The quick and simple editor for cron schedule expressions by Cronitor"
print(len(content))
print(base64.b64encode(content.encode("utf-8")))