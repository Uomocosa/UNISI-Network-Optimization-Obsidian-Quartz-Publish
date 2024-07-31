
Useful for when you have a sequence of steps you want to run and each step uses the output of the previous step to do something.

~Es.:
```python
def process_videos(url):
	page_html = download_page(url)
	video_links = find_youtube_videos(video_links)
	videos = fetch_youtube_videos(video_links)
	videos = convert_videos_to_mp4(videos)
	return save_videos_to_cloud(videos)

process_videos('some url')
```

~Es.: The Pipeline Pattern Implementation 'Chain of Responsability':
```python
def process_videos(url):
	page_downloader = PageDownloader()
	video_finder = VideoURLFinder()
	youtube_fetcher = YoutubeVideoFetcher()
	mp4_converter = MP4VideoConverter()
	cloud_uploader = VideoCloudUploader()
	
	pipeline = PipelineMenager()
	pipeline.add_step(page_downloader)
	pipeline.add_step(video_finder)
	pipeline.add_step(youtube_fetcher)
	pipeline.add_step(mp4_converter)
	pipeline.add_step(cloud_uploader)
	
	return pipeline.execute(url)
```

~Es.: Advanced Pipeline Implementation using dynmic Imports
```python
def process_videos(url):
	pipeline = PipelineMenager(
		'pipeline.download_page',
		'pipeline.find_youtube_links',
		'pipeline.fetch_youtube_videos',
		'pipeline.convert_videos_to_mp4',
		'pipeline.save_videos_to_cloud',
	)
	
	return pipeline.execute(url)
```