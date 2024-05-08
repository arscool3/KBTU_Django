from fastapi import Depends, FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect
import requests

app = FastAPI()

# Define a basic HTML page for WebSocket connection
html_page = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
    </head>
    <body>
        <p id='unique_id'><p>
        <script>
            var socket = new WebSocket("ws://127.0.0.1:8000/get_info");

            socket.onmessage = function(event) {
                var message = event.data;
                document.getElementById('unique_id').innerText = message
            };

            socket.onopen = function(event) {
                socket.send("get_traffic_info");
            };
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html_page)

def get_traffic_level():
    response = requests.get("https://jam.api.2gis.com/almaty/meta/score/0/")
    traffic_level = int(response.text[1:-1])
    return traffic_level

@app.websocket("/get_info")
async def get_info(websocket: WebSocket, traffic_level: dict = Depends(get_traffic_level)):
    await websocket.accept()
    while True:
        try:
            message = await websocket.receive_text()
            if message == 'get_traffic_info':
                await websocket.send_text(f"At this time, in Almaty traffic congestion is {traffic_level} out of 10")
            else:
                await websocket.send_text(f"No idea")
        except WebSocketDisconnect:
            break

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

