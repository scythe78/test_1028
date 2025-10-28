from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Synopsis(BaseModel):
    text: str

def generate_scenario(synopsis: str) -> str:
    """
    Generates a 3-act scenario from a given synopsis.
    (This will later be implemented using an LLM API)
    """
    # TODO: Implement LLM API call
    act_1 = "제1막: 소개\n- 주인공과 배경 소개\n- 일상적인 삶\n- 촉발 사건 발생"
    act_2 = "제2막: 대립\n- 주인공의 목표 설정\n- 갈등 심화\n- 중간점"
    act_3 = "제3막: 해결\n- 절정\n- 하강 액션\n- 결말"

    return f"""# 시나리오 초안\n\n## 시놉시스\n{synopsis}\n\n---\n\n{act_1}\n\n---\n\n{act_2}\n\n---\n\n{act_3}\n"""

@app.post("/generate")
def generate_scenario_endpoint(synopsis: Synopsis):
    scenario = generate_scenario(synopsis.text)
    return {"scenario": scenario}

