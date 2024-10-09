from flask import (
    Flask,
    request,
    Response,
    send_from_directory,
    send_file,
    jsonify,
    abort,
)
import json
import model_pb2_grpc as analyzer_service
import model_pb2 as analyzer
import grpc

app = Flask(__name__)

stub = None  # initialized during a remote procedure call

is_not_null = lambda x: x is not None


def get_file_content(file_name: str) -> str:
    out = ""
    try:
        f = open(file_name)
        out = f.read()
        f.close()
    except Exception as e:
        out = "File not found!"
    return out


@app.route("/vendor/<path:path>", methods=["GET"])
def vendor(path: str) -> Response:
    return send_from_directory("vendor", path)


@app.route("/", methods=["GET"])
def index():
    c = get_file_content("editor.html")
    return Response(c, mimetype="text/html")


def analyze_internal(code_buffer: str, name: str):
    global stub
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = analyzer_service.AnalyzerStub(channel)
        response: analyzer.AnalyzeResponse = stub.DoAnalyze(
            analyzer.AnalyzeRequest(name=name, code=code_buffer)
        )
        if is_not_null(response):
            status = response.status
            report = response.report
            # looks like python took a few pages off of rust's book!
            match status:
                case analyzer.Status.Ok:
                    out_dict = {"status": "Ok", "message": report}
                case analyzer.Status.Err:
                    out_dict = {
                        "status": "Error",
                        "message": "The given code is either structually invalid or cannot be parsed",
                    }
            return jsonify(out_dict)
        return "Invalid request"


@app.route("/api/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "GET":
        return abort(501, "Not implemented yet!")
    code = request.json.get("code_buffer")  # translated into code later
    name = request.json.get("name")
    return analyze_internal(code, name)


if __name__ == "__main__":
    app.run()
