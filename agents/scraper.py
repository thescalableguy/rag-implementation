import random

def get_mythology_topics():
    topics = [
        "Concept of Dharma in Mahabharata",
        "Teachings of Bhagavad Gita on Karma",
        "Leadership lessons from Lord Rama",
        "Role of Krishna in Mahabharata",
        "Ashoka’s transformation after Kalinga war",
        "Concept of Moksha in Upanishads",
        "Significance of Guru in Vedic tradition",
        "Comparison between Ramayana and Mahabharata",
        "Ethics in Indian mythology",
        "Symbolism of Kurukshetra war"
    ]

    return random.sample(topics, 5)
