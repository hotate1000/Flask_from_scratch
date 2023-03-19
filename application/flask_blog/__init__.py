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

# import flask_blog.views
# from flask_blog.views import views, entries;
from flask_blog.views.views import view;
app.register_blueprint(view, url_prefix='/users');

from flask_blog.views.entries import entry;
app.register_blueprint(entry, url_prefix='/users');
from flask_blog.views import views;
