Cloud Build
===

use google Cloud Build service

## Repository

in this case, it accesses [github organization's repo][github]

```
#github organization allow access

settings => Applications => Authorized OAuth Apps =>

Google Cloud Platform => Organization access
```

## Container

in this case, it use [google container registry][image-hub]

```bash
#docker auth
$ gcloud auth configure-docker

#login
$ gcloud auth login

#pusg image by Dockerfile
$ gcloud config set project PROJECT_ID
```

## Build

Cloud Build will create docker image by Repository which contain *cloudbuild.yaml* & *Dockerfile*

### cloudbuild.yaml

it's configuration for cloud build, see [intro][config]

**basic filds:**
*   steps:
    *   name:
    *   args:
    *   env:
    *   id:
    *   waitFor:
    *   timeout:
*   timeout:
*   options:
*   images:
*   substitutions:

### Dockerfile

it's configuration for docker image build, see [intro][dockerfile]


[github]: https://help.github.com/articles/requesting-organization-approval-for-oauth-apps/  "how to access github organization's repo"
[image-hub]: https://cloud.google.com/container-registry/docs  "google container registry"
[dockerfile]: https://docs.docker.com/engine/reference/builder/  "docker file intro"
[config]: https://cloud.google.com/cloud-build/docs/build-config  "cloudbuild.yaml intro"