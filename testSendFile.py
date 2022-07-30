#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host = "smtp.163.com"   # 设置服务器
mail_user = "xzs18907401623@163.com"     # 用户名 zpuaszwpmucsbjad  dlryhldgrweobgfa  KJCUSHLICVFYHAOX
mail_pass = "KJCUSHLICVFYHAOX"  # 密码不是登录密码，是IMAP口令

sender = '******qq.com'
receivers = ['******@qq.com','****@sina.com.cn'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('a test for python', 'plain', 'utf-8')
message['From'] = Header("ppyy", 'utf-8')
message['To'] = Header("you", 'utf-8')
subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')
try:
 smtpObj = smtplib.SMTP_SSL(mail_host,465)
 smtpObj.login(mail_user,mail_pass)
 smtpObj.sendmail(sender, receivers, message.as_string())
 smtpObj.quit()
 print ("邮件发送成功")
except smtplib.SMTPAuthenticationError as e:
 print(e)