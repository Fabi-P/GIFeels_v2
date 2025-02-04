from flask import render_template, request, redirect, Blueprint, current_app


error = Blueprint('error', __name__)

@error.errorhandler(429)
def error_handler(error):
    current_app.logger.error(f"Error occurred at route: {request.path} (method: {request.method}) - Error: {error}")
    return render_template("429error.html")


@error.errorhandler(Exception)
def error_handler(error):
    current_app.logger.error(f"Error occurred at route: {request.path} (method: {request.method}) - Error: {error}")
    if request.referrer != 'http://127.0.0.1:8443/' and request.referrer != 'https://www.gifeels.co.uk/':
        return redirect(request.referrer)
    return render_template("disaster.html")
