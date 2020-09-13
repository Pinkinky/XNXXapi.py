from bs4 import BeautifulSoup
import requests, re

baseURL = "https://www.xnxx.com/"

#Return the argument used in a string single-argument javascript function.
def javascriptGetArg(script: str, function: str) -> str:
	try:
		return str(re.search("'(.+?)'", script.split(function, 1)[1]).group(0)[1:-1])
	except:
		return None

class search:
	def __init__(self, input: str, page: int = 1, mode: str = None):
		request = requests.get(baseURL + "/search/{}{}/{}".format(input, "/{}".format(mode) if mode is not None else "", page-1), timeout=60)
		request.raise_for_status()
		soup = BeautifulSoup(request.content, "html.parser")
		self.input = input
		self.page = page
		self.mode = mode
		self.totalResults = int(soup.find("span", title="[:NB_FREE_VIDEOS:{").text.split()[0].replace(",", ""))
		self.totalPages = int(soup.find_all("li")[-2].a.text)
		self.videos = [div.find("a")["href"].split("video-", 1)[1].split("/", 1)[0] for div in soup.find("div", class_="mozaique").find_all("div", recursive=False)]
		self.results = len(self.videos)
		if not self.results > 0:
			raise Exception()
	
	def video(self, num: int):
		return video(self.videos[num-1])

class video:
	def __init__(self, id: str):
		self.pageURL = baseURL + "video-{}/".format(id)
		request = requests.get(self.pageURL, timeout=60)
		request.raise_for_status()
		soup = BeautifulSoup(request.content, "html.parser")
		self.id = id
		self.streamURL = soup.find("a", text="View High Qual")["href"]
		self.thumbnail = javascriptGetArg(str(request.content), "html5player.setThumbUrl169")[:-1]
		#self.thumbnails = self.thumbnailGetList(thumbnail)
		self.title = soup.find("strong").text
		self.description = soup.find("p", class_="metadata-row video-description").text
		metadata = [meta.strip() for meta in soup.find("span", class_="metadata").text.split("-")]
		self.duration = metadata[0]
		self.resolution = metadata[1]
		self.views = int(metadata[2].replace(",", ""))
		self.rating = soup.find("span", class_="rating-box value").text
		self.tags = [tag.text for tag in soup.find("div", class_="metadata-row video-tags").find_all("a")]
	
	#Return a thumbnail number num from thumbnail URL.
	def thumbnail(self, num: int) -> str:
		return re.sub("\.\d{1,2}\.", ".{}.".format(str(num)), self.thumbnail)
	
	#Return a list of all thumbnail URLs from a single thumbnail URL.
	def thumbnails(self) -> list:
		thumbs = []
		for num in range(1, 31):
			thumbs.append(self.thumbnail(num))
		return thumbs