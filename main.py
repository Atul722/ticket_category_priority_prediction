from flask import Flask, render_template, request
import config
from src.utils import TicketPredictor

# Flask App
app = Flask(__name__)

# Load Models (sirf ek baar startup par)
predictor = TicketPredictor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # User input
    ticket_text = request.form.get("ticket_text")

    # Validation
    if not ticket_text or ticket_text.strip() == "":
        return render_template(
            "index.html",
            error="Please enter a ticket description."
        )

    # Prediction
    ticket_category, ticket_priority = predictor.predict(ticket_text)

    return render_template(
        "index.html",
        ticket_category=ticket_category,
        ticket_priority=ticket_priority
    )


if __name__ == "__main__":
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=True
    )