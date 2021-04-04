r"""The routing file."""

from __future__ import print_function
import sys
from __init__ import *
from users import User

# Home Page
@app.route('/home', methods=['GET', 'POST'])
@app.route('/home/<username>')
def home(username=None):
    if request.method == 'POST':
        # 從 request 抓出 delete_users 的值(user.id)
        del_id = request.values['delete_users']

        # 從DB抓出 id 符合 del_id 的 row
        del_user = User.query.filter_by(
            id=del_id).first()

        # 執行刪除
        db.session.delete(del_user)
        db.session.commit()

    return render_template('home.html', username=username, users=User.query.all())


# 註冊頁面
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    # signup
    if request.method == 'POST':
        username = request.values['username']
        password = request.values['password']
        email = request.values['email']

        # 創建新User物件
        new_user = User(username, password, email)

        # 存入DB
        try:
            # 放入待辦事項
            db.session.add(new_user)
            # 處理待辦事項
            db.session.commit()
            # 返回home
            return redirect(url_for('login'))
        except sqlalchemy.exc.IntegrityError as err:
            # 提示錯誤
            flash(err)

    return render_template('signup.html')


# 登入頁面
@app.route('/login', methods=['GET', 'POST'])
def login():
    # login
    if request.method == 'POST':
        username = request.values['username']
        password = request.values['password']

        # 確認是否在DB裡面
        if User.can_login(username, password):
            # 登入成功
            return redirect(url_for('home', username=username))

        flash('未知的帳號或密碼')

    return render_template('login.html')


# 使用者頁面
@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username=None):
    if username is not None:
        m_user = User.query.filter_by(username=username).first()

    if request.method == 'POST':
        user = request.values['user']
        username = request.values['username']

        user.username = username
        db.session.commit()

    return render_template('user.html', user=m_user)
