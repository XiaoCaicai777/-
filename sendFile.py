import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import os
import operationPath

# 配置邮箱服务器信息
mail_host = "smtp.163.com"   # 设置服务器
mail_user = "xzs18907401623"     # 用户名 zpuaszwpmucsbjad  dlryhldgrweobgfa  KJCUSHLICVFYHAOX
mail_pass = "KJCUSHLICVFYHAOX"  # 密码不是登录密码，是IMAP口令
# mail_user = "320568015@qq.com"     # 用户名
# mail_pass = "lby1106JWhaha"  # 密码不是登录密码，是IMAP口令

# 配置发件人、收件人信息
sender = 'xzs18907401623@163.com' # 发件人邮箱
# receivers = ['320568015@qq.com']  # 接收邮件，可设置为多个邮箱
receivers = ['lonb1981@163.com', '191739006@qq.com', '429765062@qq.com']  # 接收邮件，可设置为多个邮箱


def message_config(msg):
    """
    配置邮件信息
    :return: 消息对象
    """
    #获取天气信息
    # tianqi = "<p>" + getTomorrowWeather.get_html(None) + "</p>"
    # 第三方 SMTP 服务
    mail_msg = """
    <p>您好, 幼鲜知本周数据准备好了, 请查收!!!</p>
    """
    # mail_msg = """
    # <p>哈喽, 早上好, 心情好点没, 今日份的数据小的已经为你准备好啦,请查收</p>
    # <p>我家主子嘴笨, 说话气到你了吧, 他就是个猪蹄, 今天要开心起来哦</p>
    # <p>有啥新需求要及时提哦, 我会提醒我家主子为你新增需求哒</p>
    # <p style="text-align: right">我家主子一直在努力我把变得更聪明......</p>
    # <div style="float: right">
    #     <p>点击投诉他<a href="#" style="text-align: right">xzs18907401623@163.com</a></p>
    # </div>
    # """
    # mail_msg = tianqi + mail_msg
    # now = datetime.datetime.now().strftime('%Y-%m-%d')
    content = MIMEText(mail_msg, 'html', 'utf-8')
    message = MIMEMultipart() # 多个MIME对象
    message.attach(content)  # 添加内容
    message['From'] = Header("小助手", 'utf-8') # 发件人
    message['To'] = Header("商业顶尖人才", 'utf-8')  # 收件人
    message['Subject'] = Header(msg, 'utf-8') # 主题
    # 添加Excel类型附件
    file_name = operationPath.getTargetExcle(operationPath.getPath()) # 文件名
    file_path = os.path.join(file_name)  # 文件路径
    xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'  # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name)  # 添加到header信息
    message.attach(xlsx)
    return message

def send_mail(message):
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) # 使用SSL连接邮箱服务器
        smtpObj.login(mail_user, mail_pass)   # 登录服务器
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
        print("邮件发送成功")
        print("接受人: " + str(receivers))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("开始执行")
    message = message_config() # 调用配置方法
    send_mail(message)         # 发送邮件
    print("执行结束")