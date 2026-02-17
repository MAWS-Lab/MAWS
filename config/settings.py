"""
MAWS Configuration - Nanashi Ecosystem
"""
import os

class Settings:
    PROJECT_NAME = "MAWS v1.1"
    PROJECT_CODE = "SG195220" 
    ANONYMITY_LEVEL = "High"
    BLOCKCHAIN_AUDIT = True 
    SIMILARITY_THRESHOLD = 0.85
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
