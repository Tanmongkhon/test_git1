import uvicorn
from fastapi import FastAPI
from action import Action

app = FastAPI()



@app.get("/")
async def read_root():
    return {"Con": "Start"}


@app.get("/hw/get")
async def hw_get():
    data = Action.getHW()
    return data

@app.get("/hw/up")
async def hw_up(ID, status,value):
    data = Action.updateStatusHW(ID, status,value)
    return data

@app.get("/my_name")
def my_name():
    data = "Mongkhon Chaimaha"
    return data

@app.get("/Input_name")
def input_name(name):
    data = name
    return data

@app.get("/equation")
async def equation(s,t):
    data = (f'V={float(s)/float(t):.2f}')
    return data




@app.get("/resistance")
async def resistance(r1,r2,r3):
    data = (f'Series={float(r1)+float(r2)+float(r3):.2f}'),(f'Parallael={1/float(r1)+1/float(r2)+1/float(r3)**-1:.2f}')
    return data






@app.get("/Input_name2")
def input_name2(name,last_name):
    data = "{} {}".format(name,last_name)
    return data

@app.post("/users/up")
async def users_up(ID, name, last_name):
    data = Action.updateusers(ID, name, last_name)
    return data




if __name__ == "__main__":
    uvicorn.run(app, host="10.96.25.106", port=8000)
