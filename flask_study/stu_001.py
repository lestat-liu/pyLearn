from flask import Flask
from flask import request
# 创建一个Flask对象
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "this first hello world!"

@app.route("/users/<int:user_id>")
def get_user_id(user_id):
    print(type(user_id))
    return f"这是ID  {user_id}  的用户"

# 获取查询的参数,  http://0.0.0.0:8888/get_param/?name=小白&age=18
@app.route("/get_param/")
def get_canshu():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"姓名是：{name}， 年龄是：{age} ！！！"


# post请求体参数
@app.route("/post_param", methods=["POST"])
def post_param():
    uname = request.form.get('uname')
    pwd = request.values.get('pwd')
    age = request.form.get('age')
    return f"你的名字：{uname}, 密码：{pwd}, 年龄：{age}"


if __name__ == '__main__':
    # 默认localhost和5000端口，
    app.run(host="0.0.0.0", port=8888, debug=True)
    # 自带命令运行： flask run -h 0.0.0.0 -p 8000