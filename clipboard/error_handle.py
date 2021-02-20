from flask import (
    render_template
)


def error_404(error):
    return render_template('error/404.html', error=error)
