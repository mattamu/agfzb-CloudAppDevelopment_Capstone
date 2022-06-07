import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    # my IAM_API_KEY
    authenticator = IAMAuthenticator("SzJ5tNAzMZS3OpYTLkzOAxaBU-0lckN8L-4WF9EFmAT2")
    service = CloudantV1(authenticator=authenticator)
    # my COUCH_URL
    service.set_service_url("https://722b0a8f.eu-gb.apigw.appdomain.cloud/capstone")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
