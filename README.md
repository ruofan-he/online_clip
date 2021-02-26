# online_clipboard
## 環境整備
### python
pythonのライブラリ周りの仮想環境にはvenvがおすすめです。pythonの純正モジュールです。
```
python -m venv [envname]
source [envname]/bin/activate
```
仮想環境を抜けるには
```
deactivate
```
### 必要なライブラリについて
`setup.py`に書いたので必要無いかもですが、
```
pip install flask
pip install alembic
pip install sqlalchemy
```

### `import`システムについて
pythonでは`import`に2種類あります。
#### 相対インポート
相対パスでインポートする方法です。
これが有効になるのは、
呼び出し元と先が同じパッケージに属していて、
呼び出し元がパッケージ呼び出しによる実行のときだけです。
パッケージ呼び出しは後述の`python -m`オプションによる実行、
あるいは`import [module_name]`でコード上で呼び出されることを指します。
```
from . import db
#この行は通常そのディレクトリの__init__.pyで定義されている
#dbをインポートする

from .__init__ import db #明示的

from .db import db
#dbディレクトリ内の__init__.pyからdbインポート
#もしくはdb.pyからdbインポート
```
`.`は`current directry`の意味です。

下位ディレクトリは`.dir1.dir2`みたいに指定します。
上位ディレクトリは`..`とか`...`みたいに指定します。
ドットが増えるほど上位です。

#### 絶対インポート
絶対パスでインポートする方法です。
現在のワーキングディレクトリ以下しかインポートできません。

任意の場所のものをインポートしたいときは、
`current directry`を変更するスクリプトを
挟むか、`sys.path.append('target_path')`やって`import`するとか、
`importlib`を使うなど、動的に`import`するしかありません。
当然、そういうことをするとIDEの補完が効かなくなります。
避けましょう。

### 実行について
pythonではモジュールとして作ったプログラムの起動方法として次があります。
```
python -m [module_name] ...(各種コマンドライン引数)
```
`[module_name]`は作業ディレクトリにあるフォルダ名でもいいですし、
`pip install`したときのモジュール名でもいいです
(このとき各`site-package`内の該当モジュールから読み取られます。)。

この方法で起動したとき、
モジュール直下に存在している`__init__.py`→`__main__.py`の順番で
実行されます。`__main__.py`は`-m`から起動したときのみ発動するスクリプトだと
考えやすいかもしれません。

`__init__.py`は必ず読み込まれます。なにかの事情で回避したいときも
あるかもしれませんが方法は知りません。`__init__.py`内部の処理で`-m`から起動したときだけ実行しない文を追加する事も考えられるかもしれません。

## `alembic`の使い方
将来的にアジャイルなデータベース運用に移るとmigrationツールがあったほうが便利です。
`alembic`は`sqlalchemy`用のmigrationツールで、
スキーマの変更に応じたテーブル構造の変更を自動的にやってくれます。
とりあえずテーブルコラムの追加などにしか使わないつもりですが、
スキーマアップデート時のデータ変更も自動的にやらせるかもしれません。

設定ファイルの生成
```
alembic init [dir_name]
```
あれこれ
```
alembic revision -m 'message' # 手動でテーブル変更指示が必要
alembic revision --autogenerate # sqlalchemyスキーマから自動生成
alembic update # データベースの実際のマイグレーション url設定は必要
```
ぜんぶ`python -m online_clipboard migration [command]`で
できるようにした。

`--autogenerate`で参照するスキーマ本体の設定は`alembic/env.py`で
`target_metadata`にスキーマの`metadata`を代入することによって、
実現される。


