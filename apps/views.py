# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='index', parent='dashboard')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404


# Pages Components

@app.route('/pages/components/bc_button/')
def pages_components_bc_button():
  return render_template('pages/components/bc_button.html', segment='button', parent='basic_components')

@app.route('/pages/components/bc_badges/')
def pages_components_bc_badges():
  return render_template('pages/components/bc_badges.html', segment='badges', parent='basic_components')

@app.route('/pages/components/bc_breadcrumb-pagination/')
def pages_components_bc_breadcrumb_pagination():
  return render_template('pages/components/bc_breadcrumb-pagination.html', segment='breadcrumbs_&_pagination', parent='basic_components')

@app.route('/pages/components/bc_collapse/')
def pages_components_bc_collapse():
  return render_template('pages/components/bc_collapse.html', segment='collapse', parent='basic_components')

@app.route('/pages/components/bc_tabs/')
def pages_components_bc_tabs():
  return render_template('pages/components/bc_tabs.html', segment='navs_&_tabs', parent='basic_components')

@app.route('/pages/components/bc_typography/')
def pages_components_bc_typography():
  return render_template('pages/components/bc_typography.html', segment='typography', parent='basic_components')

@app.route('/pages/components/icon-feather/')
def pages_components_icon_feather():
  return render_template('pages/components/icon-feather.html', segment='feather_icon', parent='basic_components')

# Pages

@app.route('/pages/form_elements/')
def pages_form_elements():
  return render_template('pages/form_elements.html', segment='form_elements', parent='form_components')

@app.route('/pages/tbl_bootstrap/')
def pages_tbl_bootstrap():
  return render_template('pages/tbl_bootstrap.html', segment='basic_tables', parent='tables')

@app.route('/pages/chart-morris/')
def pages_chart_morris():
  return render_template('pages/chart-morris.html', segment='morris_chart', parent='chart')

@app.route('/pages/map-google/')
def pages_map_google():
  return render_template('pages/map-google.html', segment='google_maps', parent='maps')

@app.route('/pages/profile/')
def pages_profile():
  return render_template('pages/profile.html', segment='profile', parent='pages')

@app.route('/pages/sample-page/')
def pages_sample_page():
  return render_template('pages/sample-page.html', segment='sample_page', parent='pages')

# Accounts

@app.route('/accounts/auth-signup/')
def accounts_auth_signup():
  return render_template('accounts/auth-signup.html', segment='auth_signup', parent='accounts')

@app.route('/accounts/auth-signin/')
def accounts_auth_signin():
  return render_template('accounts/auth-signin.html', segment='auth_signin', parent='accounts')

@app.route('/accounts/auth-reset-password/')
def accounts_auth_reset_password():
  return render_template('accounts/auth-reset-password.html', segment='auth_reset_password', parent='accounts')

@app.route('/accounts/auth-password-reset-done/')
def accounts_auth_password_reset_done():
  return render_template('accounts/auth-password-reset-done.html', segment='auth_password_reset_done', parent='accounts')

@app.route('/accounts/auth-password-reset-confirm/')
def accounts_auth_password_reset_confirm():
  return render_template('accounts/auth-password-reset-confirm.html', segment='auth_password_reset_confirm', parent='accounts')

@app.route('/accounts/auth-password-reset-complete/')
def accounts_auth_password_reset_complete():
  return render_template('accounts/auth-password-reset-complete.html', segment='auth_password_reset_complete', parent='accounts')

@app.route('/accounts/auth-change-password/')
def accounts_auth_change_password():
  return render_template('accounts/auth-change-password.html', segment='auth_change_password', parent='accounts')

@app.route('/accounts/auth-password-change-done/')
def accounts_auth_password_change_done():
  return render_template('accounts/auth-password-change-done.html', segment='auth_password_change_done', parent='accounts')

@app.template_filter(name = 'replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()