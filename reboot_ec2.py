#!/usr/bin/env python

"""
**************************************************************************************************************
Description: 
Prints a list of EC2 IP's based on the tag key that you specify. 
If you use the -r or --reboot flag, it will also reboot the EC2's listed

**************************************************************************************************************
Prerequisite:
Uses python2.7, if using python3 changed all occurences of 'raw_input()' to 'input()' 
Must have aws cli installed
Must have boto3 installed
Must have aws secret key and id that can access EC2 information configured

**************************************************************************************************************
Usage: 
./reboot_ec2.py -k Env -v Production -r

**************************************************************************************************************
Required arguement:
-k, --key       The tag key you used on AWS. An example is Key: Name, Value: EC2Test1

**************************************************************************************************************
Optional arguements:
-v, --value     The tag value you used on AWS. An example is Key: Env, Value: Production
-r, --reboot    This will reboot the EC2 instance with the applied filter

**************************************************************************************************************
"""

import boto3
import argparse

#Reboots ec2 instance_id's provided
def reboot_ec2(instance_id, instance_ip, reboot_key):
    client = boto3.client('ec2')

    response = client.reboot_instances(InstanceIds = [instance_id,])

    #If http status code is 200 then it will notify you if reboot was succesful
    if response["ResponseMetadata"]["HTTPStatusCode"] >= 200 and response["ResponseMetadata"]["HTTPStatusCode"] < 300:
        print("EC2 with the public IP {} has been rebooted".format(instance_ip))

    else:
        print("{} was not able to reboot".format(instance_ip))

def get_instance_descriptions(tag_key, tag_value, reboot_key):
    client = boto3.client('ec2')

    #List instances with the tag key of tag_key variable, and tag_value(default is *)
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:' + tag_key,
                'Values': [
                    tag_value
                ]
            },
        ]

    )
    reservations = response["Reservations"]

    #Iterate through each instance description and go through the one with assigned Public IP's
    for instances in reservations:
        described_instances = instances['Instances'][0]
        if "PublicIpAddress" in described_instances:
                  
            instance_id = described_instances["InstanceId"]
            instance_ip = described_instances['PublicIpAddress']

            #If -r or --reboot flag was used, call reboot func
            if reboot_key:
                reboot_ec2(instance_id, instance_ip, reboot_key) 
            else:
                print("{}".format(described_instances['PublicIpAddress']))       

#Arg parse for tag key and reboot
def parse_args():
    parser = argparse.ArgumentParser(description="Reboot EC2 instances based on key tag that you specify")

    parser.add_argument("-k", "--key", dest="tag_key", type=str, action="store", help="input tag's key")

    parser.add_argument("-v", "--value", dest="tag_value", type=str, action="store", help="input tag's value")

    parser.add_argument("-r", "--reboot", dest="reboot_key", action="store_true", help="reboot ec2's ")

    return parser.parse_args()

#Main function to run
def main():
    args = parse_args()

    if args.tag_key == None:
        tag_key = str(raw_input("Enter the tag key for the EC2 you are searching for (Ex: Name): ").replace(" ", ""))
    else:
        tag_key = str(args.tag_key)

    if args.tag_value:
        tag_value = str(args.tag_value)
    else:
        tag_value = "*"

    if not args.reboot_key:
        print("\nBelow is a list of EC2 IP's that have the tag key: {}\nIf you wish to reboot the instances please rerun the script with -r or --reboot command flag\n".format(tag_key))

    get_instance_descriptions(tag_key, tag_value, args.reboot_key)

if __name__ == "__main__":
    main()
