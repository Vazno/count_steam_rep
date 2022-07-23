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