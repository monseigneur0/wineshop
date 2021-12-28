from django.shortcuts import render
from .models import User, Wine, manwine #data
from django.views.decorators.csrf import csrf_exempt #token err

from django.http import HttpResponseRedirect, HttpResponse, request
from .forms import UploadFileForm, FileFieldForm
# to uplaod files
import random
import os
# Imaginary function to handle an uploaded file.
import uuid
from datetime import datetime
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.http import HttpResponse #HttpResponse : 응답에 대한 메타정보를 포함한 객체입니다. 로그인 완료시에 "로그인 완료" 라는 text를 띄우기 위해 임포트했습니다.
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from django.contrib import auth


def upload_file(request):
      if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                  handle_uploaded_file(request.FILES['file'])
                  return render(request, "uplaod.html", {'fil': request.FILES['file'].name })
                  # return HttpResponseRedirect('/success/url/')
      else:
            form = UploadFileForm()
      return render(request, 'upload.html', {'form': form})
def handle_uploaded_file(f):
      with open(os.path.abspath('./member/static/' + f.name), 'wb+') as destination:
            for chunk in f.chunks():
                  destination.write(chunk)

def hello(req) :
      return render(req, "a.html" )
def rec(req) :
      new_member = User( userid = req.POST.get('id'), username = req.POST.get('name'), password = req.POST.get('pw'), gender = req.POST.get('gender'), ping_num = req.POST.get('ping'), teachers = req.POST.get('teach'),)
      print(new_member)
      new_member.save()
      return render(req, 'homeboot/homeboot.html')
    #   {'username':req.POST.get('name'), 'info2':req.POST.get('address')}
def send(req) :
      return render(req, 'd.html', {'info1':req.POST.get('name'), 'info2':req.POST.get('address')} )
def novel1(req,chapter, player1,player2) :
      return render(req, 'e.html', {"n1":chapter, "p1":player1 , "p2": player2 } )
def static(req) :
      return render(req, 'f.html')
def schedule(req) :
      return render(req, 'g.html')
def login(req) :
      return render(req, 'login.html')
def join(req) :
      return render(req, 'join.html')
def search(req) :
      all_member = User.object.filter(username="김탁호", password="1234")
      return render(req, 'join.html', {'total_member : all_member'} )
def logged(req) :
      logged_member = User.objects.filter( userid = req.POST.get('user_id'))
      if logged_member :
            req.session['userid'] = req.POST.get('user_id')
            #req.session.get['userid']
            #세션 저장
            #req.session['password'] = req.POST.get('pwd')
            #세션 로드
            #req.session.get['password'] = req.POST.get('pwd')
            #세션삭제
            #req.session.pop['password'] = req.POST.get('pwd')
            #alert(req.session['userid'])
            print("로그인 성공")
            return render(req, 'success.html',{'total_member' : logged_member[0]} )
      elif req.session.get('userid') :
            print(req.session.get('userid'))
            logged_member = User.objects.filter( userid = req.session.get('userid'))
            # logged_member = User.objects.filter( userid = req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'success.html', {'total_member' : logged_member[0]})
      else:
            print("로그인실패")
            return render(req, 'login.html')
