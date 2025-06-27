from flask import Flask, send_file, abort
import os

app = Flask(__name__)

@app.route("/cn", methods=["GET"])
def download_file():
    file_path = "commands.txt"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        abort(404, description="Arquivo não encontrado.")

if __name__ == "__main__":
    app.run(debug=True)

