## VU Software Containerization 2022 - Group 24
---

This repo holds most of the codes and configs for our application.

#### Frontend
- Dockerfile
- server.py
- front.yml

#### Backend
- backend/*

The docker images for backend and frontend have been uploaded to docker hub(lofyin/packmanserver and lofyin/packmanfront).

#### Database
We use the helm package bitnami/postgresql.


#### Deployment

> kubectl create -f front.yml

> kubectl create -f scpackman.yml

> helm repo add bitnami https://charts.bitnami.com/bitnami

> helm install my-release bitnami/postgresql
