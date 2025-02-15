from flask import Flask, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# Initialize BigQuery client
client = bigquery.Client()

# Define SQL Query
query = """
SELECT SUM(Sales) AS total_sales, CURRENT_TIMESTAMP() AS calculated_at
FROM `rosy-acolyte-450607-t8.My_Dataset.My_Sales`
"""

@app.route('/sales-summary', methods=['GET'])
def fetch_sales_data():
    try:
        query_job = client.query(query)
        result = query_job.result()

        for row in result:
            return jsonify({
                "total_sales": row.total_sales,
                "timestamp": row.calculated_at
            })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Additional route for the base URL
@app.route('/')
def home():
    return "Cloud Run Service is up and running! Visit /sales-summary to see the sales data."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


