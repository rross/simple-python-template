from __future__ import annotations
import asyncio

import dataclasses
from dataclasses import dataclass
from datetime import timedelta

from temporalio import workflow
from temporalio import activity
from temporalio.common import RetryPolicy

from echoactivities import EchoInput, MyActivities

@dataclass
class SimpleInput:
    val: str

@dataclass
class SimpleOutput:
    result: str

@workflow.defn
class SimpleWorkflow:

    def __init__(self) -> None:
        self.sched_to_close_timeout = timedelta(seconds=5)
        self.retry_policy = RetryPolicy(initial_interval=timedelta(seconds=1),
                                        backoff_coefficient=2, 
                                        maximum_interval=timedelta(seconds=30))
    
    @workflow.run
    async def run(self, input: SimpleInput) -> SimpleOutput:
       logger = workflow.logger
       logger.info("Simple workflow started, input = %s |", input.val)

       await workflow.execute_activity(MyActivities.echo1, 
           input.val, 
           schedule_to_close_timeout=self.sched_to_close_timeout,
           retry_policy=self.retry_policy)
       
       await workflow.execute_activity(MyActivities.echo2, 
           input.val, 
           schedule_to_close_timeout=self.sched_to_close_timeout,
           retry_policy=self.retry_policy)
       
       await workflow.execute_activity(MyActivities.echo3, 
           input.val,
           schedule_to_close_timeout=self.sched_to_close_timeout,
           retry_policy=self.retry_policy)

       # sleep for 1 second
       await asyncio.sleep(1)

       echoInput = EchoInput(input.val)
       # execute async
       handle = workflow.execute_activity(MyActivities.echo4, 
            echoInput,
            schedule_to_close_timeout=self.sched_to_close_timeout,
            retry_policy=self.retry_policy)
       
       # do some other stuff
       echoOutput = await handle
       
       return SimpleOutput(echoOutput.result)

       

       