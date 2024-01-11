from flask import Flask, request, jsonify, render_template
import json
import requests
from requests.exceptions import RequestException

app = Flask(__name__)

# プロキシ認証情報を設定
proxies = {
    "http": "http://sera:Ej3AR1MH,<@172.16.1.23:15080",
    "https": "http://sera:Ej3AR1MH,<@172.16.1.23:15080"
}

# APIエンドポイントのURL
#deployment_id = "model-gpt-35-turbo-16k"
#api_version = "2023-07-01-preview"
#api_base = 'https://hekchat-api-managementservice.azure-api.net/openai/deployments/' + deployment_id + '/chat/completions?api-version=' + api_version
api_base = 'https://hekchat-api-managementservice.azure-api.net/openai/'


@app.route('/', methods=['GET'])
def index():  
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # リクエストからユーザーの入力メッセージを取得
    user_message = request.json['message']

#    # OpenAI APIへのリクエストパラメータを設定
#    user_data = {
#        "model":"model-gpt-35-turbo-2"
#      , "messsges":[{
#            "role":"user"
#          , "content" : user_message
#        }]
#    }

#    # プロキシの設定
#    proxies = {
#        "http": "http://sera:Ej3AR1MH,<@172.16.1.23:15080"
#      , "https": "http://sera:Ej3AR1MH,<@172.16.1.23:15080"
#    }

    headers={
#        "Content-Type": "application/json"
        "Content-Type": "text/plain"
#      , "Host": "hekchat-api-managementservice.azure-api.net"
      , "Ocp-Apim-Subscription-Key": "fa27b8cb5a3249bb93efe843fca26015"
    }

    try:
        # Azure APIManagementI APIにリクエストを送信
        response = requests.post(
            api_base
#          , json=user_data
          , data=user_message
          , headers=headers
#          , proxies=proxies  # プロキシを指定
        )
        print("response:",response.text)

        # レスポンスから生成されたテキストを取得
#        generated_text = json.loads(response.text)
        generated_text = response.json()["choices"][0]["message"]["content"]

        print("generated_text:",generated_text)


        # レスポンスを返す
        return jsonify({'message': generated_text})

    except RequestException as e:
#        print("error:[" + e.response.text + "]")
        print("error1:",e)
        return jsonify({'message': 'エラーが発生しましたね。'})

    except Exception as e:
        # エラーメッセージを返す
        print("error2:",e)
        return jsonify({'message': 'エラーが発生しましたよ。'})

if __name__ == '__main__':
    app.run(debug=True)
