
import json

SERVICES = (
    "foo",
    "bar",
    "baz",
    "ahoj",
    "hello",
)

def make_service(name):
    return {
        "build-%s" % name: {
            "stage": "build",
            "script":[
                "echo Build %s" % name,
            ]
        },
        "deploy-%s" % name: {
            "stage": "deploy",
            "script":[
                "echo Deploy %s" % name,
            ]
        }
    }

with open(".gitlab-ci.yml", "w") as f:
    pipeline = {}
    pipeline.update({
        "image": "sikalabs/ci",
        "stages": ["init","build", "deploy"],
        "regenerare-gitlab-ci": {
          "stage": "init",
          "image": "python:3.9",
          "only": {
            "changes": [
              "generate-gitlab-ci.py"
            ]
          },
          "script": [
            "git clone https://ci-bot:HikmMBzkzzuJ6xN_rfmU@gitlab.sikademo.com/example/ondrejsika.git repo",
            "cd repo",
            'git config --global user.email "ci-bot@sikalabs.io"',
            'git config --global user.name "CI Bot"',
            "make generate-gitlab-ci || true",
            "git push"
          ]
        }
    })
    for service in SERVICES:
        pipeline.update(make_service(service))
    f.write(json.dumps(pipeline))
