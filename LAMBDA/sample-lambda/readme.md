https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html#python-package-create-createfunction-no-dependency

1. Create a lambda function named lambda_function.py
2. Create a zip file with the lambda_function.py as the main file of the zip: zip my-deployment-package.zip lambda_function.py
3. Upload it to s3, and change the aws cloudformation deploy parameters accordingly