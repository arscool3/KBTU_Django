from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

msgs: List[str] = []

@app.get("/msgs/")
async def get_msgs():
    return {"msgs": msgs}

@app.post("/msgs/")
async def add_msg(msg: str):
    msgs.append(msg)
    await bd_msg(msg)
    return {"msg": "Msg added", "content": msg}

class ConnMgr:
    def __init__(self):
        self.cnxs: List[WebSocket] = []

    async def cnct(self, ws: WebSocket):
        await ws.accept()
        self.cnxs.append(ws)

    def dscnct(self, ws: WebSocket):
        self.cnxs.remove(ws)

    async def snd_msg(self, msg: str, ws: WebSocket):
        await ws.send_text(msg)

    async def brdcast(self, msg: str):
        for c in self.cnxs:
            await c.send_text(msg)

mgr = ConnMgr()

# WebSocket endpoint
@app.websocket("/ws")
async def ws_ep(ws: WebSocket):
    await mgr.cnct(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        mgr.dscnct(ws)
    except Exception as e:
        mgr.dscnct(ws)
        print('Error:', e)

async def bd_msg(msg: str):
    await mgr.brdcast(f"New msg: {msg}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)