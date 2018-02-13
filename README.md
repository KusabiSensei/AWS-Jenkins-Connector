# AWS-Jenkins-Connector
You have AWS CodeCommit. You have Jenkins. You want them to work together.

# What do you need?

* Python 3.6
```
pip install requests
```
* A recent Jenkins installation on an EC2 instance
* Jenkins AWS CodeCommit Jobs plugin

# What does it do?

When using CodeCommit, you do not have access to pre-receive and post-receive
server side hooks in `git`. The only thing available is to send a message to either
a SNS topic, or call a Lambda function.

In theory, you can use a Lambda function as your integration with just about any
non-Amazon provided service.

This also allows one to automate as much of the setup of Jenkins jobs as possible.

# Yeah, this is dumb. Why not use Travis or CodeBuild? And for that matter, why not GitHub?

AWS CodeBuild could be considered to be a bit....massive....for certain classes of
projects (and for some, it flat out won't do what you want). Also, you have a
very large amount of vendor lock-in, which may not be desirable for your use cases.

Travis, and other cloud hosted CI/Source Control solutions are great (I even use them). However,
not everyone in the world is able to use these solutions, thanks to the wonder of
things called "Corporate IT Policy"

# Okay, but what about Concourse CI?

*sigh* Look, the main point here is not that Jenkins is the be-all end-all of CI
tools, but rather that writing a glue function between Amazon's services (which
want things done the Amazon Way™) and the rest of the world isn't that daunting.

If you want to take what I've done and modify it to support Concourse CI, I'll
be happy to host it here.

# How do I set it up?

You'll need to package the Python file along with the requests library, and upload it
to a new AWS Lambda function. Make sure that your function policy allows CodeCommit
to call it.

Make sure you have Jenkins running, and have created a user who can start builds
from the API (you'll need the API token). You will also want to have CodeCommit
Jobs folders for each region that you have repositories in. Most importantly, you
will want them named according to the AWS region short names (e.g. us-east-1).

Once the region is indexed, any repositories that have a Jenkinsfile set up correctly
will automatically have projects created for them. You can then go into the CodeCommit
settings for the repo, and create a trigger to call the Lambda function.

# That's it?

Yup. You should have Jenkins building upon pushes to CodeCommit, which is as good
as you will get with CodeCommit.

# I want to contribute! How?

* Fork this repository
* Start your work in a new feature branch
* Open a pull request
