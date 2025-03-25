import uuid

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import pymysql
import json
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from Rapid7ToneDetermination import models
from django.shortcuts import render, HttpResponse
import soundfile as sf
import math
import librosa
from scipy import signal
from scipy.signal import lfilter
import os
import random
import threading

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import random
import uuid
#
# import requests
# response = requests.get(url='', verify=False)
# 用于存储任务状态的字典（仅在内存中存在）
TASKS_STATUS = {}

class RapidUserInfo(APIView):
    def post(self, request, *args, **kwargs):
        # 接收Json，写入数据库
        userJsonStr = request.POST.get('userJson')
        userChooseStr = request.POST.get('userChoose')
        print(userJsonStr)
        print(userChooseStr)
        print(type(userJsonStr))
        userJson = json.loads(userJsonStr)
        userChoose = json.loads(userChooseStr)

        # 判断是七音还是纯音测试还是噪声
        userListenTest = userChoose.get('userListenTest')
        print(userListenTest)
        if(userListenTest == 'pure'):
            userRandomNumber = userJson.get('userRandomNumber')
            userName = userJson.get('userName')
            userAge = userJson.get('userName')
            userSex = userJson.get('userSex')
            HearLoss = userJson.get('HearLoss')
            userLossTime = userJson.get('userLossTime')
            userLEar = userJson.get('userLEar').get('Ear')
            userLEarAid = userJson.get('userLEar').get('Aid')
            userREar = userJson.get('userREar').get('Ear')
            userREarAid = userJson.get('userREar').get('Aid')
            print(type(userRandomNumber))

        elif userListenTest == 'seven' :
            userRandomNumber = userJson.get('userRandomNumber')
            userName = userJson.get('userName')
            userAge = userJson.get('userName')
            userSex = userJson.get('userSex')
            HearLoss = userJson.get('HearLoss')
            userLossTime = userJson.get('userLossTime')
            userLEar = userJson.get('userLEar').get('Ear')
            userLEarAid = userJson.get('userLEar').get('Aid')
            userREar = userJson.get('userREar').get('Ear')
            userREarAid = userJson.get('userREar').get('Aid')
            print(type(userRandomNumber))

        else:
            # 数据库列名
            userRandomNumber = userJson.get('userRandomNumber')
            userName = userJson.get('userName')
            userAge = userJson.get('userName')
            userSex = userJson.get('userSex')
            HearLoss = userJson.get('HearLoss')
            userLossTime = userJson.get('userLossTime')
            userLEar = userJson.get('userLEar').get('Ear')
            userLEarAid = userJson.get('userLEar').get('Aid')
            userREar = userJson.get('userREar').get('Ear')
            userREarAid = userJson.get('userREar').get('Aid')
            print(type(userRandomNumber))
            # userListenSex = userChoose.get('userListenSex')
            # userListenAge = userChoose.get('userListenAge')
            # gaussianNoise = userChoose.get('gaussianNoise')
            # # 写入数据库
            # # 数据库安全：未做
            # models.User.objects.create(userRandomNumber=userRandomNumber, userName=userName, userAge=userAge,
            #                            userSex=userSex,
            #                            HearLoss=HearLoss, userLossTime=userLossTime, userLEar=userLEar, userLEarAid=userLEarAid, userREar=userREar,
            #                            userREarAid=userREarAid)
            # models.UserListen.objects.create(userRandomNumber=userRandomNumber, userListenSex=userListenSex,
            #                                  userListenAge=userListenAge, gaussianNoise=gaussianNoise)
            # # sqlInsertIntoUser = "insert into user values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            # # userRandomNumber, userName, userAge, userSex, HearLoss, userLEar, userLEarAid, userREar, userREarAid)
            # print(request.data)
            #

        return Response({"status": True})




class RapidUploadFile(APIView):
    def post(self, request, *args, **kwargs):
        up_file = request.FILES.get('file')
        models.UploadFileModel(name=up_file.name, path=up_file).save()
        # txt转写为excel 删除原txt文档
        status = 'success'
        return HttpResponse(status)



