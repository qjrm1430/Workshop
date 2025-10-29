# bad_script.py


def run(data, kind, outfile=None):
    # 정제
    cleaned = []
    for x in data:
        if x and x != "":
            cleaned.append(x.strip())
    # 필터
    if kind == "number":
        filtered = []
        for c in cleaned:
            if c.isdigit():
                filtered.append(c)
    elif kind == "word":
        filtered = []
        for c in cleaned:
            if c.isalpha():
                filtered.append(c)
    else:
        filtered = cleaned
    # 출력 또는 파일 저장
    result = ",".join(filtered)
    if outfile:
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)
