import numpy as np

def detect_heart_anomalies(ecg_signal, fs):
    """
    Detects heart anomalies from ECG data.

    Args:
        ecg_signal (np.ndarray): The input ECG signal (1D NumPy array).
        fs (int): Sampling frequency in Hz.

    Returns:
        dict: Anomalies detected. Keys include 'arrhythmia', 'bradycardia', 'tachycardia'.
    """
    from scipy.signal import find_peaks

    # Find R-peaks (main upward spikes in normal ECG)
    distance = int(0.2 * fs)  # Approx minimum heart rate = 300 bpm
    peaks, _ = find_peaks(ecg_signal, distance=distance, height=np.mean(ecg_signal))

    if len(peaks) < 2:
        return {"error": "Too few R-peaks detected; check signal quality."}

    rr_intervals = np.diff(peaks) / fs  # RR intervals in seconds
    heart_rates = 60.0 / rr_intervals   # Heart rate in BPM

    anomalies = {
        "arrhythmia": False,
        "bradycardia": False,
        "tachycardia": False,
        "average_hr": float(np.mean(heart_rates)),
        "min_hr": float(np.min(heart_rates)),
        "max_hr": float(np.max(heart_rates)),
        "num_beats": int(len(peaks)),
    }

    # Bradycardia: HR < 60 bpm
    if np.any(heart_rates < 60):
        anomalies["bradycardia"] = True

    # Tachycardia: HR > 100 bpm
    if np.any(heart_rates > 100):
        anomalies["tachycardia"] = True

    # Arrhythmia: Significant irregularity in RR intervals
    rr_std = np.std(rr_intervals)
    if rr_std > 0.12:  # >120ms standard deviation in RR intervals is a rough threshold
        anomalies["arrhythmia"] = True
        anomalies["rr_std"] = float(rr_std)

    return anomalies

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Example: Simulate or load ECG data
    # For demo, create a signal with synthetic R-peaks
    fs = 250  # 250 Hz typical for ECG
    t = np.linspace(0, 10, fs*10)  # 10 seconds
    # Basic synthetic ECG: sum of sine + unit spikes for R-peaks
    ecg_signal = 0.04 * np.sin(2 * np.pi * 1.2 * t)  # Pseudo baseline
    r_peaks = np.arange(0.8, 10, 1)  # R-peak at 1 Hz (60 bpm)
    for r in r_peaks:
        idx = int(r * fs)
        if idx < len(ecg_signal):
            ecg_signal[idx:idx+2] += 1.0  # create R-peak

    anomalies = detect_heart_anomalies(ecg_signal, fs)
    print("Detected anomalies:", anomalies)

    # Plot for visual debug
    plt.figure(figsize=(10,4))
    plt.plot(t, ecg_signal, label='ECG Signal')
    detected_peaks, _ = __import__('scipy.signal').signal.find_peaks(ecg_signal, distance=int(0.2*fs), height=np.mean(ecg_signal))
    plt.plot(t[detected_peaks], ecg_signal[detected_peaks], 'rx', label='Detected R-peaks')
    plt.title("Synthetic ECG Signal with Detected R-Peaks")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()
