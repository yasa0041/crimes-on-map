from flask import Flask, render_template
from elasticsearch import helpers, Elasticsearch
import elasticsearch
from kafka import KafkaProducer
import json

#import routes
from routes.handlers import routes_bp

app = Flask(__name__)

@app.route('/')
def root():
    return status()

@app.route('/status')
def status():
    return render_template("status.html")

def getDataSchema(es_index):
    es = Elasticsearch([app.config['ELASTIC_CONNCETION']])
    ind_client = elasticsearch.client.IndicesClient(es)

    fields = list(ind_client.get_mapping()[es_index]['mappings']['type']['properties'].keys())
    print(es_index + " fields : " + str(fields))
    
    return fields

def createKafkaProducer():
    producer = KafkaProducer(bootstrap_servers=['35.232.117.118:9092'], 
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                        api_version = (0,10))
    print("Created Kafka producer")
    return producer

if __name__ == '__main__':

    print("Setting Server Config")
    app.config['UPLOAD_FOLDER'] = './user-uploaded-csv'
    app.config['ELASTIC_CONNCETION'] = {'host': '34.73.60.209', 'port': 9200}
    app.config['ELASTIC_INDEX'] = 'combined_crimes'

    print("Running Prequisites")
    app.config['DATA_COLS'] = getDataSchema(app.config['ELASTIC_INDEX'])
    app.config['KAFKA_PRODUCER'] = createKafkaProducer()
    app.config['KAFKA_TOPIC'] = 'crimes'

    print("Registering blueprints")
    app.register_blueprint(routes_bp)

    print("Starting Server on 0.0.0.0")
    app.run(debug=True, host='0.0.0.0')
