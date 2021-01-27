from flask import Flask, request #import main Flask class and request object
import subprocess

app = Flask(__name__) #create the Flask app
bashCommand = "mpg123 /home/smartroom/audio/music.mp3"

@app.route('/', methods=['POST'])
def query_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        music = request.form.get('music')
    if music == '1':
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    return "Music!!!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000
