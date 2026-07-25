# Flask Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000


# ==========================
# Model Paths
# ==========================

CATEGORY_MODEL_PATH = r"artifacts\ticket_category_model.keras"

PRIORITY_MODEL_PATH = r"artifacts\ticket_priority_model.keras"


# ==========================
# Tokenizer Paths
# ==========================

CATEGORY_TOKENIZER_PATH = r"artifacts\tokenizer.pkl"

PRIORITY_TOKENIZER_PATH = r"artifacts\priority_tokenizer.pkl"


# ==========================
# Label Encoder Paths
# ==========================

CATEGORY_LABEL_ENCODER_PATH = r"artifacts\label_encoder.pkl"

PRIORITY_LABEL_ENCODER_PATH = r"artifacts\priority_label_encoder.pkl"


# ==========================
# Text Configuration
# ==========================

MAX_SEQUENCE_LENGTH = 100

# MongoDB Configuration

MONGO_URL = "mongodb://localhost:27017"

DB_NAME = "customer_support_ticket_db"

PREDICTION_COLLECTION = "ticket_predictions"