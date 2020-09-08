import json

# server = { 'baseUrl': 'http://localhost:8153/go/api', 'userName': 'admin', 'apiToken': 'secret' }

# request = HttpRequest({'url': 'http://site'}, "username", "password")

httpRequest = HttpRequest({'url' : server['baseUrl']}, server['userName'], server['apiToken'])

print (httpRequest)

ISSUE_PATH = '/pipelines/{}/history'.format('test1')

response = httpRequest.doRequest(
    # method='GET', #default GET method
    context=ISSUE_PATH,
    # body={}, #optional to GET method
    # contentType='application/json', #optional
    # headers={} #optional
    )
    
if not response.isSuccessful():
    raise response.errorDump()

print (response.getResponse())

gocdPipelineHistoryJson=json.loads(response.getResponse())

print(gocdPipelineHistoryJson)