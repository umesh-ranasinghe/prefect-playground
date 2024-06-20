from prefect import flow, task
from prefect.blocks.system import Secret

secret_block = Secret.load("sample-secret")

@task
def create_message():
    msg = f"Hello world create by task! The secret is {secret_block.get()}"
    return msg

@flow
def create_another_message():
    msg = "Hello world create by subflow!"
    return msg

@flow
def hello_world():
    task_msg = create_message()
    subflow_msg = create_another_message()
    print(task_msg)
    print(subflow_msg)

if __name__ == '__main__':
    hello_world()