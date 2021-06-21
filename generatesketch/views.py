from django.shortcuts import render
import urllib.request
from django.core.files.storage import FileSystemStorage
import cv2
# Create your views here.
def index(request):
    return render(request,'index.html')
def files(request):
    if request.method=='POST':
        upfiles = request.FILES['document']
        fs = FileSystemStorage()
        fl = fs.save(upfiles.name,upfiles)
        link = fs.url(fl)
        link = link[1:]
        img = cv2.imread(link)
        cv2.imshow(upfiles.name,img)
        grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        inverted = 255-grayimg
        blurred = cv2.GaussianBlur(inverted,(21,21),0)
        inverted_blur = 255-blurred
        pencil = cv2.divide(grayimg,inverted_blur,scale=256.0)
        cv2.imshow("sketched image",pencil)
        cv2.imwrite("media/superhappy.jpg",pencil)
    return render(request,'files.html',{'names':upfiles.name})