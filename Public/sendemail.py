import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time
from email.mime.multipart import MIMEMultipart
resultdir = "C:/Users/admin/PycharmProjects/python/xybao/Report/"

# sender    = "361690074@qq.com"
# password  = "ezvmlgkxkxukbiba"
# receiver  = "285384556@qq.com"
# smtpsever="smtp.qq.com"
# msg = MIMEText("测试结果：")
# msg["Subject"] = "测试报告"
# msg["From"]    = sender
# msg["To"]      = receiver
#
# try:
#     s = smtplib.SMTP_SSL(smtpsever)
#     s.login(sender, password)
#     s.sendmail(sender, receiver, msg.as_string())
#     s.quit()
#     print("邮件发送成功!")
# except smtplib.SMTPException as e:
#     print("无法发送邮件!")
#     print(e)

def send_mail(file_new,file_name):
    sender    = "361690074@qq.com"
    password  = "ezvmlgkxkxukbiba"
    receiver  = "285384556@qq.com"
    smtpsever="smtp.qq.com"
    f=open(file_new,"rb")
    mail_body=f.read()
    f.close()

    #附件形式发
    msg = MIMEMultipart()
    att = MIMEText(mail_body, 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename='+file_name
    msg.attach(att)

    # 文本形式发
    # msg=MIMEText(mail_body,_subtype="html",_charset="utf-8")

    msg["Subject"] = "自动化测试报告"
    msg["From"]    = sender
    msg["To"]      = receiver
    try:
        s = smtplib.SMTP_SSL(smtpsever)
        s.login(sender, password)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        print("邮件发送成功!")
    except smtplib.SMTPException as e:
        print("无法发送邮件!")
        print(e)
    finally:
        s.close()

def send_report(testreport):
    result_dir =testreport
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    print("最新文件：" + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    send_mail(file,lists[-1])


if __name__=="__main__":
    send_report(resultdir)