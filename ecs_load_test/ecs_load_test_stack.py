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

        task_definition = ecs.FargateTaskDefinition( self, "spring-boot-td", cpu=512, memory_limit_mib=2048)

        image = ecs.ContainerImage.from_registry("springio/gs-spring-boot-docker")
        container = task_definition.add_container( "spring-boot-container", image=image)

        port_mapping = ecs.PortMapping(container_port=8080, host_port=8080)
        container.add_port_mappings(port_mapping)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "test-service",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=2,
            cpu=512,
            memory_limit_mib=2048,
            public_load_balancer=True)
