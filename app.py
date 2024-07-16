from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # HTML template with the Uber Fare Estimate widget embedded
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Uber Fare Estimates</title>
    </head>
    <body>
        <h1>Uber Fare Estimates</h1>
        <div id="uber-fare-estimate-widget"></div>
        <script>
            var uberWidgetOptions = {
                pickup: {
                    formatted_address: "Central Park, New York, NY"
                },
                dropoff: {
                    formatted_address: "Times Square, New York, NY"
                }
            };
            (function() {
                var script = document.createElement("script");
                script.type = "text/javascript";
                script.async = true;
                script.src = "https://www.uber.com/webwidgets/price-estimate.js";
                var s = document.getElementsByTagName("script")[0];
                s.parentNode.insertBefore(script, s);
            })();
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
