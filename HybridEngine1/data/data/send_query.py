
import json
import predictionio

engine_client = predictionio.EngineClient(url="http://localhost:8000")
PredictionOutput = engine_client.send_query({"user": "642", "num": 12})
print PredictionOutput

json.dump(PredictionOutput, open("txtop.txt",'w'), indent=4)
