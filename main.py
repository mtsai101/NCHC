from app import app
import threading
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True      
    app.jinja_env.auto_reload = True
    app.run(host='140.114.79.84', port=1234, debug=True)