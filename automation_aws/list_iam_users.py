"""
to list all iam users:
    1. create boto3 session object by providing the profile name
    2. get iam console.
    3. list all users
Boto3 resource operations returns object
Boto3 client operations returns dictionary
"""
import boto3

aws_mgmt_console = boto3.session.Session(profile_name='root')
iam_console_re = aws_mgmt_console.resource('iam')
iam_console_cli = aws_mgmt_console.client('iam')
""" :type : pyboto3.iam """
# listing iam users using boto3 resource
for each_user in iam_console_re.users.all():
    print(each_user.name)

# listing iam users using boto3 client
for each in iam_console_cli.list_users()['Users']:
    print(each['UserName'])


