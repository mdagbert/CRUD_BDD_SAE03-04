import copy

from flask import Flask, request, render_template, redirect, url_for, abort, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

# test
@app.route('/')
def show_accueil():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run()


def generate_flash_message(flashName, flashList):
    message = f'{flashName},<br>'
    for key in flashList.keys():
        if key == 'Modifier' or key == "Valider":  # ne pas modifier
            break
        value = flashList.getlist(key)[0]
        message += f'{key}: {value}<br>'

    flash(message, 'alert-success')
