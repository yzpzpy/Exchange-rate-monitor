#coding: utf-8

# meeqenhewhcmdiic
 
from email.mime.text import MIMEText
import smtplib
def send_mail(con, mail_list):
    mail_content = con
    try:
        content = MIMEText(mail_content, 'plain', 'utf-8') # 邮件的内容；邮件内容的格式；编码utf-8
        reveivers = "Email address"
        content['To'] = reveivers # 接收者
        content['From'] = str("sender") # 发送者
        content['Subject'] = "汇率更新！！！" 
        #需要去开启你的qq邮箱服务，163等其他邮箱也应该有类似的操作
        smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465) 
        smtp_server.login("Email address", 'Password') # 发送者的邮箱账号 对应邮箱账号邮箱服务生成的密码
    
        smtp_server.sendmail("Email address", mail_list, content.as_string())
        smtp_server.quit() 
    except Exception as e:
        print(str(e))