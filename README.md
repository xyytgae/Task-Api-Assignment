# Task Api Assignment

## 1. 概要
新たなプロジェクトでタスク管理クラウドアプリを作成することになりました。
今回あなたは、タスク管理クラウドアプリ用のバックエンドAPIを作成を担当するつもりで、以下の課題に取り組んでください。

## 2. 課題
### 2.1. タスク管理用APIの作成
#### 課題1の前提条件
  - タスクは以下の属性を持つとします。
    - タスクのタイトル (title)
    - タスクの内容 (content)
    - タスクの期限 (due_date)
    - タスクのステータス (status: `Open`・`In Progress`・`Closed`)
#### 課題1. API作成
以下の3つの API を作成すること
- タスク登録用API
  - 登録用リクエストには、「タスクのタイトル」・「タスクの内容」・「タスクの期限」を設定する
  - タスク登録時のステータスはOpenとする
  - レスポンスは作成されたタスクの各属性とタスクIDを返すようにしてください
- タスク一覧取得API
  - 作成したタスクの一覧を取得できるAPIを作成すること
  - タスク一覧取得時に、「タスクの期限」・「タスクのステータス」でフィルタできるようにすること
- タスク更新用API
  - タスクの以下の属性を更新するためのAPIを作成すること
    - タスクのタイトル
    - タスクの期限
    - タスクのステータス

### 2.2. 記述問題
課題1で作成したAPIについて以下を説明してください。**英語で書いても構いません**。
1. APIの実装で工夫したところ
2. APIの実用を考えるうえで、さらに改良していかなければならないこと

レポジトリに`assignment2_answer.txt` というテキストファイルを作成して、そこに回答を記述してください。

## 3. 課題の進め方

### 3.1. 事前準備
- Docker と Docker Compose を利用できるようにしてください
- API開発に基本的に必要な以下のライブラリ等は、Docker コンテナにインストールされるようにしています
  - FastAPI
  - Uvicorn
  - SQLAlchemy
- その他、必要に応じてライブラリを追加していただいて構いません。

### 3.2. リポジトリのダウンロードとDockerコンテナのビルド・起動
```bash
$ git clone https://gitlab.hacarus.com/hirotoshi.uchino/task-api-assignment.git
$ cd task-api-assignment
$ docker-compose build   # Docker コンテナのビルド
$ docker-compose up   # Docker コンテナの起動
```

### 3.3. APIのサンプル動作確認とデータベースの初期化
本リポジトリには、初期状態としてサンプルのデータとAPIが含まれています。

以下のコマンドで、データベースの初期化とサンプルデータの作成が実行されます。
```bash
$ docker-compose run --rm --entrypoint "poetry run python ./init_db.py" task-api-assignment
```

上記コマンドでサンプルデータを作成し、Docker コンテナを起動した状態で、以下のコマンドを実行するとサンプルデータが取得できます。
```bash
$ curl localhost:8000/api/tasks/1

# レスポンス  -----------------------
{
  "title": "sample_task",
  "content": "sample_task_content",
  "due_date": "2022-08-10",
  "status": "Open"
}
```

`localhost:8000/api/tasks/1` は、タスクIDによってタスクの属性を取得するサンプルのAPIとなっています。このAPIを参考にして、課題のAPI作成を進めてください。


## 4. 課題提出方法
- `git archive` 機能を使い、tar.gz に圧縮したものを提出してください。
- この README を変更し、以下を記述しておいてください。なお、README は**英語で書いても構いません**。
  - 使用ライブラリ・フレームワーク等
    - SQLAlchemy
    - Pydantic
    - FastAPI
  - API のインストール・起動方法・動作確認方法
    ```bash
    $ git clone https://gitlab.hacarus.com/hirotoshi.uchino/task-api-assignment.git
    $ cd task-api-assignment
    $ docker-compose build   # Docker コンテナのビルド
    $ docker-compose up   # Docker コンテナの起動
    ```
  - API の仕様
    - APIにはFastAPI、DBにはSQLite、ORMにはSQLAlchemyを使用して実装
    - タスクの登録、更新、一覧取得の機能を実装
      - タスクの登録
        ```bash
        $ curl -X 'POST' \
          'http://localhost:8000/api/tasks' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "title": "sample_task1",
          "due_date": "2022-08-10",
          "content": "sample_task_content"
        }'
        # レスポンス  -----------------------
        {
          "id": "1",
          "title": "sample_task1",
          "content": "sample_task_content",
          "due_date": "2022-08-10",
          "status": "Open"
        }
        ```
      - タスクの更新
        ```bash
        $ curl -X 'PUT' \
          'http://localhost:8000/api/tasks/1' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "title": "sample_task123",
          "due_date": "2023-12-10",
          "status": "Closed"
        }'
        # レスポンス  -----------------------
        {
         "id": "1",
         "title": "sample_task123",
         "content": "sample_task_content",
         "due_date": "2023-12-10",
         "status": "Closed"
         }
        ```
      - タスクの一覧取得

        due_dateやstatusのフィルタリングを行わずに取得 
        ```bash
        $ curl -X 'GET' \
          'http://localhost:8000/api/tasks' \
          -H 'accept: application/json'

        # レスポンス  -----------------------
        [
          {
            "id": "1",
            "title": "sample_task123",
            "content": "sample_task_content",
            "due_date": "2023-12-10",
            "status": "Closed"
          }
        ]
        ```

        due_dateやstatusのフィルタリングを行い取得
        ```bash
        $ curl -X 'GET' \
          'http://localhost:8000/api/tasks?due_date=2023-12-10&status=Closed' \
          -H 'accept: application/json'

        # レスポンス  -----------------------
        [
          {
            "id": "1",
            "title": "sample_task123",
            "content": "sample_task_content",
            "due_date": "2023-12-10",
            "status": "Closed"
          }
        ]
        ```

