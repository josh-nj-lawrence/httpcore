import httpcore
import json

"""
    Following Quickstart guide to familiarize with the tool: https://www.encode.io/httpcore/quickstart/
"""

response = httpcore.request("GET", "https://www.coinsandcanada.com/coins-prices.php")

print(response)
print(response.status)
print(response.headers)
#print(response.content)

# Testing request headers as a dictionary (or as a list of two-tuples)
headers = {'User-Agent':'httpcore'}
r1 = httpcore.request("GET","https://httpbin.org/headers", headers=headers)
print(json.loads(r1.content))

# Request Body can be included either as bytes or as an iterable that returns bytes
r2 = httpcore.request('POST', 'https://httpbin.org/post', content=b'Hello, world')
print(json.loads(r2.content))

with open("hello-world.txt", "rb") as input_file:
    r3 = httpcore.request('POST','https://httpbin.org/post', content=input_file)
print(json.loads(r3.content))

# Dealing with a streaming response
with httpcore.stream("GET",'https://twitter.com/') as r4:
    for chunk in r4.iter_stream():
        print(f"Downloaded: {chunk}")

# More complete example that demonstrates downloading a response
with httpcore.stream('GET','https://speed.hetzner.de/100MB.bin') as r5:
    with open("download.bin","wb") as output_file:
        for chunk in r5.iter_stream():
            output_file.write(chunk)

with httpcore.stream('GET','https://speed.hetzner.de/100MB.bin') as r6:
    content_length = [int(v) for k, v in r6.headers if k.lower() == b'content-length'][0]
    if content_length > 100_000_000:
        raise Exception("Response too large.")
    r6.read() # response.content is now available.
