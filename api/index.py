from vercel_wsgi import handle_request
from online_learning_management_portal.wsgi import application

def handler(request, context):
    return handle_request(request, application)