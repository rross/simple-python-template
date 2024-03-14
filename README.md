# simple-python-template
To be used as a template project to boostrap other projects on the [Temporal Python SDK](https://github.com/temporalio/sdk-python)
This example shows how to start the workflow using the [Temporal Command Line](https://docs.temporal.io/cli).

## Set up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
pip install temporalio
```

## Run Worker Locally
Be sure you set up your Python Virtual Environment before running the worker

```bash
python worker.py
```

## Start Workflow Locally using Temporal CLI
```bash
# run only once
temporal server start-dev
# trigger a workflow locally
temporal workflow start --type SimpleWorkflow --task-queue simple-python-task-queue --input '{"val":"foo"}'
```

## Run Worker using Temporal Cloud
Be sure you set up your Python Virtual Environment before running the worker

```bash
# set up environment variables
export TEMPORAL_NAMESPACE=<namespace>.<accountId>
export TEMPORAL_ADDRESS=<namespace>.<accountId>.tmprl.cloud:7233
export TEMPORAL_TLS_CERT=/path/to/cert
export TEMPORAL_TLS_KEY=/path/to/key
# run the worker
python worker.py
```

## Start Workflow on Temporal Cloud
```bash
# set your temporal environment
temporal env set dev.namespace <namespace>.<accountId>
temporal env set dev.address <namespace>.<accountId>.tmprl.cloud:7233
temporal env set dev.tls-cert-path /path/to/cert
temporal env set dev.tls-key-path /path/to/key 
# trigger a workflow on Temporal Cloud
temporal workflow start --type SimpleWorkflow --task-queue simple-python-task-queue --input '{"val":"foo"}' --env dev
```
