from robyn import Robyn
from rust.rust_math import square

app = Robyn(__file__)

@app.before_request("/")
async def hello_before_request(request):
    print("before_request")
    return request

@app.after_request("/")
def hello_after_request(response):    
    print("after_request")
    return response

@app.get("/")
async def h(request):
    return square(5)

app.start()