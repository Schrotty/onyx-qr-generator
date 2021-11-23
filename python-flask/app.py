from flask import Flask, request
import werkzeug, logging, structlog

structlog.configure(processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
logging.basicConfig(level=logging.INFO)
logging = structlog.get_logger("flask")

app = Flask(__name__)

@app.route("/")
def index():
    log = logging.bind(addr=request.remote_addr, url=request.url, method=request.method, headers=dict(request.headers), params=request.args)
    log.info("Success")
    return "A warm myLab welcome from Python <a href='https://flask.palletsprojects.com'>Flask</a>"

@app.errorhandler(werkzeug.exceptions.NotFound)
def not_found(ex):
    log = logging.bind(addr=request.remote_addr, url=request.url, method=request.method, headers=dict(request.headers), params=request.args)
    log.error("Not found", error=str(ex))
    return f"Not found ({ ex }) ", 404

# print("Starting ...")
app.run(host="0.0.0.0", port=8080)