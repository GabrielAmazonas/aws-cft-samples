### AWS Cloud Formation Template Samples
#### This project aims to provide a starting point for the usage of cloud formation templates

Requirements:
AWS CLI

Official Documentation:
    https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html


Linux:
    sudo apt install awscli

On Windows:
    C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    


Sample Commands:

1. aws cloudformation deploy --template-file s3.yaml --stack-name s3stack
    Deploys the stack defined in the yaml file.

2. aws cloudformation delete-stack --stack-name gluestacknodepends
    Deletes the referenced stack name previously created and its resources. Obs: Always double check the deletion for cleanup purposes


