from googleCrawling import googleCrawling, googleCrawling_mac
from concat import concat

DOWNLOAD_PATH = '.'

# 재현
# googleCrawling_mac('value', 0, 500, DOWNLOAD_PATH)
# # 유하
# googleCrawling('value', 500, 1071, DOWNLOAD_PATH)
# 이건 둘중 한명이 마지막에 하좌
concat('value')

# # 재형
# googleCrawling('overlap', 0, 682, DOWNLOAD_PATH)
# concat('overlap')
# # 혜인
# googleCrawling('growth', 0, 503, DOWNLOAD_PATH)
# concat('growth')