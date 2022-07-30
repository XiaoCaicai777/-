import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import operationPath
import getJokers


def getEmailConfig():
    file = open("email_config.dls", 'r')
    emails = file.read()
    if len(emails) > 0:
        return emails.split(',')
    else:
        print("没有配置email_config.dls配置文件， 请先输入收件人邮箱！！！！")
        return


def message_config(msg):

    """
    配置邮件信息
    :return: 消息对象
    """
    #获取天气信息
    # tianqi = "<p>" + getTomorrowWeather.get_html(None) + "</p>"
    #获取笑话
    joker = "<p>" + getJokers.getJoker() + "</p>"
    # 第三方 SMTP 服务
    mail_msg = """
    <p>这周数据已经准备好啦,请查收,有啥新需求要及时提哦, 我会提醒我家主子为你新增需求哒</p>
    <p style="text-align: right">我家主子一直在努力把我变得更聪明......</p>
    <div style="float: right">
        <p>反馈邮箱地址<a href="#" style="text-align: right">xzs18907401623@163.com</a></p>
    </div>
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
    mail_msg = joker + mail_msg;
    content = MIMEText(mail_msg, 'html', 'utf-8')
    message = MIMEMultipart() # 多个MIME对象
    message.attach(content)  # 添加内容
    message['From'] = Header("永不停息的勤劳小助手", 'utf-8') # 发件人
    message['To']   = Header("嘎嘎好看的小公主", 'utf-8')  # 收件人
    message['Subject'] = Header(msg, 'utf-8') # 主题
    # 添加Excel类型附件
    excles = operationPath.getPath()
    file_name = operationPath.getTargetExcle(excles) # 文件名
    if file_name is None:
        print("发送目标文件不存在！！！")
        return
    file_path = os.path.join(file_name)  # 文件路径
    xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'  # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name)  # 添加到header信息
    message.attach(xlsx)
    return message

def send_mail(message):

    # 配置邮箱服务器信息
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "xzs18907401623"  # 用户名 zpuaszwpmucsbjad  dlryhldgrweobgfa  KJCUSHLICVFYHAOX
    mail_pass = "KJCUSHLICVFYHAOX"  # 密码不是登录密码，是IMAP口令
    # mail_user = "320568015@qq.com"     # 用户名
    start_time = "2022-06-03"  # 神圣的日子
    sub_start_time = "03"
    # 配置发件人、收件人信息
    sender = 'xzs18907401623@163.com'  # 发件人邮箱
    receivers = getEmailConfig()  # 接收邮件，可设置为多个邮箱
    # receivers = ['320568015@qq.com','1913681710@qq.com']  # 接收邮件，可设置为多个邮箱
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        if len(receivers) > 0:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465) # 使用SSL连接邮箱服务器
            smtpObj.login(mail_user, mail_pass)   # 登录服务器
            smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
            print("邮件发送成功")
            print("接受人: " + str(receivers))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # print("开始执行")
    # message = message_config("今日报表") # 调用配置方法
    # print("执行结束")
    # send_mail(message)         # 发送邮件
    # print("执行结束")
    getEmailConfig();