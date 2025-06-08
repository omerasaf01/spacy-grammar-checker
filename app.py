from fastapi import FastAPI
from grammar_checker import check_grammar
from dtos.requests.checking_request import CheckingRequestDto

app = FastAPI()

@app.post("/grammar/check")
def grammer_check(request: CheckingRequestDto):
    return check_grammar(request.text)
