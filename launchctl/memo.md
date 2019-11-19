### plistのロード

```
launchctl load ~/Library/LaunchAgents/info.hotoku.launchctl-sample.plist 
```

RunAtLoad=Trueを指定しているので、勝手に起動する。~/temp/hogeを見ると、1秒ごとに時刻が追記されているのが見える

### タスクのスタートとストップ

```
launchctl start info.hotoku.launchctl-sample
launchctl stop info.hotoku.launchctl-sample
```
