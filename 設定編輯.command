#!/bin/bash
cd "$(dirname "$0")"
python3 bin/make_gate.py
echo
echo "完成。請把 gate.json 一併更新上網（如果網站已 push，再 git add gate.json && git commit && git push）。"
read -n 1 -s -p "撳任何鍵關閉"
