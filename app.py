from flask import Flask,render_template,request,flash,url_for,redirect
from flask_mail import Mail, Message
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['MAIL_SERVER']='smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '3330861773@qq.com'
app.config['MAIL_PASSWORD'] = 'qwrhivyusxzldaig'
app.config['MAIL_USE_TLS'] = False
# 启用/禁用安全套接字层加密
app.config['MAIL_USE_SSL'] = True
# 创建类的实例
mail = Mail(app)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/case1')
def case1():
    return render_template('case1.html')

@app.route('/queryPrice', methods=['GET', 'POST'])
def queryPrice():
    name = request.form['name']
    phone = request.form['phone']
    community = request.form['community']
    area = request.form['area']

    # sender：发件人    recipients：收件人
    msg = Message('新的报价信息', sender = '3330861773@qq.com', recipients = ['2252424406@qq.com','2644756040@qq.com'])
    msg.body = f"姓名: {name}, 联系方式: {phone}, 小区: {community}, 面积: {area}"
    mail.send(msg)#发送Message类对象的内容
    print("发送成功")
    flash("您的咨询信息已经收到，报价信息请等待回信！","success")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()