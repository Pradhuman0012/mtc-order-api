from fastapi import FastAPI, HTTPException
from uuid import uuid4
from datetime import datetime
from typing import List

from models import OrderCreate, Order
from storage import read_orders, write_orders

app = FastAPI(
    title="MTC Order API",
    version="1.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/orders")
def create_order(order: OrderCreate):

    orders = read_orders()

    record = {
        "id": str(uuid4()),
        "source": order.source,
        "table": order.table,
        "items": [item.dict() for item in order.items],
        "subtotal": order.subtotal,
        "total": order.total,
        "created_at": datetime.utcnow().isoformat(),
        "status": "new"
    }

    orders.append(record)
    write_orders(orders)

    return {"success": True, "order_id": record["id"]}


@app.get("/orders", response_model=List[Order])
def get_orders():

    orders = read_orders()

    return [
        o for o in orders
        if o["status"] == "new"
    ]


@app.post("/orders/{order_id}/complete")
def complete_order(order_id: str):

    orders = read_orders()

    for o in orders:
        if o["id"] == order_id:
            o["status"] = "completed"
            write_orders(orders)
            return {"success": True}

    raise HTTPException(status_code=404, detail="Order not found")