import os

def search(dirname):
    try:
        # 해당 디렉터리에 있는 파일 목록을 가져옴
        filenames = os.listdir(dirname)
        for filename in filenames:
            # 전체 경로 생성
            full_filename = os.path.join(dirname, filename)
            
            # 경로가 디렉터리인지 확인
            if os.path.isdir(full_filename):
                # 디렉터리라면 재귀 호출
                search(full_filename)
            else:
                # 파일 확장자가 .py인 경우 출력
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        # 접근 권한이 없는 디렉터리는 건너뜀
        pass

# 검색을 시작할 디렉터리 지정
search("c:/work")





## os.walk를 사용한 예제
print("os.walk를 사용한 예제")
# 검색할 시작 디렉터리 경로
search_path = "c:/work/"

# os.walk를 사용하여 디렉터리를 순회
for path, dirs, files in os.walk(search_path):
    for filename in files:
        # 파일 확장자가 .py인 경우 전체 경로 출력
        if filename.endswith('.py'):
            print(os.path.join(path, filename))