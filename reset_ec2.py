import boto3
import argparse

#Reboots ec2 instance_id's provided
def reboot_ec2(instance_id, instance_ip):
    client = boto3.client('ec2')
    response = client.reboot_instances(
    InstanceIds=[
        instance_id,
    ]
    )

    if response["ResponseMetadata"]["HTTPStatusCode"] >= 200 and response["ResponseMetadata"]["HTTPStatusCode"] < 300:
        print("EC2 with the public IP {} is being deleted".format(instance_ip))

    else:
        print("{} was not able to reboot".format(instance_ip))

# def get_public_ip(described_instances, reboot_key):
#     for address in described_instances:
#         if 'PublicIpAddress' in address:
#             instance_id = address["InstanceId"]
#             instance_ip = address['PublicIpAddress']
            
#             if reboot_key:
#                 reboot_ec2(instance_id, instance_ip)
                
#             else:
#                 print("{}".format(address['PublicIpAddress']))

#List instances with the tag key of tag_key variable
def get_instance_descriptions(tag_key, reboot_key):
    client = boto3.client('ec2')

    response = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:' + tag_key,
                'Values': [
                    '*'
                ]
            },
        ]

    )
    reservations = response["Reservations"]

    for instances in reservations:
        described_instances = instances['Instances'][0]
        if "PublicIpAddress" in described_instances:
                  
            instance_id = described_instances["InstanceId"]
            instance_ip = described_instances['PublicIpAddress']

            if reboot_key:
                reboot_ec2(instance_id, instance_ip)
                
            else:
                print("{}".format(described_instances['PublicIpAddress']))
            
        # get_public_ip(described_instances, reboot_key)

#Arg parse for tag key and reboot
def parse_args():
    parser = argparse.ArgumentParser(description="Reboot EC2 instances based on key tag that you specify")


    parser.add_argument("-t", "--tag", dest="tag_key", type=str, action="store", help="input tag's key")

    parser.add_argument("-r", "--reboot", dest="reboot_key", action="store_true", help="reboot ec2's ")

    return parser.parse_args()

#Main function to run
def main():
    args = parse_args()

    if args.tag_key == None:
        tag_key = str(raw_input("Enter the tag key for the EC2 you are searching for (Ex: Name): ").replace(" ", ""))
    else:
        tag_key = str(args.tag_key)

    if not args.reboot_key:
        print("\nBelow is a list of EC2 IP's that have the tag key: {}\nIf you wish to reboot the instances please rerun the script with -r or --reboot command flag\n".format(tag_key))


    get_instance_descriptions(tag_key, args.reboot_key)

if __name__ == "__main__":
    main()
