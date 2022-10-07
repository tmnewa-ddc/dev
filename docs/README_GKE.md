Kubernetes Engine
===

use google Kubernetes Engine service

## Kubernetes

see [K8S Official Website][k8s] and it's tools below:

*   [ksonnet] : configuration management tool
*   [kubectx] : contexts switcher
*   [kube-ps1][kubeps1], [kube-shell][kubeshell] : for command tips

## Local

how to run Kubernetes locally, see below: 

*   [docker-desktop][kubeDocker]
*   [minikube]
*   [kubeadm-dind] (multi-node)

## GKE

see [intro][gke]

there are some issues:

*   Use [*Ingress*][ingress] instead *Load Balancer* on Service
*   when running cloudbuild, the image with *same tag* will not trigger gke deployment

## Advanced

some advanced tools, see below:

*   [Skaffold]
*   [helm]
*   [Istio]


[k8s]: https://kubernetes.io  "k8s official website"
[ksonnet]: https://ksonnet.io "ksonnet itro"
[kubectx]: https://github.com/ahmetb/kubectx "kubectx intro"
[kubeps1]: https://github.com/jonmosco/kube-ps1 "kube-ps1 intro"
[kubeshell]: https://github.com/cloudnativelabs/kube-shell "kube-shell intro"
[minikube]: https://github.com/kubernetes/minikube "minikube intro"
[kubeadm-dind]: https://github.com/kubernetes-sigs/kubeadm-dind-cluster "kubeadm-dind-cluster intro"
[kubeDocker]: https://blog.docker.com/2018/07/kubernetes-is-now-available-in-docker-desktop-stable-channel/ "k8s on docker-desktop "
[gke]: https://cloud.google.com/kubernetes-engine/docs/ "gke docs"
[ingress]: https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer "ingress setting intro"
[Skaffold]: https://skaffold.dev
[helm]: https://helm.sh/
[Istio]: https://istio.io "istio official website"