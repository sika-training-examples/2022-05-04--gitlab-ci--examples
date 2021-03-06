# ondrejsika

```
image: sikalabs/ci

stages:
  - build
  - deploy

variables:
  HOST: $CI_PROJECT_PATH_SLUG-$CI_COMMIT_REF_SLUG.$KUBE_INGRESS_BASE_DOMAIN
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA-$CI_PIPELINE_ID

build:
  stage: build
  script:
    - docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
    - docker build -t $IMAGE .
    - docker push $IMAGE

deploy:
  stage: deploy
  script:
    - helm repo add sikalabs https://helm.sikalabs.io
    - helm upgrade --install $CI_PROJECT_PATH_SLUG-$CI_COMMIT_REF_SLUG -n default sikalabs/hello-world
      --set host=$HOST
      --set image=$IMAGE
  environment:
    name: $CI_COMMIT_REF_SLUG
    url: https://$CI_PROJECT_PATH_SLUG-$CI_COMMIT_REF_SLUG.$KUBE_INGRESS_BASE_DOMAIN
    on_stop: stop

stop:
  stage: deploy
  when: manual
  variables:
    GIT_STRATEGY: none
  script:
    - helm uninstall $CI_PROJECT_PATH_SLUG-$CI_COMMIT_REF_SLUG -n default
  environment:
    name: $CI_COMMIT_REF_SLUG
    action: stop 

```
