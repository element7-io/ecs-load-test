#!/usr/bin/env python3

from aws_cdk import core

from ecs_load_test.ecs_load_test_stack import EcsLoadTestStack


app = core.App()

env_EU = core.Environment(account="107164128218", region="eu-west-1")
EcsLoadTestStack(app, "ecs-load-test", env=env_EU)

app.synth()
