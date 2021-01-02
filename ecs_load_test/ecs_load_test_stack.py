from aws_cdk import (
    core, aws_ec2 as ec2,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)

class EcsLoadTestStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "ecs-load-test", cidr="10.0.0.0/22", max_azs=3)

        cluster = ecs.Cluster(self, "load-test-cluser", vpc=vpc)

        repository = ecr.Repository(self, "spring-boot-helloworld", image_scan_on_push=True)

        task_definition = ecs.FargateTaskDefinition( self, "spring-boot-td", cpu=512, memory_limit_mib=2048)

        image = ecs.ContainerImage.from_ecr_repository(repository, "v8")
        container = task_definition.add_container( "spring-boot-container",
                image=image,
                logging=ecs.LogDrivers.aws_logs(stream_prefix="loadtest"))

        port_mapping = ecs.PortMapping(container_port=8080, host_port=8080)
        container.add_port_mappings(port_mapping)

        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "test-service",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=2,
            cpu=512,
            memory_limit_mib=2048,
            public_load_balancer=True)

        fargate_service.target_group.set_attribute("deregistration_delay.timeout_seconds", "10")

