# MIT License

# Copyright (c) 2022 Beksultan Artykbaev

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import requests
import re

def count_steam_rep(steam_url: str) -> int:
	'''Counts total reputation for steam user.'''
	reputation = 0
	for page in range(1, 1001): # Steam stores only 50.000 comments for user, each page can contain 50 comments
		all_comments_url = f"{steam_url}/allcomments?ctp={page}"
		steam_response = requests.get(all_comments_url).text
		comments = re.findall(r'<div class="commentthread_comment_text" id="comment_content_[0-9]+">\r\n\t\t\t\t(.*)\t\t\t</div>', steam_response)
		if not comments:
			return reputation # If there is no more comments in page, returns total reputation
		for comment in comments:
			if re.match(r"(?:[+][\s]+|[+]|plus[\s]+)(?:reputation|rep)", comment):
				reputation += 1
			elif re.match(r"(?:[-][\s]+|[-]|minus[\s]+)(?:reputation|rep)", comment):
				reputation -= 1
	return reputation

if __name__ == "__main__":
	description = '''--- Steam reputation counter ---'''
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("-url", "--steam_url", type=str, required=True)
	args = parser.parse_args()
	print(count_steam_rep(args.steam_url))