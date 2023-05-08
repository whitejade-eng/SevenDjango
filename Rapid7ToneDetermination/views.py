from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import pymysql
import json
from Rapid7ToneDetermination import models
from django.shortcuts import render, HttpResponse


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

        # 数据库列名
        userRandomNumber = userJson.get('userRandomNumber')
        userName = userJson.get('userName')
        userAge = userJson.get('userName')
        userSex = userJson.get('userSex')
        HearLoss = userJson.get('HearLoss')
        userLEar = userJson.get('userLEar').get('Ear')
        userLEarAid = userJson.get('userLEar').get('Aid')
        userREar = userJson.get('userREar').get('Ear')
        userREarAid = userJson.get('userREar').get('Aid')
        print(type(userRandomNumber))

        userListenSex = userChoose.get('userListenSex')
        userListenAge = userChoose.get('userListenAge')
        gaussianNoise = userChoose.get('gaussianNoise')

        # 写入数据库
        # 数据库安全：未做
        models.User.objects.create(userRandomNumber=userRandomNumber, userName=userName, userAge=userAge,
                                   userSex=userSex,
                                   HearLoss=HearLoss, userLEar=userLEar, userLEarAid=userLEarAid, userREar=userREar,
                                   userREarAid=userREarAid)
        models.UserListen.objects.create(userRandomNumber=userRandomNumber, userListenSex=userListenSex,
                                         userListenAge=userListenAge, gaussianNoise=gaussianNoise)
        # sqlInsertIntoUser = "insert into user values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        # userRandomNumber, userName, userAge, userSex, HearLoss, userLEar, userLEarAid, userREar, userREarAid)

        print(request.data)

        return Response({"status": True})



class RapidUnloadFile(APIView):
    def post(self, request, *args, **kwargs):
        up_file = request.FILES.get('file')
        models.UploadFileModel(name=up_file.name, path=up_file).save()
        # txt转写为excel 删除原txt文档
        
        return HttpResponse('success')



class RapidGetFile(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        return
