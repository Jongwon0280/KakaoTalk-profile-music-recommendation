
# 카카오톡 프로필 사진과 User 텍스트를 활용한 프로필음악추천 어플리케이션


## 🎧프로젝트 소개
카카오톡 프로필 사진 및 텍스트를 활용하여 프로필에 적합한 프로필뮤직을 추천해주는 어플리케이션 입니다.

<div style="text-align: center;">
  <img src="https://oasis-mouth-2d1.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fa6bbd52d-4565-47e8-8495-06a47f55eada%2F7752ec5d-5c1c-4457-b5f1-ddc53fe12e58%2FUntitled.png?table=block&id=1c985a73-839a-41c8-a9bb-4f8086f91f70&spaceId=a6bbd52d-4565-47e8-8495-06a47f55eada&width=2000&userId=&cache=v2" alt="이미지 설명" width=700 height=300 >
</div>


<br>

## 🕙개발기간
* 23.06.01일 - 23.11.01일

<br>

## 👨‍👨‍👦‍👦구성원
- 팀장 : 황선웅 - 백엔드 

- 팀원1 : 백서희 - 프론트엔드
  
- 팀원2 : 최종원 - 모델구축 및 모델배포
  
- 팀원3 : 이민호 - 데이터 수집 및 모델배포
  
- 팀원4 : 최다경 - 데이터 수집 및 모델배포


<br>

## 👨‍💻역할
> **모델 구축**
- 얼굴검출 및 감정분류 모델 구축
- 음원 및 텍스트 유사도 추출
  
<br>

> **모델배포**
- AWS lambda를 활용한 모델 서버리스 배포
- 감정별 이미지, 음원메타데이터, 음원임베딩 AWS S3에 적재

<br>

## 💻개발도구
- **Model** : ![Apache Kafka](https://img.shields.io/badge/Tensorflow-A50034?style=flat-square&logo=&logoColor=white)  ![Apache Kafka](https://img.shields.io/badge/Pytorch-EE4C2C?style=flat-square&logo=&logoColor=white)
- **Database** : ![Apache Kafka](https://img.shields.io/badge/S3-FFDF18?style=flat-square&logo=&logoColor=white)
- **Model Deployment** : ![Apache Kafka](https://img.shields.io/badge/AWS_ECR-4285F4?style=flat-square&logo=&logoColor=white) ![Apache Kafka](https://img.shields.io/badge/AWS_S3-43B02A?style=flat-square&logo=&logoColor=white)

<br>

## 📈모델

### 아키텍처

<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/095ca516-eb3c-429f-b979-ed199073679f" alt="이미지 설명" width=700 height=300 >
</div>



### 프로필 이미지 감정분류

> **데이터셋**
>
>  장면의 맥락 정보를 통한 감정 분석을 위한 얼굴 표정 이미지 데이터
> 
> <a href="https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=82"><img src="https://img.shields.io/badge/한국인 감정인식을 위한 복합 영상 Link-222222?style=flat-square&logo=&logoColor=white"/></a>

<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/63be0eef-92df-4c75-a5dc-cefdca7198fa" alt="이미지 설명" width=700 height=300 >
</div>

<br>

> **이미지 전처리 및 예측단계 얼굴검출**
> 
> ![Apache Kafka](https://img.shields.io/badge/Train-4285F4?style=flat-square&logo=&logoColor=white) :  Json 형식의 얼굴좌표를 통해 각 이미지를 cropping 하였음. 음악추천의 도메인을 고려하여 happy, sad, angry, neutral의 이미지를 사용
> 
> ![Apache Kafka](https://img.shields.io/badge/Train-4285F4?style=flat-square&logo=&logoColor=white) ![Apache Kafka](https://img.shields.io/badge/Test-43B02A?style=flat-square&logo=&logoColor=white) : 데이터셋의 이미지를 width : 128 , height : 128로 resizing
> 
> ![Apache Kafka](https://img.shields.io/badge/Test-43B02A?style=flat-square&logo=&logoColor=white) : 사용자의 프로필 이미지에서 얼굴영역을 검출해야하기 때문에, 얼굴영역 검출에 특화된 ![Apache Kafka](https://img.shields.io/badge/MTCNN-0C2074?style=flat-square&logo=&logoColor=white)을 통해 얼굴 검출 후 모델의 입력으로 사용 
> 
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/9bbe6780-0e1f-4701-ab64-cf1a6f627bfb" alt="이미지 설명" width=400 height=300 >
</div>

<br>

> **감정 분류 모델**
> 
> CNN 중 기울기소멸문제에 강력한 ResNet50을 미세튜닝하여 (happy, angry, sad, neutral)로 분류할 수 있게 미세튜닝을 진행.
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/1dd135d6-d589-4874-914a-d992b52fcbf8" alt="이미지 설명" width=400 height=300 >
</div>

<br>

> **하이퍼파라미터**
<table border="1" width ="500" height="100" align = "center">
  <th> Dataset </th>
	<th> Batch </th>
  <th> Epochs </th>
	<th> LearningRate </th>
  <th> KFold-nsplits </th>
  <tr align = "center"><!-- 첫번째 줄 시작 -->
	    <td> AIHUB </td>
      <td> 5 </td>
	    <td> 5  </td>
      <td> 0.00001 </td>
      <td> 	4  </td>
  </tr>
</table>

> **성능**
> 
> Train, Test를 8 : 2로 분할하여 accuracy 및 macro-f1 score를 평가지표로 93.7 , 93.4로 측정하였습니다. 
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/3d09bfc6-9e7c-41d1-a23a-be80dfb8ff5f" alt="이미지 설명" width=400 height=300 
</div>

<br>
<br>
<br>
<br>


### 음원 및 유저 텍스트 유사도 추출

> **데이터셋**
>
>  멜론 음원차트 사이트의 DJ Playlist의 감정별 플레이리스트를 크롤링함.
> 가사내용에서 영어로된 문장과, 중복문장, 문장부호를 제거
>
> <a href="https://www.melon.com/dj/today/djtoday_list.htm
"><img src="https://img.shields.io/badge/멜론 DJ 플레이리스트 링크 Link-222222?style=flat-square&logo=&logoColor=white"/></a>
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/KakaoTalk-profile-music-recommendation/assets/56438131/5d0410a7-063a-4809-9487-3c2e4d5f3ce3" alt="이미지 설명" width=400 height=300 
</div>

<br>
<br>


> **가사와 텍스트 유사도 추출**
>
1. 음원 및 텍스트 임베딩 추출
> Ko-sroberta를 kor-sts로 사후학습시킨 모델을 활용하여 음원과 사용자입력 텍스트의 임베딩을 추출하고, 감정별 음원들의 가사임베딩은 사전에 AWS S3에 적재하여 호출시 불러오도록 구성
> 
> <a href="https://huggingface.co/jhgan/ko-sroberta-multitask
"><img src="https://img.shields.io/badge/ko_sroberta Link-222222?style=flat-square&logo=&logoColor=white"/></a>

<br>

2. 코사인유사도를 통한 Top-k 음원 제공
> S3에 적재한 음원별 문장임베딩과 사용자가 입력한 문장의 임베딩들 간의 코사인유사도를 통해 상위 5곡의 노래를 제공






  




