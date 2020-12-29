from aws_cdk import (
    core, aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)

class EcsLoadTestStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "ecs-load-test", cidr="10.0.0.0/22", max_azs=3)

        cluster = ecs.Cluster(self, "load-test-cluser", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "test-service",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=6,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("springio/gs-spring-boot-docker")),
            memory_limit_mib=2048,      # Default is 512
            public_load_balancer=True)  # Default is False
