import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

import config


class TicketPredictor:

    def __init__(self):

        # Load Models
        self.category_model = load_model(config.CATEGORY_MODEL_PATH)
        self.priority_model = load_model(config.PRIORITY_MODEL_PATH)

        # Load Tokenizers
        with open(config.CATEGORY_TOKENIZER_PATH, "rb") as f:
            self.category_tokenizer = pickle.load(f)

        with open(config.PRIORITY_TOKENIZER_PATH, "rb") as f:
            self.priority_tokenizer = pickle.load(f)

        # Load Label Encoders
        with open(config.CATEGORY_LABEL_ENCODER_PATH, "rb") as f:
            self.category_encoder = pickle.load(f)

        with open(config.PRIORITY_LABEL_ENCODER_PATH, "rb") as f:
            self.priority_encoder = pickle.load(f)

    def predict(self, ticket_text):

        # Category Prediction
        category_seq = self.category_tokenizer.texts_to_sequences([ticket_text])
        category_pad = pad_sequences(
            category_seq,
            maxlen=config.MAX_SEQUENCE_LENGTH,
            padding="post"
        )

        category_pred = self.category_model.predict(category_pad, verbose=0)
        category_index = np.argmax(category_pred)

        ticket_category = self.category_encoder.inverse_transform(
            [category_index]
        )[0]

        # Priority Prediction
        priority_seq = self.priority_tokenizer.texts_to_sequences([ticket_text])
        priority_pad = pad_sequences(
            priority_seq,
            maxlen=config.MAX_SEQUENCE_LENGTH,
            padding="post"
        )

        priority_pred = self.priority_model.predict(priority_pad, verbose=0)
        priority_index = np.argmax(priority_pred)

        ticket_priority = self.priority_encoder.inverse_transform(
            [priority_index]
        )[0]

        return ticket_category, ticket_priority