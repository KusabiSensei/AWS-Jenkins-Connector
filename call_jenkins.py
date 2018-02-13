#!/usr/bin/env python
#
# Call a Jenkins Server from AWS Lambda
# 
# This isn't a complicated thing. All we need to do is get the incoming message,
# figure out what needs to be called on Jenkins, fetch a crumb, and then do it.
import requests

def lambda_handler(event, context):
    source_arn = event['Records'][0]['eventSourceARN']
    region = source_arn.split(":")[3]
    repository = source_arn.split(":")[5]
    url = 'http://<JENKINS_URI>/job/'+region+'/job/'+repository+'/build'
    call = requests.get('http://<JENKINS_URI>/crumbIssuer/api/json',
                        auth=('<JENKINS_USER>', '<JENKINS_API_TOKEN>'))
    response = call.json()
    crumb = response.get('crumb')
    field = response.get('crumbRequestField')
    headers = {field:crumb}
    call = requests.post(url, headers=headers,
                         auth=('<JENKINS_USER>', '<JENKINS_API_TOKEN>'))
