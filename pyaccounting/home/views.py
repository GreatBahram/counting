# third-party imports
from flask import abort, render_template
from flask_login import current_user, login_required

# local imports
from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Render the dashboard template on the /admin/dashboard route
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Admin Dashboard")

@home.route('/about')
def aboutpage():
    """
    Render the homepage template on the /about route
    """
    return render_template('home/about.html', title="About Us")