def check(req) :
      if req.session.get('userid') :
            print(req.session.get('userid'))
            logged_member = User.objects.filter( userid = req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            return render(req,'check.html', {'total_member' : logged_member[0]})
      else :
            return render(req, 'login.html')
def logout(req) :
    req.session.pop('userid')
    print(req.session.get('userid'))
    print("로그아웃 성공")
    return render(req, 'homeboot/homeboot.html')
def change(req) :
      return render(req, 'change.html')
def changed(req) :
      logged_member = User.objects.get( userid = req.POST.get('user_id'),)
      if logged_member :
            user = User.objects.get(userid = req.POST.get('user_id'))
            print("비밀번호 변경")
            print(logged_member)
            User.password = req.POST.get('pw_changed')
            User.save()
            return render(req, 'success.html', {'total_member' : logged_member[0]})
      else :
            print("로그인실패")
            return render(req, 'failure.html')
def delete(req) :
      #   records = User.objects.all()
      #   records.delete()
      return render(req, 'delete.html')
def deleted(req) :
      logged_member = User.objects.filter( userid = req.POST.get('user_id'), password = req.POST.get('pwd'))
      if logged_member :
            user = User.objects.get(userid = req.POST.get('user_id'))
            print(user)
            user.delete()
            print("유저정보 삭제")
            return render(req, 'deleted.html')
      else :
            print("유저정보 확인 실패")
            return render(req, 'logged.html')
def login2(req) :
      if req.session.get('userid') :
            print(req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'tttt.html')
      else :
            return render(req,'tttt.html')
# 'parameter1' : req.POST.get( 'id_' ), 'parameter2' : req.POST.get( 'pw_' )}
def ajax2(req) :
      logged_member = User.objects.get( userid = req.POST.get('id_'), password = req.POST.get('pw_'))
      print(req.POST.get('id_'))
      print(req.POST.get('pw_'))
      print(logged_member.password)
      if logged_member.password:
            req.session['userid'] = req.POST.get('id_')
            #req.session.get['userid']
            #세션 저장
            #req.session['password'] = req.POST.get('pwd')
            #세션 로드
            #req.session.get['password'] = req.POST.get('pwd')
            #세션삭제
            #req.session.pop['password'] = req.POST.get('pwd')
            #alert(req.session['userid'])
            print(req.session.get('userid'))
            print("로그인 성공")
            print(logged_member)
            return render(req, 'ttt3.html',{'total_member' : logged_member })
      elif req.session.get('userid') :
            print(req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'ttt3.html', {'total_member' : logged_member })
      else:
            print("로그인실패")
            return render(req, 'failure.html',)
def multibox(req) :

      return render(req, 'multibox.html')
def multiview(req) :
      # fruits = req.POST.getlist('fruit')
      return render(req, 'multiboxview.html', {'objects': req.POST.getlist('fruit')})

      # {'info1':req.POST.getlist('objects'), 'info2':req.POST.get('objects')}

def ping(req) :
    users = User.objects.all()
    response_data = {}
    # if req.method == "POST":
    if req.POST.get('user_id') :
        # 처음 로그인 정보 입력시 로그인 확인 및 세션 저장 경로
        login_username = req.POST.get('user_id')
        login_password = req.POST.get('pwd')

        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else :
            myuser = User.objects.get(userid=login_username)
            print(myuser.password)
            print(login_password)
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if login_password == myuser.password :
                req.session['userid'] = myuser.userid
                print(req.session['userid'])
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                login_session = req.session['userid']
                context = {'session' : login_session, 'userss' : users }
                # print(context)
                # # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
                board = User.objects.get(userid=req.session['userid'])
                # # Board는 필자가 Model에서 설정한 DB 이름
                # print(board)
                context['User'] = board
                print("첫로그인성공입니다.")
                # if myuser.teachers == "T" :
                #     return render(req, 'ping.html',context)
                return render(req, 'ping.html',context)
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                print("비밀번호 오류")
                return render(req, 'login.html',response_data)
    # else :
    #     return render(request, 'ping.html')
    elif req.session['userid'] :
        # 세션만 있을 경우
        print(req.session['userid'])
        print("세션 재 로드 성공")
        login_session = req.session['userid']
        # 세션 정보 저장
        context = {'session' : login_session, 'userss' : users }
        # 세션에 세션정보 context에 저장 및 유저스스에 모든 유져들 형식 저장 유저스스는 템플렛에서 사용
        print(context)
        # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
        board = User.objects.get(userid=req.session['userid'])
        # 세션 정보 일치하는 DB항목 찾아와서 보드에 저장
        print(board)
        context['User'] = board
        # context 형식 에 세션 사람 저장
        # peoples= User.objects.filter()
        # return render(req, 'ping.html', {'total_member' : peoples[0]})
        if req.POST.get('no1')  :
            pinguser = User.objects.get(userid = req.session['userid'])
            print(pinguser)
            pinguser.ping_num = req.POST.get('no1')
            print(pinguser.ping_num)
            pinguser.save()
        elif req.POST.get('no2') :
            pinguser = User.objects.get(userid = req.session['userid'])
            pinguser.ping_num = req.POST.get('no2')
            pinguser.save()
        elif req.POST.get('no3') :
            pinguser = User.objects.get(userid = req.session['userid'])
            pinguser.ping_num = req.POST.get('no3')
            pinguser.save()
        elif req.POST.get('pingstart') :
            print("핑 초기화")
            userping = User.objects.all()
            print(userping)
            for userp in userping :
                userp.ping_num = req.POST.get('pingstart')
                userp.save()
        return render(req, 'ping.html', context)
    else:
        # 로그인 입력없고 세션도 없을 경우
        print("처음 페이지 접속")
        return render(req, 'login.html',)

def gprat(req) :
    return render(req, 'gprat.html')


def buy(req, pk) :
    users = User.objects.all()
    response_data = {}
    if req.POST.get('user_id') :
        # 처음 로그인 정보 입력시 로그인 확인 및 세션 저장 경로
        login_username = req.POST.get('user_id')
        login_password = req.POST.get('pwd')

        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."

        else :
            myuser = User.objects.get(userid=login_username)
            print(myuser.password)
            print(login_password)
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if login_password == myuser.password :
                req.session['userid'] = myuser.userid
                print(req.session['userid'])
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                login_session = req.session['userid']
                context = {'session' : login_session, 'userss' : users }
                # print(context)
                # # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
                board = User.objects.get(userid=req.session['userid'])
                # # Board는 필자가 Model에서 설정한 DB 이름
                # print(board)
                context['User'] = board
                print("첫로그인성공입니다.")
                # if myuser.teachers == "T" :
                #     return render(req, 'ping.html',context)
                return render(req, 'shop.html',context)
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                print("비밀번호 오류")
                return render(req, 'shop.html',response_data)
    # else :
    #     return render(request, 'ping.html')
    elif req.session['userid'] :
        # 세션만 있을 경우
        print(req.session['userid'])
        print("세션 재 로드 성공")
        login_session = req.session['userid']
        # 세션 정보 저장
        context = {'session' : login_session, 'userss' : users }
        # 세션에 세션정보 context에 저장 및 유저스스에 모든 유져들 형식 저장 유저스스는 템플렛에서 사용
        print(context)
        # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
        board = User.objects.get(userid=req.session['userid'])
        # 세션 정보 일치하는 DB항목 찾아와서 보드에 저장
        print(board)
        context['User'] = board

        print(pk)
        board = get_object_or_404(Wine, id=pk)
        # Board는 필자가 Model에서 설정한 DB 이름
        context = {'winess' : board }
        context['board'] = board

        print(req.POST.get('buywine'))
        # buywines = Wine.objects.get( wine_photo = req.POST.get('buywine'))
        # alotofwine = Wine.objects.filter()
        # context = {'wines' : buywines }
        # 와인스는 템플렛에서 사용
        # context['wine'] = buywines
        return render(req, 'buy.html', context)
def homeboot(req) :
      return render(req, 'homeboot/homeboot.html')
def shop(req) :
    alotofwine= Wine.objects.all()
    context = {'wines' : alotofwine }
    # Django 템플릿에 사용할 파라미터 값을 변수로 선언 > 사용해야할 인자값이 많아질 때 편리하다.
    # board = get_object_or_404(Board, id=pk)
    # Board는 필자가 Model에서 설정한 DB 이름
    context['wine'] = alotofwine
    return render(req, 'shop.html', context)
# def wineup(req) :
#       return render(req, 'wineup.html')

def wineup(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            todays_date = datetime.now()
            print(todays_date)
            w = str(todays_date.year) + str(todays_date.month).rjust(2,"0") + str(todays_date.day).rjust(2,"0") + str(todays_date.hour).rjust(2,"0") + str(todays_date.minute).rjust(2,"0") + str(todays_date.second).rjust(2,"0") + str(todays_date.microsecond).rjust(2,"0")
            print(w)
            extension = "." + request.FILES['file'].name.split('.')[-1]
            print(extension)
            new_wine = Wine( wine_name = request.POST.get('wname'), wine_price = request.POST.get('wprice'), wine_discribe = request.POST.get('wdiscribe'),wine_photo = 'wineno' + str(w) + str(extension))
            new_wine.save()
            with open(os.path.abspath('./winemall/static/wineno' + str(w) + str(extension)), 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            return render(request, "uplaod.html", {'fil': request.FILES['file'].name })
            # return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'wineup.html', {'form': form})

def bought(req) :
    print(req.session.get('userid'))
    print(req.POST.get('wname'))
    print(req.POST.get('winequant'))
    idid = User.objects.get(userid=req.session.get('userid'))
    winname = Wine.objects.get(wine_name=req.POST.get('wname'))
    wine_order = manwine( id_user = idid, name_wine = winname, wine_num = req.POST.get('winequant'),)
    print(wine_order)
    wine_order.save()
    return render(req, 'bought.html')


def ai(req):
      if req.method == 'POST':
            x_train = torch.FloatTensor([[int(req.POST.get('day1'))],[int(req.POST.get('day2'))],[int(req.POST.get('day3'))]])
            y_train = torch.FloatTensor([[int(req.POST.get('score1'))],[int(req.POST.get('score2'))],[int(req.POST.get('score3'))]])
            W = torch.zeros(1)
            b = torch.zeros(1)

            lr = 0.0002

            epochs = 10000

            len_x = len(x_train)

            for epoch in range(epochs):
                  hypothesis = x_train * W + b
                  cost = torch.mean((hypothesis -y_train)**2)

                  gradient_w = torch.sum((W*x_train - y_train +b)*x_train)/ len_x
                  gradient_b = torch.sum((W*x_train - y_train +b))/len_x

            W -= lr * gradient_w
            b -= lr * gradient_b

            return render( req, 'ai_output.html', { 'W':W.item(), 'b':b.item() } )
      else:
            return render(req, 'ai_input.html')
