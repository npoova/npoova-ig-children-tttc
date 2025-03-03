# Talk to the City（OVA改変版）

本リポジトリは、特定非営利活動法人OVAが[Talk to the City](https://github.com/AIObjectives/talk-to-the-city-reports)に改変を加え、「インターネット・ゲートキーパー事業における10代以下の相談者からの相談内容」レポートを出力する際に使用したリポジトリです。


## 改変箇所

- Azure OpenAI APIで使用できるように調整
- Azure OpenAI のコンテンツフィルタリングにかかった場合、エラーで処理が停止されるのではなく、該当の相談内容のみスキップされる仕様に変更
- 環境変数を.env内に記述できるように変更
- extraction、labelling、takeaways のプロンプトを調整