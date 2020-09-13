# XNXXapi.py
A Python API for getting content from xnxx.com.

## Classes
### search()
A single page of search results.

#### Args:
`input: str` Your search terms.

`page: int` The page number you want results from.

`mode: str` How to sort the results - `'hits'` or `None`: None for "Default", 'hits' for by view count.

#### Vars:
`input: str` The search terms you entered.

`page: int` The page number you entered.

`mode: str` The mode you entered.

`totalResults: int` The total number of results for your search. (this many results may or may not be indexable, as page numbers are seemingly limited to 112)

`totalPages: int` The highest page number visible.

`videos: list` A list of video IDs as strings.

`results: int` The length of `videos`.

#### Funcs:
##### `video() -> video`
Get video with nth ID from `videos`.

`num: int` Index of video to return.

#### Example:
```py
a = XNXXapi.search('hot videos', page=2)
print('Got '+str(a.totalResults)+' results for "hot videos": '+str(videos))
vid = a.video(10)
```


### video()
A single video.

#### Args:
`id: str` The video's ID.

#### Vars:
`id: str` The ID you entered.

`streamURL: str` A URL to the video stream file. Only valid for a certain time.

`thumbnail: str` A URL to a thumbnail for the video.

`title: str` The video's title.

`description: str` The description of the video.

`duration: str` The rough duration of the video. (i.e. '21min')

`resolution: str` The resolution of the video. (i.e. '480p')

`views: int` The number of views.

`rating: str` The percentage of positive reviews(?)

`tags: list` A list of the video's tags as strings.

#### Funcs:
##### `thumbnail() -> str`
Get nth thumbnail URL for video.

`num: int` Index of thumbnail to return. Values 1 to 30 are valid.

##### `thumbnails() -> list`
Get all thumbnail URLs for video in a list.

#### Example:
```py
vid = XNXXapi.video(id='ug6zt5c')
print('Watch "'+vid.title+'" at '+vid.streamURL)
```
