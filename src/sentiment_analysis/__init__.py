"""Kinetic Anomaly Detection Engine System (KADES)

Sentiment Analysis Module

This module implements social media sentiment analysis and NLP processing
for detecting market manipulation and crowd sentiment in memecoin communities.

Author: KADES Team
License: Proprietary"""

from .social_scraper import SocialScraper
from .nlp_processor import NLPProcessor
from .embedding_models import EmbeddingModel
from .sentiment_scorer import SentimentScorer

__version__ = '1.0.0'
__author__ = 'KADES Team'
__email__ = 'contact@kades.ai'

__all__ = [
    'SocialScraper',
    'NLPProcessor',
    'EmbeddingModel',
    'SentimentScorer',
]

# Default NLP configuration
DEFAULT_NLP_CONFIG = {
    'model_type': 'bert-base-uncased',
    'max_length': 512,
    'batch_size': 32,
    'cache_dir': './models/nlp',
}

# Supported platforms
SUPPORTED_PLATFORMS = [
    'x',
    'telegram',
    'discord',
    'reddit',
    'youtube'
]
