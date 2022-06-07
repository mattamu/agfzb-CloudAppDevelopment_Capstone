
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    # my IAM_API_KEY
    authenticator = IAMAuthenticator("SzJ5tNAzMZS3OpYTLkzOAxaBU-0lckN8L-4WF9EFmAT2")
    service = CloudantV1(authenticator=authenticator)
    # my COUCH_URL
    service.set_service_url("https://dfce011a-67e6-4ba7-83b3-f4e4b904b87e-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
        db='reviews',
        selector={'dealership': {'$eq': int(dict["id"])}},
        ).get_result()
    try:
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
