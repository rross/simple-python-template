import asyncio
import logging
import os

from temporalio.client import Client, TLSConfig
from temporalio.worker import Worker

from simpleworkflow import SimpleWorkflow
from echoactivities import MyActivities

async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(message)s")
    
    address = os.getenv("TEMPORAL_ADDRESS","127.0.0.1:7233")
    namespace = os.getenv("TEMPORAL_NAMESPACE","default")
    tlsCertPath = os.getenv("TEMPORAL_TLS_CERT","")
    tlsKeyPath = os.getenv("TEMPORAL_TLS_KEY","")
    tls = None

    if tlsCertPath and tlsKeyPath:
        with open(tlsCertPath,"rb") as f:
            cert = f.read()
        with open(tlsKeyPath,"rb") as f:
            key = f.read()
                    
        tls = TLSConfig(client_cert=cert,
                        client_private_key=key)

    client = await Client.connect(
        target_host=address, 
        namespace=namespace,
        tls=tls
    )

    myActivity = MyActivities(4)

    worker = Worker(
        client,
        task_queue="simple-python-task-queue",   
        workflows=[SimpleWorkflow],
        activities=[myActivity.echo1, 
                    myActivity.echo2, 
                    myActivity.echo3, 
                    myActivity.echo4],
    )

    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())