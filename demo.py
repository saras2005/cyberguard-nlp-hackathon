
from cyber_threat_detector import CyberThreatDetector
import pickle

def run_demo():
    # Load model
    with open('../model/cyber_threat_detector.pkl', 'rb') as f:
        detector = pickle.load(f)
    
    # Test case
    test_text = """
    Sophisticated APT using quantum computing.
    Multiple systems compromised.
    Data exfiltration detected.
    """
    
    # Analyze
    result = detector.analyze_threat(test_text)
    
    # Print results
    print(f"Category: {result['category']}")
    print(f"Confidence: {result['confidence']:.4f}")
    print(f"Severity: {result['severity']:.2f}")
    print(f"Level: {result['severity_level']}")

if __name__ == "__main__":
    run_demo()
