from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# In-memory storage for simplicity
datasets = {}
experiments = {}
models = {}
recommendations = {}

@app.route('/datasets', methods=['POST'])
def upload_dataset():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    dataset_id = str(len(datasets) + 1)
    datasets[dataset_id] = file.read()  # Store the file in memory
    return jsonify({"message": "Dataset uploaded successfully", "dataset_id": dataset_id}), 200

@app.route('/experiments', methods=['POST'])
def create_experiment():
    data = request.json
    experiment_id = str(len(experiments) + 1)
    experiments[experiment_id] = {
        "name": data['name'],
        "dataset_id": data['dataset_id'],
        "config": data['config'],
        "results": None
    }
    return jsonify({"message": "Experiment created successfully", "experiment_id": experiment_id}), 201

@app.route('/experiments/<experiment_id>', methods=['GET'])
def get_experiment_results(experiment_id):
    if experiment_id not in experiments:
        return jsonify({"error": "Experiment not found"}), 404
    return jsonify(experiments[experiment_id]), 200

@app.route('/experiments/<experiment_id>', methods=['DELETE'])
def delete_experiment(experiment_id):
    if experiment_id not in experiments:
        return jsonify({"error": "Experiment not found"}), 404
    del experiments[experiment_id]
    return jsonify({"message": "Experiment deleted successfully"}), 204

@app.route('/recommendations', methods=['POST'])
def generate_recommendations():
    data = request.json
    user_id = data['user_id']
    model_id = data['model_id']
    top_n = data['top_n']
    # For simplicity, return dummy recommendations
    recommendations[user_id] = [f"Item {i}" for i in range(1, top_n + 1)]
    return jsonify({"recommendations": recommendations[user_id]}), 200

@app.route('/models', methods=['POST'])
def train_model():
    data = request.json
    model_id = str(len(models) + 1)
    models[model_id] = {
        "name": data['name'],
        "dataset_id": data['dataset_id'],
        "config": data['config'],
        "status": "training"
    }
    return jsonify({"message": "Model training initiated", "model_id": model_id}), 201

@app.route('/models/<model_id>', methods=['GET'])
def get_model_details(model_id):
    if model_id not in models:
        return jsonify({"error": "Model not found"}), 404
    return jsonify(models[model_id]), 200

@app.route('/models/<model_id>', methods=['DELETE'])
def delete_model(model_id):
    if model_id not in models:
        return jsonify({"error": "Model not found"}), 404
    del models[model_id]
    return jsonify({"message": "Model deleted successfully"}), 204

@app.route('/metrics', methods=['GET'])
def retrieve_metrics():
    experiment_id = request.args.get('experiment_id')
    if experiment_id not in experiments:
        return jsonify({"error": "Experiment not found"}), 404
    # Return dummy metrics for simplicity
    metrics = {"accuracy": 0.95, "precision": 0.9, "recall": 0.85}
    return jsonify(metrics), 200

if __name__ == '__main__':
    app.run(debug=True)

