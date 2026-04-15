from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
# Load our processed data
movies = joblib.load('recommender_data.pkl')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        genre = data.get('genre', 'Action')
        min_rating = data.get('min_rating', 4.0)

        # Recommendation Logic: Filter by genre and rating, then take top 5
        results = movies[(movies['Genre'] == genre) & 
                        (movies['Rating'] >= min_rating)]
        
        top_5 = results.sort_values(by='Rating', ascending=False).head(5)
        
        return jsonify({
            'recommendations': top_5.to_dict(orient='records'),
            'count': len(top_5),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
