import requests


# FastAPI 서버 URL
API_URL = f"https://api.vxfz.top/predict"

# 텍스트를 점자로 번역 (FastAPI 서버에 요청)
def translate_to_braille(text, st):
    print("Text to be translated:", text)  # 전송할 텍스트 확인용
    try:
        response = requests.post(API_URL, json={"input_text": text})
        response.raise_for_status()  # 에러 발생 시 예외 발생
        return response.json().get("prediction", "")
    except requests.exceptions.RequestException as e:
        st.error(f"번역 서버에서 오류가 발생했습니다: {e}")
        return

def convert_unicode_braille_to_ascii_braille(unicode_braille):
    table = {
        k: v for k, v in zip("'⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿",
                             " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)=")
    }
    return ''.join(table.get(c, c) for c in unicode_braille)