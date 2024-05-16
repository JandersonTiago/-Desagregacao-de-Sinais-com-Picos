import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter, find_peaks
import matplotlib.pyplot as plt
import os

# Função para aplicar a FFT
def apply_fft(signal):
    return np.fft.fft(signal)

# Função para identificar os picos no espectro de frequência
def identify_peaks(fft_result, threshold=0.2):
    # Encontrar picos usando a função find_peaks
    peaks, _ = find_peaks(np.abs(fft_result), height=threshold)
    
    # Retornar os índices dos picos no espectro
    return peaks

# Funções para projetar e aplicar filtros
def butter_lowpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_highpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def apply_filter(data, b, a):
    return lfilter(b, a, data)

# Carregar dados dos arquivos CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Função para realizar a desagregação
def perform_desaggregation(file_fft, file_signal, file_filtered, lowpass_cutoff, highpass_cutoff, fs, order=4):
    # Construir caminhos completos para os arquivos
    file_fft = os.path.join(base_path, file_fft)
    file_signal = os.path.join(base_path, file_signal)
    file_filtered = os.path.join(base_path, file_filtered)

    # Carregar dados
    fft_data = load_data(file_fft)
    signal_data = load_data(file_signal)
    
    # Aplicar FFT
    fft_result = apply_fft(signal_data['Amplitude'])

    # Identificar picos no espectro de frequência
    peaks = identify_peaks(fft_result)
    
    # Projetar filtros
    b_low, a_low = butter_lowpass(lowpass_cutoff, fs, order)
    b_high, a_high = butter_highpass(highpass_cutoff, fs, order)

    # Aplicar filtros
    low_freq_signal = apply_filter(signal_data['Amplitude'], b_low, a_low)
    high_freq_signal = apply_filter(signal_data['Amplitude'], b_high, a_high)

    # Salvar dados filtrados em CSV
    filtered_data = pd.DataFrame({'Time': signal_data['Time'], 'Low_Freq_Signal': low_freq_signal, 'High_Freq_Signal': high_freq_signal})
    filtered_data.to_csv(file_filtered, index=False)

    # Visualizar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(signal_data['Time'], signal_data['Amplitude'], label='Original Signal')
    plt.plot(signal_data['Time'], low_freq_signal, label='Low Frequency Signal')
    plt.plot(signal_data['Time'], high_freq_signal, label='High Frequency Signal')
    plt.plot(signal_data['Time'][peaks], low_freq_signal[peaks], 'x', label='Peaks (Low Freq)', color='red')
    plt.plot(signal_data['Time'][peaks], high_freq_signal[peaks], 'x', label='Peaks (High Freq)', color='green')
    plt.legend(loc='upper left')  # Ajuste a posição da legenda
    plt.title('Desagregação de Sinal com Picos')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.show()

# Parâmetros
lowpass_cutoff = 1000  # Ajuste conforme necessário
highpass_cutoff = 500   # Ajuste conforme necessário
fs = 10000  # Ajuste conforme necessário
order = 4    # Ajuste conforme necessário

# Caminho base para os arquivos
base_path = r'C:\Users\jande\OneDrive\Documentos\ADS\Desafio\Arquivos'

# Executar desagregação para cada conjunto de sinais
for i in range(1, 4):
    file_fft = f'643587bee47069204862f69b_3_fft{i}.csv'
    file_signal = f'643587bee47069204862f69b_3_signal{i}.csv'
    file_filtered = f'643587bee47069204862f69b_3_filtered{i}.csv'

    perform_desaggregation(file_fft, file_signal, file_filtered, lowpass_cutoff, highpass_cutoff, fs, order)
