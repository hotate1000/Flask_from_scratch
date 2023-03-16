# Flaskのインポート
from flask import Flask;
# SQLAlchemyライブラリをインストールする
from flask_sqlalchemy import SQLAlchemy
# Flaskアプリケーションを作成
app = Flask(__name__);
# configファイルの位置を設定
app.config.from_object('flask_blog.config');
# ｋの変数を参照することでデータベースを扱うことが出来る
db = SQLAlchemy(app);

import flask_blog.views