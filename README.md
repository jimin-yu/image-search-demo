## Image-serach demo

opensearch knn 플러그인을 이용해서 이미지 유사도 검색을 해보자


### opensearch 로컬에서 실행
```
docker-compose up
```


### opensearch-dashboard 접속
```
http://localhost:5601/
Username: admin
Password: admin
```

### Flask 서버 시작하기
```
python3 -m venv venv
. venv/bin/activate
which python

pip install Flask
```
```
export FLASK_APP=server           # default = app.py
export FLASK_ENV=development      # defaul = production

flask run
```

### 패키지 관리
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

### opensearch 인증서 복사
```
docker cp {opensearch-container-id}:/usr/share/opensearch/config/root-ca.pem ./security
```
