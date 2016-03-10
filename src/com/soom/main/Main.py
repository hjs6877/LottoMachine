"""
1. Lotto 번호 생성기 작업. 2016.02.19
(1) 초기 작업 목표
    - 6자리의 랜덤 숫자를 생성한다.
    - 사용자로부터 게임 횟수 입력을 받아서 게임당 6자리의 랜덤 숫자를 생성한다.
    - 생성한 게임을 DB에 저장한다.
    - 생성한 게임을 프린트로 출력한다.
    - 생성한 게임을 메일로 발송한다.
    - 회차별 당첨 번호를 입력 및 저장한다.
(2) 중간 목표
    - 그동안 DB에 저장 된 생성 번호와 회차별 번호를 확률적 통계를 내어 번호를 생성한다.

(3) Advanced 목표
    - Machine Learning 학습 이론을 적용하여 번호를 생성한다.
"""
import random;

print("## How many games do you want?");

gameCount = input();

print("you entered " + gameCount);

lottoGameList = [];
for i in range(1, int(gameCount)+1):
    lottoNumberList = random.sample(range(45), 6);
    lottoNumberList.sort();
    lottoGameList.append(lottoNumberList);

print(lottoGameList);