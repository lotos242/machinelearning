# coding: utf-8
def list_notebooks(client):
    """List Sagemaker Notebooks
    
       args: client: boto3 low level client object
       
       returns: List of notebooks
    """
    
    retlist = []
    nlist = client.list_notebook_instances()['NotebookInstances']
    for nb in nlist:
        retlist.append(nb['NotebookInstanceName'])
    return retlist
def show_notebook_status(client, notebook):
    nlist = client.list_notebook_instances()['NotebookInstances']
    if len(nlist) == 0:
        print("No notebooks found")
        return 
    for nb in nlist:
        if nb['NotebookInstanceName'] == notebook:
            print("{} status: {}".format(notebook,nb['NotebookInstanceStatus']))
            return
    print("{} not found".format(notebook))
    
def get_url(client, notebook):
    nlist = client.list_notebook_instances()['NotebookInstances']
    for nb in nlist:
        if nb['NotebookInstanceName'] == notebook:
            print("{} Url: https://{}".format(notebook, nb['Url']))
            
def list_buckets(client):
    names = []
    resp = client.list_buckets()
    bucks = resp['Buckets']
    for buck in bucks:
        names.append(buck['Name'])
    return names
def create_clients(services, access_key, secret_key, region='us-east-1'):
    import boto3
    clients = []
    for service in services:
        client = boto3.client(service, aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name=region)
        clients.append(client)
    
    return clients
def create_resources(services, access_key, secret_key, region='us-east-1'):
    import boto3
    resources = []
    for service in services:
        resource = boto3.resource(service, aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                  region_name=region)
        resources.append(resource)
    return resources
