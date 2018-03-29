def getTags(tag_str):
	res = tag_str.split()
	res_strip = []
	for x in res:
		res_strip.append(x.lstrip('#'))
	ans = res_strip
	return ans