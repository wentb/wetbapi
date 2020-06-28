from flask import Flask
app = Flask(__name__)

#获取所有分类
@app.route('/api/category', methods=["GET"])
def getCategory():
    pass

#根据关键字搜索分类
@app.route('/api/category/<keyword>', methods=["GET"])
def searchCategory(keyword):
    pass

#新建category
@app.route('/api/category', methods=["POST"])
def createCategory():
    pass

#修改category
@app.route('/api/category', methods=["PUT"])
def editCategory()
    pass

#获取分类ID的信息
@app.route('/api/category/<id>', methods=["GET"])
def category(id):
    pass


if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()