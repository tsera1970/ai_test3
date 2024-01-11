Azure API Management サービスの「Azure OpenAI サービスのChatGPTモデル呼び出しAPI」を使用したチャットボット<br>
<br>
API（Azure API Management）を使用しているので、ログ取得が可能<br>
API（Azure API Management）への問い合わせは平文（text/plain）<br>
API（Azure API Management）内でJSON形式に変更して問い合せ<br>
応答はJSON形式内なので、pythonプログラム内で、変換して読取<br>
<br>
モデルに対してJSON形式でチューニングできないので、APIの仕様を変更する必要があるかも
