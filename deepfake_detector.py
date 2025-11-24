import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DeepFakeDetector:
    
    def __init__(self, model_path="cvt_deepfake_model.h5"):
        self.model_path = model_path
        self.model = self._load_model()
        print(f"✅ Detector initialized. Using mocked model: {self.model_path}")
    
    def _load_model(self):
        
        return "Loaded Convolutional Vision Transformer (CVT)"

    def preprocess_video(self, video_path):
        
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found at: {video_path}")
        
        
        print(f"\n[Module 1] Processing video: {os.path.basename(video_path)}...")
        total_frames = 120
        
        
        processed_frames = np.random.rand(total_frames, 256, 256, 3) 
        
        print(f"   -> Extracted and normalized {total_frames} frames.")
        
        
        
        return processed_frames, total_frames

    def run_inference(self, processed_frames, frame_count):
        
        print(f"[Module 2] Running spatiotemporal inference...")
        
        
        
        scores = np.random.uniform(low=0.1, high=0.3, size=frame_count)
        
        
        mid_point = frame_count // 2
        scores[mid_point-10:mid_point+10] = np.random.uniform(low=0.7, high=0.95, size=20)
        
        
        aggregate_fake_prob = np.mean(scores)
        
        print(f"   -> Inference complete. Aggregate Fake Probability: {aggregate_fake_prob:.4f}")
        
        return scores, aggregate_fake_prob

    def generate_report(self, frame_scores, aggregate_prob, threshold=0.5):
        
        print("\n[Module 3] Generating final report and visualization...")
        
        
        if aggregate_prob > threshold:
            verdict = "FAKE"
            rationale = "High probability of manipulation detected."
        else:
            verdict = "REAL"
            rationale = "Video is consistent with authentic footage."
        
        print(f"   -> FINAL VERDICT: The video is classified as {verdict} (Score: {aggregate_prob:.4f})")
        
        
        df = pd.DataFrame({
            'Frame Index': range(len(frame_scores)),
            'Fake Probability': frame_scores
        })
        
        plt.figure(figsize=(10, 4))
        plt.plot(df['Frame Index'], df['Fake Probability'], label='Frame-wise Fake Probability')
        plt.axhline(y=threshold, color='r', linestyle='--', label='Detection Threshold')
        plt.title(f'DeepFake Detection Analysis: Verdict = {verdict}')
        plt.xlabel('Frame Index')
        plt.ylabel('Probability of FAKE')
        plt.ylim(0, 1)
        plt.legend()
        report_filename = f"detection_report_{time.strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(report_filename)
        plt.close()
        
        print(f"   -> Visualization saved to {report_filename}")
        
        
        log_entry = {
            'timestamp': time.time(),
            'verdict': verdict,
            'aggregate_score': aggregate_prob,
            'report_file': report_filename,
            'model_used': self.model_path
        }
        
        print(f"   -> Logged detection event: {log_entry['verdict']} at {log_entry['timestamp']}")
        
        return verdict, rationale, report_filename


if __name__ == "__main__":
    
    
    detector = DeepFakeDetector()
    mock_video_file = "sample_media/suspect_video.mp4"
    
    
    os.makedirs('sample_media', exist_ok=True)
    with open(mock_video_file, 'w') as f:
        f.write("This is a mock video file content.")
    
    try:
        
        processed_data, frame_count = detector.preprocess_video(mock_video_file)
        
        
        frame_scores, aggregate_prob = detector.run_inference(processed_data, frame_count)
        
        
        final_verdict, details, report_path = detector.generate_report(frame_scores, aggregate_prob)
        
        print("\n=== Project Execution Summary ===")
        print(f"Input: {mock_video_file}")
        print(f"Output: {final_verdict} | Details: {details}")
        print(f"Report: {report_path}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        
    finally:
        
        os.remove(mock_video_file)
        os.rmdir('sample_media')