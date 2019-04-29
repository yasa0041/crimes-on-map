import os
from datetime import datetime
from flask import current_app as app
import uuid


def remove_file(filename):
    os.remove(filename)
    print("Deleted file {}", filename)

def reportCrime(record):
    #Flatten dict
    record = {k:v[0] for k,v in record.items()}

    record['Date'] = datetime.now().strftime('%m/%d/%Y')
    record['Case_Id'] = str(uuid.uuid4().int & (1<<64)-1)
    #uuid.uuid4().__str__()
    record['Zipcode'] = '60601'
    return uploaSingleRecord(record)

def uploadCrimeRecord(filename):
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    fields = app.config['DATA_COLS']
    if sorted(fields) == sorted(list(df.columns)):
        print('Uploading to Kafka topic:', app.config['KAFKA_TOPIC'])
        df.apply(lambda x: app.config['KAFKA_PRODUCER'].send(app.config['KAFKA_TOPIC'] , value = x.to_dict()), axis=1)
    else:
        remove_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Incorrect Columns in the uploaded csv. The data fields of {} must match: {}'.format(filename, fields), 401
    
    return 'File uploaded successfully!'

def uploaSingleRecord(record):
    print("Kafka: Uploading \ndestination topic : {}\ndata : {}".format(app.config['KAFKA_TOPIC'], record))
    app.config['KAFKA_PRODUCER'].send(app.config['KAFKA_TOPIC'] , value = record)
    return "Thanks for reporting. Case ID : " + record['Case_Id'], 200