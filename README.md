
# 👍 count_steam_rep
[![build](https://github.com/Vazno/count_steam_rep/actions/workflows/main.yml/badge.svg)](https://github.com/Vazno/count_steam_rep/actions/workflows/main.yml)
##### Count steam reputation for given steam profile

## Usage:
- First:
```
usage: count_steam_rep.py STEAM_USER_URL
```
- Second:
```python
count_steam_rep("steam_user_url")
```
# How does it work?
##### To find all comments it goes through pages in profile's allcoments section
Then finds comments using this re pattern:
- `<div class="commentthread_comment_text" id="comment_content_[0-9]+">\r\n\t\t\t\t(.*)\t\t\t</div>`
### Finally counts reputation by comments in profile which contain these re patterns:
#### Positive reputation (add 1)
- `(?:[+][\s]+|[+]|plus[\s]+)(?:reputation|rep)`
#### Negative reputation (minus 1)
- `(?:[-][\s]+|[-]|minus[\s]+)(?:reputation|rep)`

## 🔑 License:
[MIT](https://choosealicense.com/licenses/mit/) - Beksultan Artykbaev