class RapidGetFile(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        return


class RpaidUploadPure(APIView):
    def post(self, request, *args, **kwargs):
        userPureResult = request.POST.get('answerJson')
        answerJson = json.loads(userPureResult)
        print(answerJson)
        # 读取数据
        userChoose = answerJson.get('userChoose')
        userRandomNumber = answerJson.get('userRandomNumber')
        userChooseERALL = answerJson.get('userChooseERALL')
        # 转数组
        userResult = userChoose
        userResult_r = [0, 0, 0, 0, 0, 0, 0, 0]
        userResultERALL = userChooseERALL
        print((userChoose))
        # 重组数组结果，按照顺序组合[125,250,500,1000,2000,4000,8000,10000]
        t = userResult[6]
        userResult_r[0] = t
        t = userResult[5]
        userResult_r[1] = t
        t = userResult[4]
        userResult_r[2] = t
        t = userResult[0]
        userResult_r[3] = t
        t = userResult[1]
        userResult_r[4] = t
        t = userResult[2]
        userResult_r[5] = t
        t = userResult[3]
        userResult_r[6] = t
        t = userResult[7]
        userResult_r[7] = t
        print(userChoose)
        print(userResult)
        print(userResult_r)
        #绘图
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        ypoints = np.array(userResult_r)
        # 绘制图表
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(xpoints, ypoints)
        # ticks在原数据的范围内,设定主刻度的位置
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
        # 设置 X 轴标签和刻度
        ax.set_xlabel('频率(Hz)')
        ax.set_xticklabels(['125', '250', '500', '1000', '2000', '4000', '8000', '10000'], fontsize=15)
        ax.set_ylabel('听力水平(dB)')
        # x_labels = [125, 250, 500, 1000, 2000, 4000, 8000, 10000]

        plt.ylim((110, -10))
        # plt.xticks(xpoints, x_labels)
        plt.yticks([i * 10 for i in range(-1, 11)]) ## 显示y轴刻度值
        # plt.xlabel('频率(Hz)')
        # plt.ylabel('听力水平(dB)')
        # # plt.plot(xpoints, ypoints, marker='o')
        plt.plot(xpoints, ypoints, color='#B77F70', marker='o')
        plt.grid(linestyle='-.')
        path = 'D:/TUT/Seven/SevenDjang0/static/img/'
        plt.savefig(path+userRandomNumber+'.png')
        plt.show()
        # 判断用户结果是否为0 如果是0 看是否超界 如果超界 减号
        status = 'success'
        return HttpResponse(status)


class RpaidGetNoise (APIView):
    def NoiseWhite(self, NoiseSNR, src, outsrc, sr=16000):
        # 加性高斯白噪声
        src, sr = librosa.core.load(src, sr=sr)
        randomValues = np.random.rand(len(src))
        # 计算语音信号功率Ps和噪声功率Pn1
        Ps = np.sum(src ** 2) / len(src)
        Pn1 = np.sum(randomValues ** 2) / len(randomValues)
        # 计算K值
        k = math.sqrt(Ps / (10 ** (NoiseSNR / 10) * Pn1))
        # 噪声数据乘以K
        randomValuesNeed = randomValues * k
        # 计算新的噪声数据功率
        Pn = np.sum(randomValuesNeed ** 2) / len(randomValuesNeed)
        # 以下开始计算信噪比
        snr = 10 * math.log10(Ps / Pn)
        print("当前信噪比：", snr)
        # 将噪声数据叠加到纯净音频上面
        outdata = src + randomValuesNeed
        # 将叠加噪声的数据写入文件
        sf.write(outsrc, outdata, sr)

    def NoisePink(self, NoiseSNR, src, outsrc, sr=16000):
        src, sr = librosa.core.load(src, sr=sr)
        pinkNoise = np.random.randn(len(src))
        b, a = signal.butter(1, 1 / 2, 'high', analog=False)
        pinkNoise = signal.filtfilt(b, a, pinkNoise)
        Ps = np.sum(src ** 2) / len(src)
        Pn1 = np.sum(pinkNoise ** 2) / len(pinkNoise)
        k = math.sqrt(Ps / (10 ** (NoiseSNR / 10) * Pn1))
        pinkNoise = pinkNoise * k
        Pn = np.sum(pinkNoise ** 2) / len(pinkNoise)
        snr = 10 * math.log10(Ps / Pn)
        print("当前pink信噪比：", snr)
        outdata = src + pinkNoise
        sf.write(outsrc, outdata, sr)

    def NoiseBB(self, NoiseSNR, src, outsrc, sr=16000, num_mixes=5):
        # 获取 babble 文件夹中的所有语音文件
        speech_folder = r"D:\TUT\Seven\SevenDjang0\static\mic\babble"
        all_files = [f for f in os.listdir(speech_folder) if f.startswith('n') and f.endswith('.wav')]

        # 随机选择 num_mixes 个语音文件
        selected_files = random.sample(all_files, num_mixes)
        # 加载所有选中的语音文件
        speech_signals = []
        for file in selected_files:
            file_path = os.path.join(speech_folder, file)
            signal, _ = librosa.load(file_path, sr=sr)
            speech_signals.append(signal)
        # 确定混合长度为最短语音文件长度
        min_length = min([len(signal) for signal in speech_signals])
        truncated_signals = [signal[:min_length] for signal in speech_signals]

        # 混合所有选定的语音段，生成 babble 噪声
        babble_noise = np.sum(truncated_signals, axis=0) / num_mixes  # 归一化

        # 加载纯净语音信号
        clean_speech, _ = librosa.load(src, sr=sr)

        # 将 babble 噪声的长度调整为与 clean_speech 长度相同
        if len(clean_speech) > len(babble_noise):
            # 如果清洁语音信号长，则填充噪声
            babble_noise = np.pad(babble_noise, (0, len(clean_speech) - len(babble_noise)))
        else:
            # 如果噪声长，则截断噪声
            babble_noise = babble_noise[:len(clean_speech)]

        # 计算纯净语音信号和初始 babble 噪声的功率
        Ps = np.sum(clean_speech ** 2) / len(clean_speech)
        Pn1 = np.sum(babble_noise ** 2) / len(babble_noise)

        # 调整 babble 噪声幅值以实现目标信噪比
        k = math.sqrt(Ps / (10 ** (NoiseSNR / 10) * Pn1))
        babble_noise_scaled = babble_noise * k

        # 验证生成噪声的实际信噪比
        Pn = np.sum(babble_noise_scaled ** 2) / len(babble_noise_scaled)
        snr = 10 * math.log10(Ps / Pn)
        print("实际信噪比：", snr)

        # 将调整后的 babble 噪声叠加到纯净语音信号上
        mixed_signal = clean_speech + babble_noise_scaled

        # 保存输出混合信号
        sf.write(outsrc, mixed_signal, sr)
        print(f"生成的带 babble 噪声语音文件保存到: {outsrc}")

    def NoiseSSN(self, NoiseSNR, src, outsrc, sr=16000, n_mels=40):
        # 以临床言语测试为目的，人为对白噪声进行特殊的滤波，在250~1000Hz之间为等能量，在1000~6000Hz间每倍频程递减12dB。
        # 使用梅尔滤波器，频率划分基于梅尔频率标度，它是非线性划分的，低频部分密集，高频部分稀疏，符合人耳对声音的敏感度
        # 这种频率划分方式可以更准确地模拟语音感知，尤其在语音清晰度和语音理解力的测试中
        # 模拟人耳听觉特性：更接近实际听觉感知。
        # 保留语音主要特性：适合语音识别、清晰度测试。
        # 易调整和实现：滤波器数量、频带划分灵活。
        # 抗噪能力强：抑制高频噪声干扰。
        # 与听觉研究一致：结果科学性和合理性强。
        # 加载音频文件
        src, sr = librosa.load(src, sr=sr)

        # 生成白噪声
        randomValues = np.random.randn(len(src))

        # 提取语音信号的梅尔频谱特性
        mel_filter_bank = librosa.filters.mel(sr=sr, n_fft=2048, n_mels=n_mels)
        S = np.abs(librosa.stft(src, n_fft=2048)) ** 2
        mel_spectrogram = np.dot(mel_filter_bank, S)

        # 将白噪声调整为梅尔频谱特性
        noise_spectrogram = mel_spectrogram.mean(axis=1)  # 取平均值生成滤波特性
        noise_filtered = lfilter(noise_spectrogram, [1], randomValues)  # 滤波白噪声

        # 计算语音信号功率和初始噪声功率
        Ps = np.sum(src ** 2) / len(src)
        Pn1 = np.sum(noise_filtered ** 2) / len(noise_filtered)

        # 调整噪声幅值以实现目标信噪比
        k = math.sqrt(Ps / (10 ** (NoiseSNR / 10) * Pn1))
        noise_scaled = noise_filtered * k

        # 验证生成噪声的实际信噪比
        Pn = np.sum(noise_scaled ** 2) / len(noise_scaled)
        snr = 10 * math.log10(Ps / Pn)
        print("实际信噪比：", snr)

        # 将噪声叠加到语音信号上
        outdata = src + noise_scaled

        # 写入输出文件
        sf.write(outsrc, outdata, sr)



#绘制图像
    def wavread(path):
        wavfile = we.open(path, "rb")
        params = wavfile.getparams()
        framesra, frameswav = params[2], params[3]
        nchannels, sampwidth, framesra, frameswav = params[:4]
        print("nchannels:%d" % nchannels)
        print("sampwidth:%d" % sampwidth)
        datawav = wavfile.readframes(frameswav)
        wavfile.close()
        datause = np.fromstring(datawav, dtype=np.short)
        print(len(datause))
        if nchannels == 2:
            datause.shape = -1, 2
        datause = datause.T
        time = np.arange(0, frameswav) * (1.0 / framesra)
        return datause, time, nchannels

    #获取噪声参数类型
    def post(self, request, *args, **kwargs):
        print("Request body:", request.body)
        # userNoiseSet = request.POST.get('newNoiseJSON')
        # NoiseSetJson = json.loads(userNoiseSet)
        data = json.loads(request.body.decode('utf-8'))
        userNoiseSet = data.get('newNoiseSetJSON')
        NoiseSetJson = userNoiseSet
        print(NoiseSetJson)
        # 读取数据
        userChooseSex = NoiseSetJson.get('sex')
        userChooseNoise = NoiseSetJson.get('noise')
        userNoiseSNR = NoiseSetJson.get('SNR')
        userChooseID = NoiseSetJson.get('id')
        #拼接音频地址
        src = f'D:/TUT/Seven/SevenDjang0/static/mic/{userChooseSex}/young/0/{userChooseID}.wav'
        # 临时存储地址
        outNoiseSrc = f'D:/TUT/Seven/SevenDjang0/static/mic/{userChooseSex}/young/0/noise/{userChooseID}.wav'
        print(src)
        # 生成任务 ID，并初始化任务状态
        task_id = str(uuid.uuid4())  # 生成唯一的任务 ID
        TASKS_STATUS[task_id] = 'Pending'  # 设置任务初始状态为 Pending
        # 启动异步线程处理任务
        threading.Thread(target=self.process_noise_task,
                         args=(task_id, userNoiseSNR, src, outNoiseSrc, userChooseNoise)).start()

        # 返回任务 ID 和初始状态给前端
        return JsonResponse({'task_id': task_id, 'status': TASKS_STATUS[task_id]})

    def process_noise_task(self, task_id, userNoiseSNR, src, outNoiseSrc, userChooseNoise):
        try:
            # 更新任务状态为正在处理
            TASKS_STATUS[task_id] = 'Processing'

            # 生成噪声并保存到文件
            # 生成噪声
            if userChooseNoise == 'white':
                # 生成新音频并临时存储
                self.NoiseWhite(userNoiseSNR, src, outNoiseSrc, sr=16000)
            elif userChooseNoise == 'pink':
                # 生成新音频并临时存储
                self.NoisePink(userNoiseSNR, src, outNoiseSrc, sr=16000)
            elif userChooseNoise == 'babble':
                # 生成新音频并临时存储
                self.NoiseBB(userNoiseSNR, src, outNoiseSrc, sr=16000, num_mixes=5)
            else:
                # 生成新音频并临时存储
                self.NoiseSSN(userNoiseSNR, src, outNoiseSrc, sr=16000)

            # 完成处理，更新任务状态为完成
            TASKS_STATUS[task_id] = 'Completed'
            print(f"Task {task_id} completed successfully.")

        except Exception as e:
            # 如果处理过程中出现异常，更新任务状态为失败
            TASKS_STATUS[task_id] = f'Failed: {str(e)}'
            print(f"Task {task_id} failed: {str(e)}")

            # 参数:
            # NoiseSNR: 目标信噪比（单位：dB）
            # src(str): 输入语音文件路径
            # outsrc(str): 输出带噪语音文件路径
            # sr(int): 音频采样率
            # num_mixes(int): 混合的语音段数量，默认为5。
            # n_mels(int): 梅尔滤波器数量（默认40）


# 后端查询生成噪声任务状态接口
class CheckTaskStatusView(APIView):
    def get(self, request, task_id, *args, **kwargs):
        # 获取任务状态
        task_status = TASKS_STATUS.get(task_id, 'Task not found')
        return JsonResponse({'task_id': task_id, 'status': task_status})


#后端查询pure结果图是否生成接口
class CheckIsPureResultImg(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            image_path = data.get('srcimg')  # 从前端接收图片路径

            if not image_path:
                return JsonResponse({'error': 'No image path provided'}, status=400)

            # 检查路径是否存在
            if os.path.exists(image_path):
                return JsonResponse({'exists': True})  # 图片存在
            else:
                return JsonResponse({'exists': False})  # 图片不存在
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



