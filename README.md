# PythonDbg

PythonDbgは、Pythonスクリプトのデバッグを支援するためのツールです。このツールは、スクリプトの実行中に関数呼び出しと行の実行をトレースし、それぞれのステップでローカル変数とグローバル変数の値を表示します。

## 主な機能

- 関数呼び出しのトレース
- 行の実行のトレース
- ローカル変数とグローバル変数の表示
- myCuteDebuggerクラスを使用したデバッグセッションの開始
- カスタムハンドラの登録

## 使い方

1. PythonDbgをクローンまたはダウンロードします。
2. デバッグしたいPythonスクリプトを用意します。
3. コマンドラインから以下のコマンドを実行します。

```bash
python dbg2.py <script_to_debug.py>
```

これにより、スクリプトの実行が開始され、各関数呼び出しと行の実行がトレースされます。各ステップで、"Press Enter to continue"と表示されるので、Enterキーを押すことで次のステップに進むことができます。

または、myCuteDebuggerクラスを使用してデバッグセッションを開始することもできます。

```python
import dbg2
import types

def my_new_cute_handler(self, filename, func_name, line_no, event, locals_dict, globals_dict):
    # Your custom logic here
    pass

if __name__ == "__main__":
    myCuteDbgger = dbg2.myCuteDebugger()
    myCuteDbgger.my_cute_handler = types.MethodType(my_new_cute_handler, myCuteDbgger)
    myCuteDbgger.start_debugger()
```

## 注意事項

- このツールはデバッグ目的のみに使用してください。本番環境での使用は推奨されません。
- 大規模なスクリプトのデバッグには時間がかかる場合があります。

## ライセンス

MIT License

## 貢献

バグの報告や機能の提案は、GitHubのIssueを通じてお願いします。