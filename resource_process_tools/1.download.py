import os
import requests
"""
curl 'https://s172-30-138-61p8888.lab-aws-production.deeplearning.ai/api/contents?type=directory&_=1722429296126' \
  -H 'cookie: _hjSessionUser_3196229=eyJpZCI6IjZiNjJmN2VmLTg1ZmItNTEwZC04Mzc2LWRhNWFlNzQzZGFiMCIsImNyZWF0ZWQiOjE3MDk4Mjk1NDk4MzMsImV4aXN0aW5nIjp0cnVlfQ==; hubspotutk=8c9114d14a7e6340595713bdbc37f0db; _fbp=fb.1.1717136336786.1050233746; ajs_anonymous_id=3c5931c7-b56c-40a0-9a5b-d01affd22623; _gid=GA1.2.1528884748.1722411536; _ga=GA1.1.402070950.1717136332; _ga_PZF1GBS1R1=GS1.1.1722416739.7.1.1722421463.60.0.0; _ga_7G5P0RV3XD=GS1.1.1722419096.8.1.1722421463.60.0.0; __hssrc=1; cf_clearance=vCyDV5TbGY3rH7c5QVMCzqIr1Xmv63cJunkTYtFc44E-1722428892-1.0.1.1-Ftq3Drpe8c9TSitUsuKN3PyoNs_IPCMVJLuyOqq_rCuuWkOGvPZb55NEKBaTdfG1m3opcH7etKjAbHyDVKYcfw; _ga_BQMBGW8LLT=GS1.1.1722429209.26.1.1722429210.59.0.0; _ga_FR2MZ1VLMS=GS1.1.1722429209.25.1.1722429210.59.0.0; __hstc=28198563.8c9114d14a7e6340595713bdbc37f0db.1717136334907.1722426234972.1722429210579.26; __hssc=28198563.1.1722429210579; _hjSession_3196229=eyJpZCI6IjI0MGE2NjY5LWY3MzgtNDBjOC04ODc0LTkwMDBmZWEyMTg3ZiIsImMiOjE3MjI0MjkyMTA4MzQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; username-s172-30-138-61p8888-lab-aws-production-deeplearning-ai="2|1:0|10:1722429227|63:username-s172-30-138-61p8888-lab-aws-production-deeplearning-ai|44:ZTU1ZTFlYjg2OWNhNDg3ZjhiYWJhMDBlMDk0ZTMxOTA=|bf18b89984398e1a5025795e4cce05cdb60e685dee431a635768ad9ac7b2308f"; _xsrf=2|6698ddfb|9da4b3246e3e33a08bb3d13cd33429f0|1722429227; ph_VfwpB7hg0i5IkyEVw5zgUuuSRjKtUwajwjNBON3mRRc_posthog=%7B%22distinct_id%22%3A%221464873%22%2C%22%24sesid%22%3A%5B1722429289624%2C%22019108c7-f47e-7ef7-808b-583f9d42beb5%22%2C1722429207678%5D%2C%22%24epp%22%3Atrue%7D; _ga_TD3C44Z6EH=GS1.1.1722426136.24.1.1722429294.0.0.0' \
  -H 'referer: https://s172-30-138-61p8888.lab-aws-production.deeplearning.ai/tree' \
  -H 'x-xsrftoken: 2|6698ddfb|9da4b3246e3e33a08bb3d13cd33429f0|1722429227'
"""
# Define the root URL and local root directory
root_url = 'https://s172-30-138-61p8888.lab-aws-production.deeplearning.ai/api/contents'
local_root_dir = './downloaded_files'

# Define the headers for the request
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://s172-30-138-61p8888.lab-aws-production.deeplearning.ai/tree',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'cookie': '_hjSessionUser_3196229=eyJpZCI6IjZiNjJmN2VmLTg1ZmItNTEwZC04Mzc2LWRhNWFlNzQzZGFiMCIsImNyZWF0ZWQiOjE3MDk4Mjk1NDk4MzMsImV4aXN0aW5nIjp0cnVlfQ==; hubspotutk=8c9114d14a7e6340595713bdbc37f0db; _fbp=fb.1.1717136336786.1050233746; ajs_anonymous_id=3c5931c7-b56c-40a0-9a5b-d01affd22623; _gid=GA1.2.1528884748.1722411536; _ga=GA1.1.402070950.1717136332; _ga_PZF1GBS1R1=GS1.1.1722416739.7.1.1722421463.60.0.0; _ga_7G5P0RV3XD=GS1.1.1722419096.8.1.1722421463.60.0.0; __hssrc=1; cf_clearance=vCyDV5TbGY3rH7c5QVMCzqIr1Xmv63cJunkTYtFc44E-1722428892-1.0.1.1-Ftq3Drpe8c9TSitUsuKN3PyoNs_IPCMVJLuyOqq_rCuuWkOGvPZb55NEKBaTdfG1m3opcH7etKjAbHyDVKYcfw; _ga_BQMBGW8LLT=GS1.1.1722429209.26.1.1722429210.59.0.0; _ga_FR2MZ1VLMS=GS1.1.1722429209.25.1.1722429210.59.0.0; __hstc=28198563.8c9114d14a7e6340595713bdbc37f0db.1717136334907.1722426234972.1722429210579.26; __hssc=28198563.1.1722429210579; _hjSession_3196229=eyJpZCI6IjI0MGE2NjY5LWY3MzgtNDBjOC04ODc0LTkwMDBmZWEyMTg3ZiIsImMiOjE3MjI0MjkyMTA4MzQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; username-s172-30-138-61p8888-lab-aws-production-deeplearning-ai="2|1:0|10:1722429227|63:username-s172-30-138-61p8888-lab-aws-production-deeplearning-ai|44:ZTU1ZTFlYjg2OWNhNDg3ZjhiYWJhMDBlMDk0ZTMxOTA=|bf18b89984398e1a5025795e4cce05cdb60e685dee431a635768ad9ac7b2308f"; _xsrf=2|6698ddfb|9da4b3246e3e33a08bb3d13cd33429f0|1722429227; ph_VfwpB7hg0i5IkyEVw5zgUuuSRjKtUwajwjNBON3mRRc_posthog=%7B%22distinct_id%22%3A%221464873%22%2C%22%24sesid%22%3A%5B1722429289624%2C%22019108c7-f47e-7ef7-808b-583f9d42beb5%22%2C1722429207678%5D%2C%22%24epp%22%3Atrue%7D; _ga_TD3C44Z6EH=GS1.1.1722426136.24.1.1722429294.0.0.0',
    'x-xsrftoken': '2|6698ddfb|9da4b3246e3e33a08bb3d13cd33429f0|1722429227'
}
# %%
response = requests.get(root_url, headers=headers)
data = response.json()


# %%
# Function to download a file
def download_file(file_url, local_path):
    response = requests.get(file_url, headers=headers, stream=True)
    with open(local_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


# Function to process a directory
def process_directory(url, local_dir):
    response = requests.get(url, headers=headers)
    data = response.json()

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    for item in data['content']:
        item_name = item['name']
        item_path = item['path']
        item_type = item['type']

        if item_type == 'directory':
            process_directory(f"{root_url}/{item_path}", os.path.join(local_dir, item_name))
        else:
            file_url = f"https://s172-30-138-61p8888.lab-aws-production.deeplearning.ai/files/{item_path}?download=1"
            download_file(file_url, os.path.join(local_dir, item_name))


# Start processing from the root directory
process_directory(root_url, local_root_dir)

#%%
