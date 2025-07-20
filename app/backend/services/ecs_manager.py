import boto3
from config import AWS_REGION, ECS_CLUSTER, ECS_TASK_DEFINITION, SUBNETS, SECURITY_GROUPS

ecs = boto3.client("ecs", region_name=AWS_REGION)

def launch_instance(user_id, port):
    response = ecs.run_task(
        cluster=ECS_CLUSTER,
        launchType='FARGATE',
        taskDefinition=ECS_TASK_DEFINITION,
        count=1,
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': SUBNETS,
                'securityGroups': SECURITY_GROUPS,
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [{
                'name': 'chromadb-instance',
                'environment': [
                    {'name': 'USER_ID', 'value': str(user_id)},
                    {'name': 'CHROMADB_PORT', 'value': str(port)}
                ]
            }]
        }
    )
    return response

def stop_instance(task_arn):
    ecs.stop_task(
        cluster=ECS_CLUSTER,
        task=task_arn,
        reason="User-initiated shutdown"
    )

def delete_task_definition(task_def_arn):
    ecs.deregister_task_definition(taskDefinition=task_def_arn)
