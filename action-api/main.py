from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from pymantic import sparql
import json

app = FastAPI()
client = OpenAI()

server = sparql.SPARQLServer('http://ec2-34-222-196-161.us-west-2.compute.amazonaws.com:9999/blazegraph/namespace/eia/sparql')

class Query(BaseModel):
    query: str

@app.post("/retrieve")
async def retrieve(query: Query):
    try:
        # Define the prompt with the ontology and the user's natural language query
        prompt = f"""Convert the natural language query below into SPARQL query using the provided ontology: @prefix ex: <http://example.com/> .

        ex:s ex:p ex:o .
        PREFIX : <http://eia.gov/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        #Regions
        :New_England a :Region ;
            :name "New England" ;
            :gas_point "Algonquin Citygate" ;
            :natural_gas_price "2.35"^^xsd:float ;
            :natural_gas_percent_change "+22.4"^^xsd:float ;
            :electricity_price "46.76"^^xsd:float ;
            :electricity_percent_change "+4.7"^^xsd:float ;
            :sparkSpread "30.31"^^xsd:float ;
            :power_point_used "Massachusetts Hub (ISONE)" .

        #Exports
        :Fuel_Exports a :Exports ;
            :unit "Quadrillion btu" .

        :Coal a :Fuel_Exports ;
            :year2022 "2.093"^^xsd:float ;
            :year2023 "2.405"^^xsd:float ;
            :march2024 "0.224"^^xsd:float ;
            :year2024 "0.811"^^xsd:float .

        #Renewable consumption
        :Renewable_Consumption a :Energy_Consumption ;
            :unit "trillion Btu" .

        :Hydroelectric_power a :Renewable_Consumption ;
            :source "Hydroelectric power" ;
            :year2020 "973"^^xsd:integer ;
            :year2021 "858"^^xsd:integer ;
            :year2022 "869"^^xsd:integer ;
            :year2023 "818"^^xsd:integer .

        Natural Language Query: {query.query}. Only include the query in the output starting with PREFIX."""

        # Forward the modified prompt to OpenAI's ChatGPT
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        # Extract and return the relevant part of the response
        chat_response = response.choices[0].message

        print(chat_response)

        # Executing query
        result = server.query(chat_response.content)
        
        prompt = "Using the below information, answer the provided question. Context: " + json.dumps(result, indent=4) + " . Question: " + query.query

        print(prompt)

        # Forward the modified prompt to OpenAI's ChatGPT
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract and return the relevant part of the response
        chat_response = response.choices[0].message


        return {"response": chat_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
