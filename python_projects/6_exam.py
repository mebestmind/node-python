# 원본 파일명과 저장할 파일명 설정
input_file = 'sample.txt'
output_file = 'converted_sample.txt'

# 변환할 공백 개수 (여기서는 4개로 설정)
space_replacement = '    '

try:
    # 파일을 읽기 모드로 열기
    with open(input_file, 'r', encoding='utf-8') as infile:
        # 변환된 내용을 저장할 파일 열기
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # 각 줄에서 탭 문자를 공백으로 치환
                converted_line = line.replace('\t', space_replacement)
                # 새로운 파일에 쓰기
                outfile.write(converted_line)
    
    print(f"변환이 완료되었습니다. 결과 파일: {output_file}")

except FileNotFoundError:
    print("원본 파일을 찾을 수 없습니다.")