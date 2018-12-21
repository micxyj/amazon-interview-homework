from flask import Flask, jsonify, request, render_template
import boto3
from boto3.session import Session

app = Flask(__name__)

#主页
@app.route('/')
def main_page():
    return render_template('work.html')

#快照服务
@app.route('/createsnapshot', methods=['post'])
def createsnapshot():
    client = boto3.client('ec2', region_name='YOUR_REGION', 
        aws_access_key_id='YOUR_ID', 
        aws_secret_access_key='YOUR_KEY')
    response = client.create_snapshot(Description='This is my root volume snapshot.',
        VolumeId='YOUR_VID')
    return jsonify(response)

#文件上传服务
@app.route('/upload', methods=['post'])
def upload():
    aws_key = 'YOUR_ID'
    aws_secret = 'YOUR_KEY'
    session = Session(aws_access_key_id=aws_key, 
        aws_secret_access_key=aws_secret, region_name='YOUR_REGION')
    s3 = session.resource('s3')
    client = session.client('s3')
    bucket = 'YOUT_BUCKET_NAME'
    upload_data = request.files['filename']
    upload_key = 'test1'
    file_obj = s3.Bucket(bucket).put_object(Key=upload_key, Body=upload_data)
    return 'finished'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
