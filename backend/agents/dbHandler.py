import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase (replace with your credentials)
cred = credentials.Certificate("enter path to credential.json file here")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_collection_data(collection_name):
    """Retrieves data from a Firestore collection."""
    collection_ref = db.collection(collection_name)
    docs = collection_ref.get()
    data = [doc.to_dict() for doc in docs]
    return data

def get_collection_data_in_doc(collection_name, doc_id):
    """Retrieves data from a collection within a document."""
    doc_ref = db.collection(collection_name).document(doc_id)
    subcollection_ref = doc_ref.collection(collection_name)
    docs = subcollection_ref.get()
    data = [doc.to_dict() for doc in docs]
    return data


def get_project_data(project):
    collection_data = get_collection_data(project)

    # print(collection_data)

    webpage_description=[]

    for docs in collection_data:
        '''
            1 ==> project_description
            3 ==> webpage_names_array
            4 ==> webpage_description_array
            5 ==> project_name

        '''

        if docs['question_num']==1:
            project_description=docs['answer']
            
        if docs['question_num']==3:
            webpage_names=docs['answer']

        if docs['question_num']==4:
            webpage_descriptions=docs['answer']
        
        if docs['question_num']==5:
            project_name=docs['answer']

    no_of_webpages=len(webpage_names)
    project_data={"project_name":project_name , "project_description":project_description , "no_of_webpages":no_of_webpages , "webpage_names":webpage_names , "webpage_descriptions":webpage_descriptions}
    
    return project_data