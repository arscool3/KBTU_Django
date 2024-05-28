from fastapi import FastAPI
from tasks import update_delivery_status_task, result_backend

app = FastAPI()


@app.get("/update_delivery/{order_id}")
async def update_delivery(order_id: str):
    result = update_delivery_status_task.send(order_id)
    try:
        delivery_status = result.get_result()
        return {"order_id": order_id, "delivery_status": delivery_status}
    except result_backend:
        return {"error": "Task result not found"}