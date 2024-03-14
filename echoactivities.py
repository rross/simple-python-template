from temporalio import activity
from dataclasses import dataclass

@dataclass
class EchoInput:
    val: str

@dataclass
class EchoOutput:
    result: str

class MyActivities:
    def __init__(self, number) -> None:
        self.number = number

    @activity.defn
    async def echo1(self, input: str) -> str:
        activity.logger.info(f"echo1 activity started. Input {input}")
        return input

    @activity.defn
    async def echo2(self, input: str) -> str:
        activity.logger.info("echo2 activity started. Input %s",input)
        return input

    @activity.defn
    async def echo3(self, input: str) -> str:
        activity.logger.info("echo3 activity started. Input %s",input)
        return input

    @activity.defn
    async def echo4(self, input: EchoInput) -> EchoOutput:
        activity.logger.info("echo4 activity started. input = %s",input)

        result = ""
        for i in range(0,self.number):
            result = result + " " + str(i)

        output = EchoOutput(result)
        return output

