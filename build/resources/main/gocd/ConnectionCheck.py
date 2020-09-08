#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import urllib3
import sys

server = { "apiUrl": "http://localhost:8153/go/api", "apiUser": "admin", "apiToken": "2c96ae755244a3a2dab05751aadc020a0a74d13d", "password": "secret"}
# Initialize variables & check parameters
apiUrl = server['apiUrl']
apiUser = server['apiUser']
apiToken = server['apiToken']
password = server['password']
if not apiUrl.strip():
    raise Exception("Error: Server configuration 'apiUrl' is undefined\n")
if not apiToken.strip():
    raise Exception("Error: Server configuration 'apiToken' undefined\n")

fullUrl = "{}/{}".format(apiUrl, "current_user")

if password.strip():
    headers = urllib3.make_headers(basic_auth='%s:%s' % (apiUser, password))
else:
    headers = { "Authorization": "Bearer %s" % apiToken.strip() }
headers["Accept"] = "application/vnd.go.cd.v1+json"

try:
    http = urllib3.PoolManager()
    response = http.request('GET', fullUrl, headers=headers)
    data = response.data.decode('utf-8')
    if not data:
        raise Exception("No valid path, please check url path: {}".format(apiUrl));
except urllib3.exceptions.HTTPError as error:
    print ("Reason: %s" % "HTTPError")
    raise Exception(error)
except Exception as error:
    raise Exception(error)
