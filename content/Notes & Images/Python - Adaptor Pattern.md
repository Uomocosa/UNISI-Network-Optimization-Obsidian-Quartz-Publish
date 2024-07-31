# How do you integrate outside code?
For example a library that you download or from any other source.
~Ex.:
```python
class FacebookConsumer(token)
- post_new_message(text)
- get_latest_timeline_post()
#----------------------------
class TwitterConsumer(token)
- tweet_message(text)
- get_latest_tweet()
```
-> We want to fetch post from both the social networks:
~Es.: Pretty std way:
```python
def store_timeline_post():
	fb_consumer = FacebookConsumer('some-token')
	post = fb_consumer.get_latest_timeline_post()
	database.add_post(post)
#------------------------------------------------
def store_tweet():
	twitter_consumer = TwitterConsumer('some-token')
	post = twitter_consumer.get_latest_tweet()
	database.add_post(post)
#------------------------------------------------
store_timeline_post()
store_tweet()
```
~Es.: A better way Version 1: (Plugin):
```python
class PostAdapter:
	def __init__(self, consumer, method_name):
		self.consumer = consumer
		self.method_name = method_name
		
	def get_post(self):
		method = getattr(
			self.consumerm, self.method_name)
		return method()
	
def store_post(consumer):
	post = consumer.get_post()
	database.add_post(post)

fb_consumer = FacebookConsumer('some_token')
adapted_fb_consumer = PostAdapter(
	fb_consumer, 'get_latest_timeline_post')
store_post(adapted_fb_consumer)
```
###### Vantaggi:
- È possibile creare una classe generale per determinati oggetti.
- Le funzioni relative alla classe dovranno essere scritte una sola volta.
- Molto generale.
--- 
~Es.: A better way Version 2: (Inheritance):
```python
class FbAdapter(FacebookConsumer):
	def get_post(self):
		return super().get_latest_timeline_post()

class TwAdapter(FacebookConsumer):
	def get_post(self):
		return super().get_latest_tweet()
```
###### Vantaggi:
- Più generale del primo esempio.
- Se ci sono poche classi da dover generalizzare è più veloce.