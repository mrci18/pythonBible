import boto3
import argparse

def list_instances(tag_key):
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

    return reservations

def get_instance_descriptions(tag_key):
    reservations = list_instances(tag_key)
    for instances in reservations:
        described_instances = instances["Instances"]
        get_public_ip(described_instances)



def get_public_ip(described_instances):

    for address in described_instances:
        if 'PublicIpAddress' in address:
            instance_id = address["InstanceId"]
            print(address['PublicIpAddress'])
            reboot(instance_id)
    #     print(address["PublicIpAddress"])


def reboot(instance_id):
    client = boto3.client('ec2')
    response = client.reboot_instances(
    InstanceIds=[
        instance_id,
    ]
)
    print(response)

def parse_args():
    parser = argparse.ArgumentParser(description="Reboot EC2 instances based on key tag that you specify")


    parser.add_argument("-t", "--tag", dest="tag_key", type=str, action="store", help="input tag's key")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.tag_key == None:
        tag_key = str(raw_input("Enter the key for the tag you are searching for (Ex: Name): "))
    else:
        tag_key = str(args.tag_key)

    get_instance_descriptions(tag_key)

if __name__ == "__main__":
    main()
