from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def getInfo(ID):
    url = f'https://solved.ac/profile/{ID}'

    options = Options()
    options.add_argument('--headless')  # 창 안 띄움
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(3)  # 로딩 대기 (WebDriverWait로 개선 가능)

    try:
        # 예시: 스트릭이 표시된 요소 잡기 (대략 오른쪽 아래 달력 옆 텍스트)
        element = driver.find_element(By.CSS_SELECTOR,
            '#__next > div.css-axxp2y div div:nth-child(4) div:nth-child(1) div:nth-child(2) div:nth-child(1) div > div')

        print("[Debug] 요소 찾음 ✅")
        print("텍스트 내용:", element.text)  # 여기에 스트릭 들어 있어야 함
        result = element.text.strip()
    except Exception as e:
        print("[Error]", e)
        result = "요소를 찾을 수 없습니다."
    finally:
        driver.quit()

    return result
