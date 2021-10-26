# K8s Base

Basis Template zum Anlegen eines nach [Kubernetes](https://kubernetes.io) deploybaren Projekts.

Dieses Template wird ihnen normalerweise als Ausgangspunkt im Rahmen einer Projekt- oder Abschlussarbeit zur Verfügung gestellt und soll Ihnen die ersten Schritte mit Kubernetes und der Deployment Pipeline von Gitlab vereinfachen.

## Komponenten

Das Template stellt verschiedene öfter genutzte Komponenten zur Verfügung, die sie automatisiert über eine Pipeline deployen und nach eigenem Ermessen anpassen können.

__Ingress:__

- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/): Kubernetes Ingress Resource, um Services Cluster-extern bereitstellen zu können

__Web-Frontend:__

- [Nginx](https://nginx.com): Webserver, z.B. zum Hosten von statischen Webseiten / Web-UIs

__Backend:__

- [Nodejs + express](https://expressjs.com/de/): Web-Framework für Nodejs

__Datenbanken und Storage:__

- [Mongo](https://www.mongodb.com/de-de): MongoDB (NoSQL Document Store)
- [Redis](https://redis.com/): Redis (NoSQL Key-Value Store, Real Time Data)
- [MinIO](https://min.io): Object Storage (Amazon S3-kompatibel)

__Messaging:__

- [RabbitMQ](https://www.rabbitmq.com/): Message Broker

Welche Komponenten Sie deployen wollen, können Sie über die `.gitlab-ci.yml` Datei in diesem Repository steuern:

```
variables:
  DEPLOY_INGRESS: "false"       # deploys Ingress for project if set to true
  DEPLOY_NGINX: "true"          # deploys NGINX static web server if set to true
  DEPLOY_NODEJS_EXPRESS: "true" # deploy nodejs/expressjs if set to true
  DEPLOY_REDIS: "true"          # deploys Redis if set to true
  DEPLOY_MINIO: "true"          # deploys minio if set to true
  DEPLOY_MONGO: "true"          # deploys Mongo if set to true
  DEPLOY_RABBITMQ: "true"       # deploys RabbitMQ if set to true
```

Wenn Sie Kenntnis von Kubernetes haben, können Sie auf Basis dieses Templates auf analoge Art weitere Komponenten ergänzen und in der Deployment Pipeline (`.gitlab-ci.yml`) ergänzen.

## Einsichtnahme in den Cluster

Um Einblick in Ihre Deployments auf einem mit der Deployment Pipeline verknüpften Cluster zu erhalten, wird empfohlen, dass Sie sich [Lens](https://k8slens.dev) installieren.

In diesem Repository ist für Sie in Gitlab unter `Einstellung -> CI/CD -> Variables` eine Umgebungsvariable namens `KUBECONFIG` hinterlegt. In dieser Umgebungsvariable finden Sie die Access Credentials für Ihren Namensraum auf einem Kubernetes-Cluster. Jeder mit Zugriff auf diese Credentials kann Ihr Deployment nach belieben verändern. Diese Access Credentials sind daher vertraulich zu behandeln und nur für Ihren Gebrauch bestimmt.

Kopieren Sie den Inhalt der Umgebungsvariable `KUBECONFIG` aus der Gitlab Weboberfläche und kopieren Sie den Inhalt in Lens mittels `File -> Add Cluster`. Sie sollten dann in Lens unter `Catalog -> Clusters` einen Cluster sehen mit dem sie sich mittels `Connect` verknüpfen können.

Alle in den Clustern deployten Kubernetes-Ressourcen wie Deployments, Services, Ingress, etc. können Sie dann entsprechend einsehen.

![Lens](https://k8slens.dev/images/header-screenshot.png)
