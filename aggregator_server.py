from fastapi import FastAPI, BackgroundTasks

from fastapi.routing import APIRoute
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware


class AggregatorServer:
    def __init__(self):
        self.app = FastAPI(routes=[
            APIRoute('/predict',
                     self.deal_response,
                     response_class=JSONResponse,
                     methods=['POST']

                     ),
        ], log_level='trace', timeout=6000)

        self.app.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True,
            allow_methods=["*"], allow_headers=["*"],
        )

    def aggregate_data(self, data):

        # TODO: post scenario data to scheduler
        pass

    async def deal_response(self, request: Request, backtask: BackgroundTasks):
        data = await request.json()
        backtask.add_task(self.aggregate_data, data)
        return {'msg': 'data send success!'}
