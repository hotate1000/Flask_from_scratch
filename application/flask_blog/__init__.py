# Flaskのインポート
from flask import Flask;
# Flaskアプリケーションを作成
app = Flask(__name__);
# configファイルの位置を設定
app.config.from_object('flask_blog.config');
import flask_blog.views