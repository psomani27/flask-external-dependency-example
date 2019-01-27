from flask import Flask
import time
import threading

app = Flask(__name__)

@app.route("/run")
def index():
    def handle_sub_view():
        l=[3,5,7,14,21]
        for loop in l:
            print("Hello World!")
            time.sleep(1)
    threading.Thread(target=handle_sub_view).start()
    return "Hello World!"

@app.route("/test")
def test():
    return "Server is working!"

if __name__ == '__main__':
   app.run()
