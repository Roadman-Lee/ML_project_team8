# ML_project_team8
## 주제 : 나와 닮은 포켓몬 찾기
![GitHub last commit](https://img.shields.io/github/last-commit/grolarkim/ML_project_team8?style=plastic)

### 조원

김명준 : 머신러닝

박진영 : 프론트

이가을 : 프론트

이상호 : 백엔드

이성 : 백엔드

### 결과 화면

![image](https://user-images.githubusercontent.com/91328539/149513738-3c8926fc-0a2b-4e7d-89ee-c38dfe249063.png)

#### 와이드 프레임
![](https://images.velog.io/images/grolar812/post/0ef78c6d-b79c-4693-8107-57fab6775dcf/image.png)

#### 기능 
| NO. | 기능 | 요청방식 | url | request(프론트에서 ajax 사용시 data에 넣을 것) | response (백엔드에서 jsonify 사용시 넣을것) | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1페이지 렌더링 | GET | / |  | (”index.html”) |  |
| 2 | 2페이지 렌더링 | GET | /upload |  | (”upload.html”) |  |
| 2-1 | 사진 업로드 | POST | /api/upload | form_data"file_give" = file | {'result':'사진 업로드 완료'} |  |
| 2-2 | 드로그앤드롭 | JS only |  |  |  |  |
| 3 | 3페이지 렌더링 | GET | /pokedex |  | (”pokedex.html”,result=result, info=info) |  |
| 3-1 | 예측 결과 및 정보 | GET | / |  |  |  |
| 3-2 | (옵션)진화전/후 포켓몬 정보 | GET |  |  |  |  |
|  |  |  |  |  |  |  |

