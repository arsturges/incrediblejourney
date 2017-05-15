import wordnik
from wordnik import swagger, WordApi
api_key = 'aefa9e8bb08c1b19b12040c8fae076f87d14cea47688e8ce7'
api_url = 'http://api.wordnik.com/v4'
client = swagger.ApiClient(api_key, api_url)

wordApi = WordApi.WordApi(client)
example = wordApi.getTopExample('irony')

twitter_api_key = 'nzAYHwT3zpaTWh1YkcYrJvSDG'
