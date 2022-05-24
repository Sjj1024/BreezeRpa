import logging
import smtplib
from email.mime.text import MIMEText

from Info import config_obj


def send_email(title: str, content: str, email):
    # 邮件发送方邮箱地址
    sender = 'sjjhub@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = [email]
    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]
    # 登录并发送邮件
    try:
        # 在阿里云上就要改为下面这种，本地和服务器都友好：
        smtpObj = smtplib.SMTP_SSL(config_obj.MAIL_HOST, 465)
        # 登录到服务器
        smtpObj.login(config_obj.MAIL_USER, config_obj.MAIL_PASS)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
    except smtplib.SMTPException as e:
        logging.error(f"发送邮件失败:{e}")
