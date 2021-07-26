aws cloudformation deploy --template-file s3.yaml --stack-name s3stack

aws cloudformation deploy --template-file glue.yaml --stack-name gluestacknew

aws cloudformation deploy --template-file gluenodepends.yaml --stack-name gluestacknodepends

aws cloudformation delete-stack --stack-name gluestacknodepends

aws cloudformation delete-stack --stack-name s3stack


