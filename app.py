from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

def auto_load_data():
    print("Auto-loading CSV and audio files...")

@app.route('/')
def hello():
    return f'''
    <h1>Hello from Automated CI/CD Pipeline!</h1>
    <p><strong>Version:</strong> 2.0 - Automated Deployment</p>
    <p><strong>Deployed via:</strong> GitHub Actions + AWS SSM</p>
    <p><strong>Build Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p><strong>Assignment:</strong> Automated EC2 Deployment</p>
    '''

@app.route('/health')
def health():
    return {
        'status': 'healthy',
        'version': '2.0',
        'deployment_method': 'automated',
        'timestamp': datetime.now().isoformat()
    }

if __name__ == '__main__':
    auto_load_data()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)), debug=False)
