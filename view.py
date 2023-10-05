from flask import Flask, render_template
import os

app = Flask My Jenkins Task


@app.route('/')
def home():
    return "Hello Welcome to Jenkins Task"


if __name__ == "MY JENKINS PROJECT TASK":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
stage('Gmail')
{
	steps
	{
		emailext body: "*${currentBuild.currentResult}:* Job Name: 
                ${env.JOB_NAME} || Build Number: ${env.BUILD_NUMBER}\n More 
                information at: ${env.BUILD_URL}",
		subject: 'Declarative Pipeline Build Status',
		to: 'sree143nani.kushi@gmail.com'
	}
