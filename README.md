# AWS-Snapshot-Manager
An AWS Snapshot mangager for snapshoting EBS Volumes in AWS. Written in Python

## About

This is a demo in python which uses boto3 to manage AWS ec2 isntances.

## Configuration

`aws configure --profile <profile_name>`

## Running

`pipenv run python shotty.shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - varies
*project* is optional
