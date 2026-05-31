"""Unit tests for emotion detection application."""
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy(self):
        """Test that joy is detected correctly."""
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test that anger is detected correctly."""
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test that disgust is detected correctly."""
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test that sadness is detected correctly."""
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test that fear is detected correctly."""
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()