# レガシーサイト判定
サイトの作りを判定してラベル付けを行う

## インターフェース
### 入力
#### Pub/Subメッセージの構成
| Message   | 説明             |
| ---       | ---              |
| Data      | JSON形式の文字列 |
| Attribute | -                |

#### Data
| キー         | 値                              | データ型 |
| ---          | ---                             | ---      |
| url          | 解析したサイトのurl             | 文字列   |
| doms         | 解析したサイトのdom情報のリスト | リスト   |
| doms[].name  | HTMLタグ名                      | 文字列   |
| doms[].count | HTMLタグの使用数                | 数値     |

##### サンプルJSON
```json
{
  "url": "http://xxx.com",
  "doms": [
    {
      "count": 1,
      "name": "div"
    },
    {
      "count": 2,
      "name": "h1"
    }
  ]
}
```

#### メッセージPublishサンプル
##### gcloud SDK
```console
$ gcloud pubsub topics publish {TOPIC_NAME} --message '{"url":"http://xxx.com","doms":[{"count":1,"name":"div"},{"count":2,"name":"h1"}]}'
```

##### REST API
###### HTTP request
POST https://pubsub.googleapis.com/v1/{topic}:publish

###### Request body
```json
{
  "messages": [
    {
      "data": "eyJ1cmwiOiJodHRwOi8veHh4LmNvbSIsImRvbXMiOlt7ImNvdW50IjoxLCJuYW1lIjoiZGl2In0seyJjb3VudCI6MiwibmFtZSI6ImgxIn1dfQo="
    }
  ]
}
```

\# `data`はbase64エンコードする


### 出力
#### Pub/Subメッセージの構成
| Message   | 説明        |
| ---       | ---         |
| Data      | サイトのURL |
| Attribute | 判定結果    |

#### Attribute
| キー     | 値                                                                   | データ型 |
| ---      | ---                                                                  | ---      |
| siteType | サイトの判定結果<br>legacy : レガシーサイト<br>modern : モダンサイト | 文字列   |

\# Cloud Pub/Subの仕様により、文字列以外のデータ型は使用不可

#### メッセージPullサンプル
##### gcloud SDK
```console
$ gcloud pubsub subscriptions pull {SUBSCRIPTION_NAME} --auto-ack
  ┌───────────────┬────────────────┬─────────────────┐
  │      DATA     │   MESSAGE_ID   │    ATTRIBUTES   │
  ├───────────────┼────────────────┼─────────────────┤
  │ http:/xxx.com │ xxxxxxxxxxxxxx │ siteType=legacy │
  └───────────────┴────────────────┴─────────────────┘
```

##### REST API
###### HTTP request
POST https://pubsub.googleapis.com/v1/{subscription}:pull

###### Request body
```json
{
  "returnImmediately": true,
  "maxMessages": 1
}
```

###### Response body
```json
{
  "receivedMessages": [
    {
      "ackId": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
      "message": {
        "data": "aHR0cDovL3h4eC5jb20=",
        "attributes": {
          "siteType": "legacy"
        },
        "messageId": "xxxxxxxxxxxxxxxxx",
        "publishTime": "2018-01-01T08:08:19.993Z"
      }
    }
  ]
}
```

\# `data`はbase64エンコードされている
