# ale.py　
# https://github.com/SOICHIRO-NISHIO-github/wav-ale
# 正弦波予測

import numpy as np
import soundfile as sf

#　　　初期設定
N  = 256                    # フレーム長 
#data, rate = sf.read('noisy_speech.wav') # 音声ファイルを読み込む場合
#Len = data.shape[0]        # 音声の長さ
Len = 42600                 # 音声の長さを指定
rate = 44100                # 正弦波予測のサンプリングレート
y   = np.zeros(Len)         # 出力格納変数．長さは入力と同じ
err = np.zeros(Len)         # 誤差信号格納変数 長さは入力と同じ
h   = np.zeros(N)           # パラメータ
m   = np.arange(Len)        # 正弦波作成用(0~音声の長さ)
D   = 50
#uは0~1の値で基本的に決める。0に近いほど細かな予測、1に近いほど大まかな予測。
#小さすぎると元信号を消す可能性がでる。大きすぎるとノイズを除去できなくなる。
u   = 0.01 
m   = np.arange(Len)
data = np.sin(2*np.pi*1000/rate*m)  #正弦波作成

for n in range(N+D,Len):        # メインループ
    x = data[n-D:n-D-N:-1]       # 音声の切り出し
    y[n] = np.dot(x,h)  #予測信号を格納
    e = data[n] - y[n]  #予測誤差の計算
    h = h+u*e*x/np.dot(x,x)  #パラメータを更新
    err[n] = e #予測誤差の格納


sf.write('out_ale.wav', y, rate, format="WAV", subtype="PCM_16") # 作成波形を保存
sf.write('out_ale_err.wav', err, rate, format="WAV", subtype="PCM_16") # 予測誤差波形を保存